# Python Objects, References, Mutability, Copying and Identity

## 1. Everything in Python is an Object

In Python, values are objects.

Examples:

```python
username = "hitesh"
score = 100
arr = [1, 2, 3]
```

A useful mental model is:

```text
Values → objects
Names  → references/bindings to objects
```

So:

```python
a = 10
```

can be understood as:

```text
a ─────→ object 10
```

The name `a` refers to an integer object.

Similarly:

```python
a = "chai"
```

means:

```text
a ─────→ "chai" string object
```

### Important

Do not think:

```text
a contains an integer
a contains a string
```

Instead, think:

```text
a ─────→ object
```

The object has a type.

For example:

```python
a = 10
type(a)
# <class 'int'>

a = "chai"
type(a)
# <class 'str'>
```

A better way to say it in an interview:

> A Python name is bound to an object; the object has a type.

---

# 2. Reassigning a Name

Example:

```python
username = "hitesh"
username = "anuj"

print(username)
# anuj
```

Initially:

```text
username ─────→ "hitesh"
```

After reassignment:

```text
username ─────→ "anuj"
```

We are **not changing the `"hitesh"` object**.

We are changing what the name `username` refers to.

---

# 3. Multiple Names Can Refer to the Same Object

Example:

```python
s = 10
y = s

print(y)
# 10
```

Conceptually:

```text
s ─────┐
       ↓
      10
       ↑
y ─────┘
```

Both `s` and `y` refer to the same object.

---

# 4. Reassignment vs Mutation

This is one of the most important concepts in Python.

## Reassignment

```python
s = 10
y = s

s = 15
```

After:

```text
s ─────→ 15

y ─────→ 10
```

We changed what `s` refers to.

We did **not modify the `10` object**.

---

## Mutation

A mutable object can be changed without changing the reference.

Example:

```python
l1 = [1, 2, 3]
l2 = l1

l1[0] = 33
```

Initially:

```text
l1 ─────┐
        ↓
    [1, 2, 3]
        ↑
l2 ─────┘
```

After:

```python
l1[0] = 33
```

the same list object becomes:

```text
l1 ─────┐
        ↓
   [33, 2, 3]
        ↑
l2 ─────┘
```

Therefore:

```python
print(l1)
# [33, 2, 3]

print(l2)
# [33, 2, 3]
```

### Key Difference

```text
Reassignment
    ↓
Changes the binding/reference

Mutation
    ↓
Changes the existing object
```

---

# 5. Example: Reassignment Does Not Affect Another Name

Consider:

```python
l1 = [1, 2, 3]

l2 = l1

l1 = "chai"

print(l2)
# [1, 2, 3]
```

Why?

### Step 1

```python
l1 = [1, 2, 3]
```

```text
l1 ─────→ [1, 2, 3]
```

### Step 2

```python
l2 = l1
```

No new list is created.

```text
l1 ─────┐
        ↓
    [1, 2, 3]
        ↑
l2 ─────┘
```

### Step 3

```python
l1 = "chai"
```

This is reassignment.

Now:

```text
l1 ─────→ "chai"

l2 ─────→ [1, 2, 3]
```

`l2` still refers to the original list.

Therefore:

```python
l2
# [1, 2, 3]
```

---

# 6. Why `l1[0] = 33` Affects `l2`

Consider:

```python
l1 = [1, 2, 3]
l2 = l1

l1[0] = 33
```

Here we are **not reassigning `l1`**.

We are modifying the list object.

Before:

```text
l1 ─────┐
        ↓
    [1, 2, 3]
        ↑
l2 ─────┘
```

After:

```text
l1 ─────┐
        ↓
   [33, 2, 3]
        ↑
l2 ─────┘
```

Therefore:

```python
l1
# [33, 2, 3]

l2
# [33, 2, 3]
```

### Remember

```python
l1 = "chai"
```

→ Reassignment

```python
l1[0] = 33
```

→ Mutation

---

# 7. Mutable vs Immutable Objects

## Immutable Objects

Immutable objects cannot be changed after they are created.

Common examples:

* `int`
* `float`
* `str`
* `bool`
* `tuple`

Example:

```python
username = "hitesh"
username = "anuj"
```

The `"hitesh"` string was not modified.

The name `username` was simply rebound to `"anuj"`.

---

## Mutable Objects

Mutable objects can be changed after creation.

Common examples:

* `list`
* `dict`
* `set`

Example:

```python
a = [1, 2]
b = a

b.append(3)
```

Both names see the change:

```python
a
# [1, 2, 3]

b
# [1, 2, 3]
```

---

# 8. List Assignment Does Not Create a Copy

Consider:

```python
l1 = [1, 2, 3]
l2 = l1
```

It does **not** create two lists.

There is only one list object:

```text
l1 ─────┐
        ↓
    [1, 2, 3]
        ↑
l2 ─────┘
```

Therefore:

```python
l1 is l2
# True
```

---

# 9. Creating a Copy Using Slicing

Consider:

