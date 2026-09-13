import ctypes
from ctypes import wintypes
from debugger_define import *
from debugger_function_prototypes import *
from dataclasses import dataclass

@dataclass
class Debugger:
    pid: int=None
    h_process: wintypes.HANDLE=None
    debugger_active: bool=False

    def load(self,path_to_exe:str):
        si=STARTUPINFO()
        pi=PROCESS_INFORMATION()
        si.cb=ctypes.sizeof(si)

        success=kernel32.CreateProcessW(path_to_exe,
                                        None,
                                        None,
                                        None,
                                        False,
                                        CreationFlags.DEBUG_PROCESS,
                                        None,
                                        None,
                                        ctypes.byref(si),
                                        ctypes.byref(pi))
        if success:
            self.pid=pi.dwProcessId
            self.h_process=pi.hProcess
            self.debugger_active=True
            print("[*]Process loaded\n", f"[*]PID: {self.pid}\n",f"[*]TID: {pi.dwThreadId}" )
            self.run(self.pid)
        else:
            print(f"[-] Error: {ctypes.get_last_error()}")

    def open_process(self,pid):
        return kernel32.OpenProcess(AccessRights.PROCESS_ALL_ACCESS,False,pid)

    def attach(self,pid):
        self.h_process=self.open_process(pid)
        if not self.h_process:
            print(f"[-] Failed to open process {ctypes.get_last_error()}")
            return
        if kernel32.DebugActiveProcess(pid):
            self.pid=pid
            self.debugger_active=True
            self.run()
        else:
            print(f"[-] Unable to attach process")
            kernel32.CloseHandle(self.h_process)

    def run(self):
        while self.debugger_active:
            self.get_debug_event()

    def get_debug_event(self):
        debug_ev=DEBUG_EVENT()
        if kernel32.WaitForDebugEvent(ctypes.byref(debug_ev),INFINITE):
            print(f"[*]PID: {debug_ev.dwProcessId}")
            self.detach()
            return
        kernel32.ContinueDebugEvent(debug_ev.dwProcessId,
                               debug_ev.dwThreadId,
                               DBG_CONTINUE)

    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] Finished debugging, exiting ....")
            self.debugger_active=False
            if self.h_process:
                kernel32.CloseHandle(self.h_process)
            return True
        else:
            err=ctypes.get_last_error()
            print(f"[-]Error detaching code: {err}")
            self.debugger_active=False
            return False
        
    def open_thread(self,threadId):
        h_thread=kernel32.OpenThread(AccessRights.THREAD_ALL_ACCESS,False,threadId)
        if h_thread:
            return h_thread
        else:
            print("[-] Could not obtain a valid thread handle.")
            return None

    def enumerate_threads(self):
        thread_entry= THREADENTRY32()
        thread_list= []
        snapshot=kernel32.CreateToolhelp32Snapshot(SnapshotFlags.TH32CS_SNAPTHREAD,self.pid)
        if snapshot:
            thread_entry.dwSize=ctypes.sizeof(thread_entry)
            success=kernel32.Thread32First(snapshot,ctypes.byref(thread_entry))
            while success:
                if thread_entry.th32OwnerProcessId == self.pid:
                    thread_list.append(thread_entry.th32ThreadId)
                success=kernel32.Thread32Next(snapshot,ctypes.byref(thread_entry))
            kernel32.CloseHandle(snapshot)
            return thread_list
        else:
            return []

    def get_thread_context(self, threadId:int):
        context=CONTEXT()
        context.ContextFlags=ContextFlags.FULL | ContextFlags.DEBUG_REGISTERS
        h_thread=self.open_thread(threadId)
        if not h_thread:
            return None

        kernel32.SuspendThread(h_thread)
        success=kernel32.GetThreadContext(h_thread,ctypes.byref(context))
        kernel32.ResumeThread(h_thread)
        kernel32.CloseHandle(h_thread)

        if success:
            return context
        else:
            print(f"[-] GetThreadContext failed: {ctypes.get_last_error()}")
            return None