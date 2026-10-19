# Python Decorators — Notes

## 1. What is a Decorator?

A **decorator** is a function that adds extra functionality to another function without modifying its original code.

Common uses:
- Measuring execution time
- Logging function calls
- Caching results
- Checking permissions
- Modifying class or function behaviour

#  Custom Decorators

### Basic Syntax

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")

        result = func(*args, **kwargs)

        print("After function execution")
        return result

    return wrapper


@my_decorator
def greet(name):
    print(f"Hello, {name}")


greet("Anuj")
```
# Built in  Decorators

| **Decorator** | **Source Module** | **Primary Use Case** |
|---|---|---|
| `@property` | Built-in | Encapsulate attribute access with getter, setter, and deleter logic |
| `@classmethod` | Built-in | Factory constructors and class-level operations using `cls` |
| `@staticmethod` | Built-in | Utility methods independent of instance or class state |
| `@dataclass` | `dataclasses` | Automatically generate methods such as `__init__`, `__repr__`, and `__eq__` |
| `@lru_cache` / `@cache` | `functools` | Cache results of repeated function calls (memoization) |
| `@wraps` | `functools` | Preserve original function metadata in custom decorators |
| `@singledispatch` | `functools` | Function-level polymorphism based on the type of the first argument |
| `@abstractmethod` | `abc` | Require subclasses to implement specified methods |
