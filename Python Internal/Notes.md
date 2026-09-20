# Internal Working of Python

### Overall Flow

```text
Source Code (.py)
       ↓
    Compiler
       ↓
   Bytecode
       ↓
 Python Virtual Machine (PVM)
       ↓
    Execution
```

---

## 1. Source Code → Bytecode

Python source code is compiled into **bytecode**.

```text
.py → Bytecode
```

Bytecode is:

* Low-level representation of Python code
* **Platform-independent** at the Python bytecode level
* **Not machine code**

Example:

```python
x = 10
y = 20
print(x + y)
```

is converted into bytecode instructions that the Python runtime can execute.

> Bytecode is designed to be easier/faster for the Python runtime to execute than repeatedly parsing the original source code.

---

## 2. `.pyc` Files

Compiled bytecode can be stored in `.pyc` files.

```text
.py
 ↓
bytecode
 ↓
.pyc
```

Usually these are found inside:

```text
__pycache__/
```

Example:

```text
__pycache__/
    module.cpython-312.pyc
```

The filename can contain information about the Python implementation and version.

For example:

```text
cpython-312
```

means CPython 3.12.

### When are `.pyc` files commonly created?

They are primarily used for **imported modules**.

When Python imports:

```python
import mymodule
```

Python can compile the module and cache its bytecode in:

```text
__pycache__/
```

Python checks whether the cached bytecode is still valid, including information related to the source file and Python version.

---

## 3. PVM — Python Virtual Machine

The **Python Virtual Machine (PVM)** is the runtime component that executes Python bytecode.

Conceptually:

```text
Bytecode
   ↓
PVM
   ↓
Execution
```

The PVM uses an execution loop to process bytecode instructions.

You can think of it as:

```text
while there are bytecode instructions:
        fetch instruction
        interpret/execute instruction
        move to next instruction
```

The exact implementation is more complicated, but this is the useful interview-level model.

PVM is often described as the **Python interpreter/runtime**.

---

## 4. Bytecode ≠ Machine Code

This is very important.

```text
Python Bytecode
      ≠
Machine Code
```

Bytecode is not directly understood by the CPU.

For example:

```text
Python source
      ↓
Python bytecode
      ↓
CPython runtime
      ↓
Machine-level execution
      ↓
CPU
```

---

## 5. Different Python Implementations

"Python" is a language specification/ecosystem with multiple implementations.

Examples:

### CPython

The standard and most widely used implementation.

```text
Python → CPython
```

CPython is primarily implemented in C.

### PyPy

Alternative Python implementation with a **JIT (Just-In-Time) compiler**.

### Jython

Python implementation running on the **Java Virtual Machine (JVM)**.

### IronPython

Python implementation designed for the **.NET ecosystem**.

Therefore:

```text
Python
 ├── CPython
 ├── PyPy
 ├── Jython
 └── IronPython
```

The exact internal execution process can differ between implementations.

---

## Interview Summary

Remember this:

```text
Source Code (.py)
       ↓
   Compilation
       ↓
    Bytecode
       ↓
      PVM
       ↓
    Execution
```

And the three most important points:

1. **Python source code is compiled to bytecode.**
2. **Bytecode is not machine code.**
3. **The Python runtime/PVM executes the bytecode.**
