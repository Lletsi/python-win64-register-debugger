import ctypes
from ctypes import wintypes
from debugger_define import *

#Function Prototypes
kernel32.CreateProcessW.argtypes=[
    wintypes.LPCWSTR,
    wintypes.LPWSTR,
    wintypes.LPVOID,
    wintypes.LPVOID,
    wintypes.BOOL,
    wintypes.DWORD,
    wintypes.LPVOID,
    wintypes.LPCWSTR,
    ctypes.POINTER(STARTUPINFO),
    ctypes.POINTER(PROCESS_INFORMATION)
]
kernel32.CreateProcessW.restype=wintypes.BOOL

kernel32.OpenProcess.argtypes=[
    wintypes.DWORD,
    wintypes.BOOL,
    wintypes.DWORD
]
kernel32.OpenProcess.restype=wintypes.HANDLE

kernel32.DebugActiveProcess.argtypes=[
    wintypes.DWORD
]
kernel32.DebugActiveProcess.restype=wintypes.BOOL

kernel32.WaitForDebugEvent.argtypes=[
    ctypes.POINTER(DEBUG_EVENT),
    wintypes.DWORD
]
kernel32.WaitForDebugEvent.restype=wintypes.BOOL

kernel32.ContinueDebugEvent.argtypes=[
    wintypes.DWORD,
    wintypes.DWORD,
    wintypes.DWORD
]
kernel32.ContinueDebugEvent.restype=wintypes.BOOL

kernel32.DebugActiveProcessStop.argtypes=[
    wintypes.DWORD
]
kernel32.DebugActiveProcessStop.restype=wintypes.BOOL

kernel32.CloseHandle.argtypes=[
    wintypes.HANDLE
]
kernel32.CloseHandle.restype=wintypes.BOOL


kernel32.OpenThread.argtypes=[
    wintypes.DWORD,
    wintypes.BOOL,  
    wintypes.DWORD 
]
kernel32.OpenThread.restype=wintypes.HANDLE

kernel32.CreateToolhelp32Snapshot.argtypes=[
    wintypes.DWORD,
    wintypes.DWORD 
]
kernel32.CreateToolhelp32Snapshot.restype=wintypes.HANDLE

kernel32.Thread32First.argtypes=[
    wintypes.HANDLE,
    LPTHREADENTRY32
]
kernel32.Thread32First.restype=wintypes.BOOL

kernel32.Thread32Next.argtypes=[
    wintypes.HANDLE,
    LPTHREADENTRY32
]
kernel32.Thread32Next.restype=wintypes.BOOL

kernel32.SuspendThread.argtypes=[
    wintypes.HANDLE
]
kernel32.SuspendThread.restype=wintypes.DWORD

kernel32.ResumeThread.argtypes=[
    wintypes.HANDLE
]
kernel32.ResumeThread.restype=wintypes.DWORD

kernel32.GetThreadContext.argtypes=[
    wintypes.HANDLE,
    lpCONTEXT
]
kernel32.GetThreadContext.restype=wintypes.BOOL

kernel32.SetThreadContext.argtypes=[
    wintypes.HANDLE, #hThread
    lpCONTEXT
]
kernel32.SetThreadContext.restype=wintypes.BOOL