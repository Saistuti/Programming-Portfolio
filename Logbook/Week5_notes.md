# Week 5 – Scripts, Modules, and Program Files

## Activities I Did
- Created **Python scripts** by saving code in `.py` files and executed them via the command line.  
- Accessed **command-line arguments** using `sys.argv`.  
- Wrote **custom modules** containing functions and variables.  
- Imported modules in different ways:
  - Full module import (`import module_name`)  
  - Specific functions or variables (`from module_name import function_name`)  
  - Using **aliases** (`import module_name as alias`)  
  - Using wildcard (`from module_name import *`) (not recommended)  
- Explored the **module search path** using `sys.path`.  
- Used `dir()` to list contents of imported modules.  
- Checked program execution context with the `__name__` variable to make scripts flexible.

## Summary of Week 5 Lecture
This week focused on **organizing Python code into files** for maintainability and reusability. Code can be saved in **script files (`.py`)** and executed by the interpreter. Scripts can also accept **command-line arguments**, accessed via `sys.argv`, allowing dynamic input.  

Python also supports **modules**, which are `.py` files containing functions, classes, or variables that can be reused in other programs. Modules can be imported in several ways, and imported content can be controlled with **aliases** or selective imports.  

When importing, Python searches in **built-in modules** first, then the **directories listed in `sys.path`**, including the current directory, PYTHONPATH environment variable, and other system paths. Using the special variable `__name__`, a program can determine if it is being **executed as a script** (`__name__ == "__main__"`) or **imported as a module**, allowing code to be reused flexibly.

## Key Technologies Learned
- **Script files**: `.py` files containing Python code.  
- **Executing scripts**: `python my_program.py`  
- **Command-line arguments**: `sys.argv`  
- **Modules**: creating and importing reusable Python files.  
- **Import styles**:
  - `import module_name`  
  - `import module_name as alias`  
  - `from module_name import function_name`  
  - `from module_name import *` (not recommended)  
- **Module search path**: `sys.path`  
- **dir()**: inspecting contents of modules.  
- `__name__` special variable: check if code runs as a script or module.  

## Extra Notes
- **Scripts vs Interactive Mode**: Scripts require `print()` to see output, unlike REPL.  
- **Module initialisation code** executes when imported.  
- Avoid `from module import *` to prevent name clashes.  
- **Aliases** help prevent conflicts with existing names in your program.  
- Using `__name__ == "__main__"` allows **dual-purpose files** that can act as a script or module.  
- `sys.argv` always stores arguments as strings; conversion (e.g., `float`) is needed for arithmetic.  

## Resources
- [Python Official Documentation – Modules](https://docs.python.org/3/tutorial/modules.html)  
- [Python sys Module](https://docs.python.org/3/library/sys.html)  
- [Real Python – Python Modules and Packages](https://realpython.com/python-modules-packages/)  
- [W3Schools – Python Command Line Arguments](https://www.w3schools.com/python/ref_sys_argv.asp)  
