# The Iteration Protocol in Python

Under the hood, Python does not use index-based counting (like traditional C-style `for (int i = 0; ...)` loops) to iterate over collections. Instead, it relies on the **Python Iteration Protocol**, which is powered by two main components: **Iterables** and **Iterators**.

## Key Concepts

- **Iteration Tools (`for`, comprehensions, `map`, etc.)**: Constructs that consume values one by one until the collection is exhausted.
- **Iterable (`[1, 2, 3, 4]`, strings, files, dicts)**: An object capable of returning its members one at a time. It implements `__iter__()`.
- **Iterator**: The helper object that maintains the state of iteration. It implements `__next__()` and raises `StopIteration` when no items remain.

---