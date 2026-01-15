# Week 4 – Functions and Lambda Expressions

## Activities I Did
- Practiced **importing built-in and external functions** from modules using `import` and `from ... import`.  
- Used functions from the **math** and **decimal** modules, including `sqrt()`, `pi`, and `Decimal()`.  
- Defined my own **functions** using `def`, with and without parameters.  
- Added **docstrings** to functions for documentation.  
- Experimented with **default arguments** and **keyword arguments** to call functions flexibly.  
- Created functions with **variable-length argument lists** using `*args`.  
- Explored **arbitrary keyword arguments** using `**kwargs` and processed them as dictionaries.  
- Implemented **lambda expressions** for small anonymous functions.  
- Used lambda functions as arguments to built-in functions like `sorted()` for custom sorting.

## Summary of Week 4 Lecture
This week focused on **functions**, both pre-defined and user-defined, which allow us to reuse and organize code effectively. Python provides thousands of built-in functions and libraries, which can be imported selectively to reduce namespace clutter. User-defined functions are created with `def`, can take **formal parameters**, and may return values with `return`. Parameters can have **default values**, and functions can also accept **variable-length positional (`*args`) and keyword arguments (`**kwargs`)** for more flexibility. **Lambda expressions** were introduced as a concise way to create small, anonymous functions, useful especially when functions are used as arguments in other functions like `sorted()`. Proper use of docstrings and parameter handling improves code readability, reusability, and maintainability.

## Key Technologies Learned
- Importing modules and functions: `import math`, `from math import sqrt`  
- Using external data types: `Decimal` from the `decimal` module  
- User-defined functions: `def` keyword, parameters, `return`  
- Function arguments: positional, keyword, default, `*args`, `**kwargs`  
- Anonymous functions: `lambda` expressions  
- Using functions as arguments: e.g., `sorted(list, key=lambda ...)`  
- Docstrings for documenting functions  

## Extra Notes
- Avoid `from module import *` to prevent namespace pollution.  
- Default arguments must appear **after positional arguments** in function definitions.  
- Keyword arguments improve readability and allow calling functions out of order.  
- `*args` allows any number of positional arguments; `**kwargs` allows any number of named arguments.  
- Lambda expressions are **single-expression functions**, cannot contain multiple statements or loops, but are very handy for short, on-the-fly operations.  
- Functions are local in scope: variables defined inside functions do not exist outside unless declared global.  
- Using modules like `decimal` avoids floating-point precision errors for financial calculations.  

## Some built-in functions
- abs()
- dict()
- chr()
- int()
- input()
- print()
- bool()
- __import__()
- exec()
- slice()
- round()
- ascii()


## Resources
- [Python Official Documentation – Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
- [Real Python – Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)  
- [Python Module Index](https://docs.python.org/3/py-modindex.html)  
- [W3Schools – Python Lambda](https://www.w3schools.com/python/python_lambda.asp)  
