# =========================
# Dictionary is Iterable
# =========================

D = {"a": 1, "b": 2}

# A dictionary is an iterable object.

# When we iterate directly over a dictionary,
# Python iterates over its keys by default.

for key in D:
    print(key)

# Output:
# a
# b


# =========================
# Dictionary Iterator
# =========================

I = iter(D)

# iter(D) creates a dictionary key iterator.

print(I)

# Output:
# <dict_keyiterator object at 0x...>

print(I.__next__())

# Output:
# a

print(I.__next__())

# Output:
# b

# After all keys are consumed:
# I.__next__()
# StopIteration


# =========================
# Range is Iterable
# =========================

R = range(10)

# range is an iterable object,
# but it is not an iterator.

print(iter(R) is R)

# Output:
# False

# iter(R) creates a separate range_iterator object.


# =========================
# Range Iterator
# =========================

I = iter(R)

print(I)

# Output:
# <range_iterator object at 0x...>


print(next(I))   # 0
print(next(I))   # 1
print(next(I))   # 2
print(next(I))   # 3
print(next(I))   # 4
print(next(I))   # 5
print(next(I))   # 6
print(next(I))   # 7
print(next(I))   # 8
print(next(I))   # 9

# range(10) produces values from 0 to 9.

# After all values are consumed:
# next(I)

# Output:
# StopIteration


# =========================
# Important
# =========================

# Dictionary → Iterable but not an Iterator
# range      → Iterable but not an Iterator
# list       → Iterable but not an Iterator
# tuple      → Iterable but not an Iterator
# string     → Iterable but not an Iterator

# File       → Iterable and Iterator

# Every iterator is iterable,
# but every iterable is not an iterator.