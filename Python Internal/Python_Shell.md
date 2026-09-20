# Python Shell — Windows

The Python Shell (interactive interpreter) is useful for:

* Quickly testing Python code
* Checking expressions
* Testing modules and functions
* Experimenting without creating a `.py` file

## 1. Enter Python Shell

From Windows CMD:

```cmd
python
```

You'll see:

```text
>>>
```

`>>>` is the **Python prompt**.

To exit:

```python
exit()
```

or press:

```text
Ctrl + Z
Enter
```

---

## 2. Test Expressions

Python can directly evaluate expressions.

```python
>>> "chai" * 4
'chaichaichaichai'
```

Strings can be multiplied by an integer.

---

## 3. Variables

```python
>>> score = 100
>>> print(score)
100
```

Python creates an object containing `100` and the name `score` refers to it.

---

## 4. Check Current Working Directory

First import the `os` module:

```python
>>> import os
>>> os.getcwd()
'C:\\Users\\anujr\\STUDY\\Python'
```

`os.getcwd()` returns the **current working directory** of the Python process.

This is important when working with:

* Files
* Relative paths
* Imports
* Project directories

---

## 5. For Loop in Shell

```python
>>> for c in "chai":
...     print(c)
...
c
h
a
i
```

Notice the difference:

```text
>>> 
```

means Python is ready for a new statement.

```text
...
```

means Python expects more lines because the previous statement isn't complete yet.

For example:

```python
>>> for c in "chai":
...     print(c)
...
```

The indentation is part of Python's syntax.

---

## 6. Check the Operating System

```python
>>> import sys
>>> sys.platform
'win32'
```

`sys.platform` tells you the platform Python is running on.

For Windows:

```text
win32
```

For Linux, you'll commonly see:

```text
linux
```

---

# 7. Importing a Python Module

Suppose you have:

```text
Python/
│
└── 01_Basics/
    └── first.py
```

and `first.py` contains:

```python
print("hello i am first")

def chai(c):
    print(c)

chai_one = "masala chai"
```

If Python can find the module:

```python
>>> import first
hello i am first
```

Notice that:

```python
import first
```

**executes the top-level code** inside `first.py`.

That's why:

```text
hello i am first
```

appears.

---

# 8. Accessing Module Members

After importing:

```python
>>> first.chai("j")
j
```

Here:

```text
first
  ↓
module object
  ↓
chai
  ↓
function
```

You can also access variables defined inside the module:

```python
>>> first.chai_one
'masala chai'
```

The `.` is used to access members of the module.

---

# 9. Reloading a Module

Normally, if a module has already been imported:

```python
>>> import first
```

doing this again:

```python
>>> import first
```

doesn't normally execute the module from scratch again.

Python keeps imported modules in:

```python
sys.modules
```

To explicitly execute the module again:

```python
>>> from importlib import reload
>>> reload(first)
hello i am first
<module 'first' from 'C:\\Users\\anujr\\STUDY\\Python\\01_Basics\\first.py'>
```

`reload()` reloads the already imported module.

---

# 10. Important Import Concept

The import flow is roughly:

```text
import first
      ↓
Python searches for "first"
      ↓
finds first.py
      ↓
loads/compiles the module
      ↓
executes module code
      ↓
creates module object
      ↓
assigns it to the name "first"
```

Then:

```python
first.chai()
```

means:

```text
first
 ↓
module object
 ↓
chai
 ↓
function
```

---

# Quick Revision

```text
python
  ↓
Python Shell
  ↓
>>>
```

Useful commands:

```python
"chai" * 4
```

```python
import os
os.getcwd()
```

```python
import sys
sys.platform
```

```python
import first
```

```python
first.chai("j")
```

```python
first.chai_one
```

```python
from importlib import reload
reload(first)
```

### Important concepts learned here

```text
Python Shell
     ↓
Interactive execution

os.getcwd()
     ↓
Current working directory

sys.platform
     ↓
Current platform

import
     ↓
Load and execute a module

module.member
     ↓
Access module contents

reload()
     ↓
Explicitly reload an imported module

sys.modules
     ↓
Python's cache of loaded modules
```
