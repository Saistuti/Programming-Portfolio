# Week 8 – Input/Output, Output Formatting, and File Handling

## Summary of Week 8 Lecture

This week focused on **Input/Output (I/O) in Python**, including **text formatting** and **file handling**, which are essential for creating professional and maintainable programs.

### Output Formatting
Python provides multiple ways to format text output, which can greatly improve readability:
1. **F-strings (formatted string literals)** – the most modern and concise method:
   - Allows embedding variables and expressions directly within strings
   - Supports format-specifiers for alignment, width, precision, and numeric formatting
2. **str.format() method** – slightly older, but still widely used
   - Offers positional and keyword-based formatting
   - Format-specifiers can be applied similarly to f-strings
3. **Manual formatting** using string methods: `ljust()`, `rjust()`, `center()`, `zfill()`
   - Useful for simple tables or padding output
4. **%-style formatting** – legacy C-style formatting
   - Still supported, but less readable for complex outputs

**Practical takeaway:** Always prefer f-strings in Python 3.6+ for readability and ease of use, especially when formatting multiple variables or expressions.


## Key Technologies Learned
- **Python 3.6+ features**
  - F-strings (formatted string literals)
  - str.format() method
  - %-style formatting (legacy support)
- **File Handling**
  - Text and binary files
  - File modes: `r`, `w`, `a`, `r+`, with optional `b` for binary
  - File object methods: `read()`, `readline()`, `readlines()`, `write()`, `writelines()`, `seek()`, `tell()`, `close()`
  - Context managers (`with` statement) for safe file handling
  - Exception handling: `try...except...finally`
- **Formatting techniques**
  - Alignment: `<`, `>`, `^`
  - Fill characters: `0`, `-`, space
  - Column width and precision
  - Numeric representation: decimal, hexadecimal, binary
- **Practical coding practices**
  - Iterating over files line-by-line
  - Converting non-string types to strings before writing
  - Creating CSV-like output for files
  - Structured output tables for readability


### File Handling
Files are a key source of input/output in real-world applications. Python provides simple yet powerful tools to work with files:

- **Opening files**: `open(filename, mode)` – modes include `r`, `w`, `a`, `r+`, with `b` for binary
- **Reading files**: `read()`, `readline()`, `readlines()`, or iterate over the file object
- **Writing files**: `write()` for strings, `writelines()` for multiple lines
- **File positioning**: `tell()` gives current position, `seek(offset, whence)` moves the pointer
- **Safe file handling**: Use `try...except...finally` to handle exceptions, or the `with` statement to automatically close files

**Practical takeaway:** Always ensure files are closed after use. Use `with` statements whenever possible to reduce errors and improve code safety.


## Activities I Did
- Practiced **text output formatting** using multiple techniques:
  - **F-strings**: `f"Name: {name}, Score: {score:.2f}"`
  - **str.format()**: `"Name: {}, Score: {:.2f}".format(name, score)`
  - **%-style formatting**: `"Score: %.2f" % score`
  - Applied **format-specifiers** for alignment, width, precision, fill characters, numeric base, and center/right/left alignment
- Explored **manual formatting** using string methods: `ljust()`, `rjust()`, `center()`, and `zfill()`
- Practiced **file handling** in Python:
  - Opening files using `open()` in different modes (`r`, `w`, `a`, `r+`) and binary mode (`rb`, `wb`)
  - Reading file contents using `read()`, `readline()`, `readlines()`, and iteration over the file object
  - Writing file contents using `write()` and `writelines()`
  - Controlling file **position** using `tell()` and `seek()`
  - Handling files safely with `try...except...finally` and `with` statements
- Practiced **formatted output of numbers and strings** to create neat tables and reports
- Experimented with **unpacking and writing complex data types** (lists, tuples, dictionaries) to files

### Best Practices Covered
- **Convert non-string data types** (integers, floats, lists, tuples, dictionaries) to strings before writing to files
- Use **format-specifiers** to align and present output neatly
- Prefer **f-strings** over older formatting methods for readability
- Handle file I/O exceptions using **try-except-finally** or **with statements**
- Use **readline() and iteration** for large files to avoid loading entire files into memory
- Apply **seek() and tell()** for precise control over file access


### Examples

**Formatted Table Output**
```python
students = [("John", 78), ("Eric", 98), ("Terry", 100)]
print(f"{'Name':<10} | {'Score':>5}")
print("-"*18)
for name, score in students:
    print(f"{name:<10} | {score:>5d}")