```python
h1 = [1, 2, 3]

h2 = h1[:]
```

`h1[:]` creates a **new list**.

Conceptually:

```text
h1 ─────→ [1, 2, 3]
              Object A

h2 ─────→ [1, 2, 3]
              Object B
```

These are two different list objects.

Now:

```python
h1[0] = 11
```

Only `h1`'s list changes:

```python
h1
# [11, 2, 3]

h2
# [1, 2, 3]
```

And:

```python
h1 is h2
# False
```

But:

```python
h1 == h2
# False
```

after modifying `h1`.

Before modifying `h1`:

```python
h1 = [1, 2, 3]
h2 = h1[:]

h1 == h2
# True

h1 is h2
# False
```

This is called a **shallow copy**.

---

# 10. `==` vs `is`

This is an important interview concept.

## `==` → Equality

`==` checks whether two objects have equal values.

Example:

```python
m = [1, 2, 3]
n = [1, 2, 3]

m == n
# True
```

The values are equal.

---

## `is` → Identity

`is` checks whether two names refer to the **same object**.

Example:

```python
m = [1, 2, 3]
n = m

m is n
# True
```

Both names point to the same list object:

```text
m ─────┐
       ↓
   [1, 2, 3]
       ↑
n ─────┘
```

---

# 11. Same Value but Different Objects

Consider:

```python
m = [1, 2, 3]
n = [1, 2, 3]
```

Conceptually:

```text
m ─────→ [1, 2, 3]   ← Object A

n ─────→ [1, 2, 3]   ← Object B
```

The values are equal:

```python
m == n
# True
```

But the objects are different:

```python
m is n
# False
```

Therefore:

```text
==  → Are the values/equality the same?
is  → Are they the exact same object?
```

---

# 12. Important Examples

### Same object

```python
m = [1, 2, 3]
n = m

m == n
# True

m is n
# True
```

---

### Different objects, same values

```python
m = [1, 2, 3]
n = [1, 2, 3]

m == n
# True

m is n
# False
```

---

### Copy using slicing

```python
h1 = [1, 2, 3]
h2 = h1[:]

h1 == h2
# True

h1 is h2
# False
```

---

# 13. Garbage Collection

When an object is no longer reachable, Python can eventually reclaim its memory.

Example:

```python
a = [1, 2, 3]
a = "chai"
```

The name `a` no longer refers to the list.

If no other references point to that list, it becomes unreachable.

Important:

> Do not assume that garbage collection happens immediately when a reference disappears.

In CPython:

* Reference counting handles many ordinary objects.
* The cyclic garbage collector handles reference cycles.

Numbers and strings do **not** make garbage collection slower simply because they are numbers or strings.

For now, focus on:

```text
Name → Object
```

and:

```text
Reassignment ≠ Mutation
```

---

# 14. Useful Built-in Functions

### `type()`

Checks the type of an object:

```python
type(10)
# <class 'int'>

type("chai")
# <class 'str'>

type([1, 2, 3])
# <class 'list'>
```

### `id()`

Returns an identity value associated with an object during its lifetime:

```python
a = [1, 2, 3]

id(a)
```

You can use it to see whether two names refer to the same object:

```python
m = [1, 2, 3]
n = m

id(m) == id(n)
# True
```

This corresponds to:

```python
m is n
# True
```

### `dir()`

Shows attributes and methods available on an object:

```python
dir("chai")
dir([1, 2, 3])
dir({})
```

---

# 15. Core Mental Model

Always visualize Python like this:

```text
Name
 │
 │ binding/reference
 ↓
Object
 │
 ├── type
 ├── value/state
 └── methods/attributes
```

Example:

```python
a = [1, 2, 3]
```

Think:

```text
a ─────→ List Object
          │
          ├── type → list
          ├── state → [1, 2, 3]
          └── methods → append(), pop(), etc.
```

---

# 16. Interview Takeaways

Remember these:

1. **Everything in Python is an object.**
2. **A name refers to an object; it does not act like a typed container.**
3. **Assignment such as `b = a` normally creates another reference to the same object.**
4. **Reassignment changes a name's binding.**
5. **Mutation changes the existing mutable object.**
6. **Lists, dictionaries, and sets are mutable.**
7. **Integers, floats, strings, booleans, and tuples are immutable.**
8. **`a[:]` creates a new list (shallow copy).**
9. **`==` checks equality/value comparison.**
10. **`is` checks object identity.**
11. **Two names can refer to the same object.**
12. **Two different objects can contain equal values.**
13. **Garbage collection is about reclaiming objects that are no longer reachable.**
14. **Do not assume garbage collection happens immediately.**

The most important diagram to remember:

```text
# Same object

a ─────┐
       ↓
    [1, 2, 3]
       ↑
b ─────┘
```

versus:

```text
# Different objects

a ─────→ [1, 2, 3]

b ─────→ [1, 2, 3]
```

The first:

```python
a is b
# True
```

The second:

```python
a is b
# False

a == b
# True
```
