# Python Mutable & Immutable — Java Connection

Python's object/reference behavior is closely related to the concepts of **mutable and immutable objects in Java**.

---

## 1. Reassignment — Python

```python
s = 10
y = s

s = 15

print(s)
# 15

print(y)
# 10
```

Conceptually:

```text
Initially:

s ─────┐
       ↓
      10
       ↑
y ─────┘
```

After:

```python
s = 15
```

```text
s ─────→ 15

y ─────→ 10
```

We did **not change the `10` object**.

We changed what `s` refers to.

---

# 2. Similar Concept in Java

Consider:

```java
String a = "hello";
String b = a;

a = "world";
```

Conceptually:

```text
Initially:

a ─────┐
       ↓
    "hello"
       ↑
b ─────┘
```

After:

```java
a = "world";
```

```text
a ─────→ "world"

b ─────→ "hello"
```

This is similar to Python.

The important idea is:

> Reassigning a variable/name changes its reference/binding. It does not modify the previous object.

---

# 3. Mutable Objects

Now consider a mutable object.

### Java

```java
ArrayList<Integer> a = new ArrayList<>();

a.add(10);

ArrayList<Integer> b = a;

b.add(20);

System.out.println(a);
```

Output:

```text
[10, 20]
```

Why?

Because both references point to the **same ArrayList object**:

```text
a ─────┐
       ↓
   ArrayList
       ↑
b ─────┘
```

When:

```java
b.add(20);
```

the actual object is modified.

Therefore `a` also sees the change.

---

# 4. Same Concept in Python

```python
a = [10]
b = a

b.append(20)

print(a)
```

Output:

```text
[10, 20]
```

Both names refer to the same list object:

```text
a ─────┐
       ↓
   [10, 20]
       ↑
b ─────┘
```

`b.append(20)` modifies the existing list object.

It does **not** create a new list and make `b` point to it.

---

# 5. Mutable vs Immutable

## Immutable

An immutable object cannot be modified after it is created.

Examples in Python:

```text
int
float
str
tuple
bool
```

Example:

```python
x = 10
y = x

x = 20
```

This does not modify the `10` object.

Instead:

```text
Before:

x ─────┐
       ↓
      10
       ↑
y ─────┘


After:

x ─────→ 20

y ─────→ 10
```

---

## Mutable

A mutable object can be modified after creation.

Examples in Python:

```text
list
dict
set
```

Example:

```python
a = [1, 2]
b = a

b.append(3)

print(a)
# [1, 2, 3]
```

The list itself was modified.

```text
a ─────┐
       ↓
   [1, 2, 3]
       ↑
b ─────┘
```

---


# 7. Main Concept to Remember

### Python

```text
Name/reference
      ↓
    Object
```

Reassignment:

```python
x = 10
x = 20
```

means:

```text
x ─────→ 10

        ↓ reassignment

x ─────→ 20
```

The old object is not modified.

---

### Mutable object

```python
a = [1, 2]
b = a

b.append(3)
```

means:

```text
a ─────┐
       ↓
   [1, 2, 3]
       ↑
b ─────┘
```

The same object was modified.

---


# 9. Interview Takeaway

Remember these three points:

1. **Everything in Python is an object.**
2. **Names refer to objects; reassignment changes the reference/binding.**
3. **Mutable objects can be modified, while immutable objects cannot.**

The most important mental model is:

```text
name ─────→ object
```

And when multiple names refer to the same mutable object:

```text
        ┌──────────────┐
a ─────→│              │
        │ mutable obj  │
b ─────→│              │
        └──────────────┘
```

Changing the object through `a` or `b` is visible through both names.
