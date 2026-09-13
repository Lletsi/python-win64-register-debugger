import ctypes
from ctypes import wintypes

#constants as enums
class CreationFlags(int):
    CREATE_NEW_CONSOLE=0x00000010
    DEBUG_PROCESS=0x00000001

class AccessRights(int):
    PROCESS_ALL_ACCESS=0x1F0FFF
    THREAD_ALL_ACCESS=0x1F03FF

class SnapshotFlags(int):
    TH32CS_SNAPTHREAD=0x00000004

class ContextFlags(int):
    FULL=0x00010007
    DEBUG_REGISTERS=0x00010010

INFINITE=0xFFFFFFFF
DBG_CONTINUE=0x00010002

#Load Kernel32
kernel32=ctypes.WinDLL("kernel32", use_last_error=True)

#Structures
class STARTUPINFO(ctypes.Structure):
    _fields_=[("cb",wintypes.DWORD), 
              ("lpReserved",wintypes.LPWSTR),
              ("lpDesktop",wintypes.LPWSTR),
              ("lpTitle",wintypes.LPWSTR),
              ("dwX",wintypes.DWORD),
              ("dwY",wintypes.DWORD),
              ("dwXSize",wintypes.DWORD),
              ("dwYSize",wintypes.DWORD),
              ("dwXCountChars",wintypes.DWORD), 
              ("dwYCountChars",wintypes.DWORD),
              ("dwFillAttribute",wintypes.DWORD),
              ("dwFlags",wintypes.DWORD),
              ("wShowWindow",wintypes.WORD),
              ("cbReserved2",wintypes.WORD),
              ("lpReserved2",ctypes.POINTER(ctypes.c_byte)),
              ("hStdInput",wintypes.HANDLE),
              ("hStdOutput",wintypes.HANDLE),
              ("hStdError",wintypes.HANDLE)]

class PROCESS_INFORMATION(ctypes.Structure):
    _fields_=[
        ("hProcess",wintypes.HANDLE),
        ("hThread",wintypes.HANDLE),
        ("dwProcessId",wintypes.DWORD),
        ("dwThreadId",wintypes.DWORD),
    ]

class DEBUG_EVENT(ctypes.Structure):
    _fields_=[
        ("dwDebugEventCode",wintypes.DWORD),
        ("dwProcessId",wintypes.DWORD),
        ("dwThreadId",wintypes.DWORD),
        ("u",ctypes.c_byte*160)
    ]

class THREADENTRY32(ctypes.Structure):
    _fields_=[
        ("dwSize",wintypes.DWORD),
        ("cntUsage",wintypes.DWORD),
        ("th32ThreadId",wintypes.DWORD),
        ("th32OwnerProcessId",wintypes.DWORD),
        ("tpBasePri",wintypes.LONG),
        ("tpDeltaPri",wintypes.LONG),
        ("dwFlags",wintypes.DWORD)
    ]

LPTHREADENTRY32=ctypes.POINTER(THREADENTRY32)

class FLOATING_SAVE_AREA(ctypes.Structure):
    _fields_=[
        ("ControlWord",wintypes.DWORD),
        ("StatusWord",wintypes.DWORD),
        ("TagWord",wintypes.DWORD),
        ("ErrorOffset",wintypes.DWORD),
        ("ErrorSelector",wintypes.DWORD),
        ("DataOffset",wintypes.DWORD),
        ("DataSelector",wintypes.DWORD),
        ("RegisterArea",wintypes.BYTE *80),
        ("Cr0NpxState",wintypes.DWORD)
    ]

class CONTEXT(ctypes.Structure):
    _fields_=[
        # Home addresses for parameter passing
        ("P1Home", ctypes.c_ulonglong),
        ("P2Home", ctypes.c_ulonglong),
        ("P3Home", ctypes.c_ulonglong),
        ("P4Home", ctypes.c_ulonglong),
        ("P5Home", ctypes.c_ulonglong),
        ("P6Home", ctypes.c_ulonglong),

        # Control flags
        ("ContextFlags", wintypes.DWORD),
        ("MxCsr", wintypes.DWORD),

        # Segment registers and EFlags
        ("SegCs", wintypes.WORD),
        ("SegDs", wintypes.WORD),
        ("SegEs", wintypes.WORD),
        ("SegFs", wintypes.WORD),
        ("SegGs", wintypes.WORD),
        ("SegSs", wintypes.WORD),
        ("EFlags", wintypes.DWORD),

        # Debug registers
        ("Dr0", ctypes.c_ulonglong),
        ("Dr1", ctypes.c_ulonglong),
        ("Dr2", ctypes.c_ulonglong),
        ("Dr3", ctypes.c_ulonglong),
        ("Dr6", ctypes.c_ulonglong),
        ("Dr7", ctypes.c_ulonglong),

        # General purpose registers
        ("Rax", ctypes.c_ulonglong),
        ("Rcx", ctypes.c_ulonglong),
        ("Rdx", ctypes.c_ulonglong),
        ("Rbx", ctypes.c_ulonglong),
        ("Rsp", ctypes.c_ulonglong),
        ("Rbp", ctypes.c_ulonglong),
        ("Rsi", ctypes.c_ulonglong),
        ("Rdi", ctypes.c_ulonglong),
        ("R8", ctypes.c_ulonglong),
        ("R9", ctypes.c_ulonglong),
        ("R10", ctypes.c_ulonglong),
        ("R11", ctypes.c_ulonglong),
        ("R12", ctypes.c_ulonglong),
        ("R13", ctypes.c_ulonglong),
        ("R14", ctypes.c_ulonglong),
        ("R15", ctypes.c_ulonglong),

        # Instruction pointer
        ("Rip", ctypes.c_ulonglong),

        # Floating point / vector registers (simplified here)
        ("DummyBytes", ctypes.c_byte * 512),  # space for XMM/YMM registers
    ]

lpCONTEXT=ctypes.POINTER(CONTEXT)