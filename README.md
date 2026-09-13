# Python Win64 Register Debugger

This project is a **Python-based Windows x64 debugger** built with the `ctypes` library.  
It interacts directly with the Windows API to:
- Attach to running processes
- Enumerate threads
- Retrieve and display CPU register states (RIP, RSP, RAX, etc.)

Registers are displayed in a tabulated format for easier inspection.

## 📸 Example Output

Here’s how the debugger displays thread registers:

![Debugger output screenshot](images/screenshot.png)


## 📖 Background

This project was **inspired by and adapted from examples in *Gray Hat Python* by Justin Seitz**.  
The original book demonstrates low-level debugging concepts in Python.  
I extended and modified the code to:
- Support **Windows x64 debugging**
- Use `ctypes` for direct Windows API calls
- Add **thread enumeration** and **register inspection**
- Provide cleaner, tabulated output

By building on the educational examples in *Gray Hat Python*, this project shows how those concepts can be applied and expanded for modern 64-bit Windows environments.

---

## ⚙️ Requirements

- Windows 10/11 (x64)
- Python 3.10+
- Dependencies:
  ```bash
  pip install tabulate

