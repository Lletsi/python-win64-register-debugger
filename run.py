from debugger import Debugger
from tabulate import tabulate

dbg=Debugger()
pid=input("Enter the process ID: ")
dbg.attach(int(pid))
threads=dbg.enumerate_threads()

rows = []
for tid in threads:
    ctx = dbg.get_thread_context(tid)
    if ctx:
        rows.append([
            tid,
            f"{ctx.Rip:#018x}",
            f"{ctx.Rsp:#018x}",
            f"{ctx.Rax:#018x}",
        ])

# Define headers for the table
headers = ["TID", "RIP", "RSP", "RAX"]

# Print the table once
print(f"\nRegisters for PID {pid}\n")
print(tabulate(rows, headers=headers, tablefmt="grid"))