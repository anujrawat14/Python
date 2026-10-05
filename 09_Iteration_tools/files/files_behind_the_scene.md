# Python File Objects and Iteration

---

## 1. What Are File Objects in Python?

When you call:

```python
f = open("basic.py")
```

Python returns a **file object** such as `_io.TextIOWrapper`.

Crucially, in Python, **a file object is already its own iterator**.

It implements:

* `__iter__()` → returns `self`
* `__next__()` → reads and returns the next line until the end of the file

---

## 2. Comparing `f.readline()` vs `f.__next__()`

There are two different ways to read lines from a file.

### A. Using `f.readline()`

```python
f.readline()
```

It returns the next line from the file.

At the end of the file (EOF):

```python
f.readline()
```

returns:

```python
''
```

It does **not** raise `StopIteration`.

If called again, it continues to return:

```python
''
```

---

### B. Using `f.__next__()` or `next(f)`

```python
f.__next__()
```

or:

```python
next(f)
```

It returns the next line from the file.

At EOF, it raises:

```python
StopIteration
```

This is part of Python's **Iteration Protocol**.

---

## 3. Why Does `for i in f` Output Nothing?

Suppose we already did:

```python
f.__next__()
```

until the file reached the end and raised:

```python
StopIteration
```

The file object's internal position is now at the **end of the file**.

If we then run:

```python
for i in f:
    print(i)
```

the loop immediately calls:

```python
next(f)
```

Since the file is already exhausted:

```python
StopIteration
```

is raised immediately.

The `for` loop catches `StopIteration` and terminates.

Therefore, nothing is printed.

### Rewind the file

To move the file pointer back to the beginning:

```python
f.seek(0)
```

Now the file can be read again.

---

## 4. Fresh File Handle

Consider:

```python
for i in open("basic.py"):
    print(i)
```

Here is what happens:

1. `open("basic.py")` creates a **new file object**.
2. Its file position starts at `0`.
3. The `for` loop calls `iter()` on the file object.
4. The file's `__iter__()` returns `self`.
5. The loop repeatedly calls `next()`.
6. `next()` internally uses the file object's `__next__()`.
7. Each call returns the next line.
8. The line is stored in `i`.
9. `print(i)` prints the line.
10. At EOF, `StopIteration` is raised.
11. The `for` loop catches it and exits normally.

---

## 5. Why Are There Extra Blank Lines?

Suppose the file contains:

```text
Hello
Python
```

Each line already contains a newline character:

```python
"Hello\n"
```

When we do:

```python
print(i)
```

the `print()` function adds another newline.

Therefore, extra blank spacing can appear.

To avoid this:

```python
print(i, end="")
```

Now `print()` does not add another newline.

---

## 6. Important: File Objects

```python
file = open("data.txt", "r")
```

A file object is **both iterable and an iterator**.

Therefore:

```python
print(iter(file) is file)
```

Output:

```text
True
```

Why?

Because:

```python
iter(file)
```

returns the **same file object**.

We can directly use:

```python
file.__next__()
```

or preferably:

```python
next(file)
```

This gives the **next line from the file**.

---

## 7. List vs File

### List

```python
myList = [1, 2, 3, 4]

print(iter(myList) is myList)
```

Output:

```text
False
```

A list is:

```text
Iterable ✅
Iterator ❌
```

`iter(myList)` creates a separate `list_iterator` object.

---

### File

```python
file = open("data.txt", "r")

print(iter(file) is file)
```

Output:

```text
True
```

A file is:

```text
Iterable ✅
Iterator ✅
```

---

## 8. Summary Cheat Sheet

| Mechanism           | Method          | At EOF                  | Purpose                         |
| ------------------- | --------------- | ----------------------- | ------------------------------- |
| Manual line reading | `f.readline()`  | Returns `''`            | Read a line manually            |
| Iterator protocol   | `next(f)`       | Raises `StopIteration`  | Get next item from iterator     |
| Direct method       | `f.__next__()`  | Raises `StopIteration`  | Calls iterator's next operation |
| `for` loop          | `for line in f` | Catches `StopIteration` | Iterate automatically           |

---

## 9. Most Important Rule

> **Every iterator is iterable, but every iterable is not an iterator.**

### List

```text
List
 ↓
Iterable
 ↓ iter()
List Iterator
```

### File

```text
File Object
 ↓
Iterable + Iterator
```

Therefore:

```python
iter(myList) is myList
# False
```

but:

```python
iter(file) is file
# True
```

---

## 10. Complete Example

```python
# List

myList = [1, 2, 3, 4]

I = iter(myList)

print(I)
# <list_iterator object at ...>

print(next(I))   # 1
print(next(I))   # 2
print(next(I))   # 3
print(next(I))   # 4

# next(I)        # StopIteration
```

```python
# File

file = open("data.txt", "r")

print(iter(file) is file)
# True

print(next(file))
# First line

print(next(file))
# Second line

file.close()
```

The main difference is:

```text
List → Iterable only
       ↓
       iter(list) creates an iterator

File → Iterable + Iterator
       ↓
       iter(file) returns the same file object
```
