# Week 6 – Lists, Tuples, and Comprehensions

## Activities I Did
- Reviewed the **list data-type** and practiced creating, indexing, slicing, and concatenating lists.  
- Used various **list methods** such as:
  - `append()`, `extend()`, `insert()`  
  - `remove()`, `pop()`, `clear()`  
  - `sort()`, `reverse()`  
  - `index()`, `count()`, `copy()`  
- Experimented with **list comprehensions** for concise list construction, including:
  - Simple comprehensions: `[x*x for x in range(10)]`  
  - Conditional comprehensions: `[x*x for x in range(10) if x % 2 == 0]`  
  - Nested loops in comprehensions: `[x*y for x in range(1,4) for y in range(1,4)]`  
- Created **tuples**, including empty tuples, single-element tuples, and multi-element tuples.  
- Accessed tuple elements via **indexing, slicing, and sequence unpacking**.  
- Used tuples as **function arguments**, including variable-length argument lists (`*args`).  
- Compared **lists vs tuples** in terms of mutability, homogeneity, and typical use cases.  

## Summary of Week 6 Lecture
This week focused on **Python’s compound sequence types**: lists and tuples.  

**Lists** are ordered, mutable sequences, useful when the number or type of elements may change. Lists support many methods for **adding, removing, sorting, reversing, copying, or counting elements**. They can also be **created programmatically** using list comprehensions, which provide a concise and readable way to generate lists from existing iterables.  

**Tuples** are ordered, **immutable** sequences, typically used to store a small number of **heterogeneous values**. Tuples support **indexing, slicing, counting, and finding elements**, but cannot be modified after creation. Tuples are often used in **function arguments** for variable-length parameter lists (`*args`) and in **sequence unpacking**, which allows multiple assignment in a single statement.  

**Key differences between lists and tuples**:
- **Mutability**: Lists are mutable, tuples are immutable.  
- **Homogeneity**: Lists often store similar data types, tuples often store heterogeneous data.  
- **Usage**: Lists are for collections of data that may change; tuples are for fixed collections, often used as records or function arguments.  

## Key Technologies Learned
- **List methods**: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `sort()`, `reverse()`, `index()`, `count()`, `copy()`  
- **List comprehensions**: concise, programmatic construction of lists  
- **Tuples**: creation, indexing, slicing, packing/unpacking  
- **Variable-length function arguments** using `*args`  
- **Sequence unpacking** for assignment and function calls  

## Extra Notes
- Mutator methods like `append()` or `remove()` **return None**, not the modified list.  
- `del` statement can remove elements or slices of a list, or delete the entire variable.  
- List comprehensions can include **conditional expressions** or multiple `for` loops for nested iteration.  
- Tuple packing/unpacking allows concise multiple assignments, e.g., `x, y, z = (1, 2, 3)`  
- Tuples are commonly used when a **function needs a fixed set of heterogeneous values**.  
- Lists are better suited for **dynamic sequences** that need frequent modification.  

## Resources
- [Python Official Documentation – Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)  
- [Python Official Documentation – Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)  
- [W3Schools – Python List Methods](https://www.w3schools.com/python/python_lists_methods.asp)  
- [W3Schools – Python Tuple](https://www.w3schools.com/python/python_tuples.asp)  
