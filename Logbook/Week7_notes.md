# Week 7 – Sets, Dictionaries, and Choosing Collection Types

## Activities I Did
- Created and manipulated **sets**, including:
  - Adding elements with `add()` and updating sets with `update()`
  - Removing elements with `remove()`, `pop()`, and `difference_update()`
  - Using **set operations**: union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`)
  - Constructed sets using **set comprehensions**, e.g., `{x*x for x in range(10) if x % 2 == 0}`
  - Created **immutable sets** using `frozenset()` and practiced accessor operations
- Explored **set comparisons**:
  - Subset (`<=`), proper subset (`<`), superset (`>=`), proper superset (`>`)
- Created and manipulated **dictionaries**:
  - Creating dictionaries using `{key:value}`, `dict()`, and dictionary comprehensions `{x:x**x for x in range(2,8)}`
  - Accessing and updating elements using keys, e.g., `stock["apple"] += 1`
  - Removing elements with `del` or `pop()`
  - Iterating over dictionaries using `keys()`, `values()`, and `items()`
- Used **dictionaries as function arguments**:
  - Arbitrary keyword arguments packed into a dictionary using `**kwargs`
  - Unpacked dictionaries into function calls using `**` operator
- Compared **lists, tuples, sets, and dictionaries**:
  - Practiced selecting the appropriate collection type based on mutability, order, uniqueness, and type of data

## Summary of Week 7 Lecture
This week focused on **Python’s advanced collection types**, **sets** and **dictionaries**, and their comparison with lists and tuples.  

**Sets** are unordered collections of unique elements. They do not allow duplicates, and indexing or slicing is not supported. Sets are **mutable**, support **membership testing**, and can be manipulated using both **operators** and **methods**. Immutable sets can be created using `frozenset()`. Sets can also be created using **set comprehensions**.  

**Dictionaries** store **key:value pairs**, where keys are unique and immutable, and values can be of any type. Dictionaries are **mutable** and ordered (from Python 3.7 onwards). They support addition, removal, and iteration over keys, values, or key-value pairs. Dictionaries can also be created using **dictionary comprehensions**.  

**Key points for using collections**:
- **Lists**: ordered, mutable, often homogeneous, indexing supported, dynamic content  
- **Tuples**: ordered, immutable, heterogeneous, small collections, fixed content  
- **Sets**: unordered, mutable, no duplicates, membership testing, dynamic content, typically homogeneous  
- **Dictionaries**: key-value pairs, fast lookups by key, keys unique and immutable, values can be mutable or heterogeneous  

## Key Functions and Methods
- **Set Methods**: `add()`, `remove()`, `pop()`, `update()`, `union()`, `intersection()`, `difference()`, `issubset()`, `issuperset()`  
- **Dictionary Methods**: `get()`, `pop()`, `update()`, `keys()`, `values()`, `items()`, `clear()`, `copy()`  
- **Comprehensions**:
  - Set: `{expression for item in iterable if condition}`  
  - Dictionary: `{key_expression: value_expression for item in iterable}`  

## Extra Notes
- Sets and dictionaries can be constructed from other collections, e.g., `set(list)` or `dict(list_of_tuples)`  
- Use **sets** when uniqueness and membership testing are required  
- Use **dictionaries** when mapping unique keys to values is needed  
- Understanding the characteristics of each collection type helps select the **most efficient and appropriate data structure** for a given problem  

## Resources
- [Python Official Documentation – Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)  
- [Python Official Documentation – Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)  
- [W3Schools – Python Set](https://www.w3schools.com/python/python_sets.asp)  
- [W3Schools – Python Dictionary](https://www.w3schools.com/python/python_dictionaries.asp)  
