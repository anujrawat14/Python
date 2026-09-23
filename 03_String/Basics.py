
# A string is a sequence of characters.
# Strings can be written using:
# 1. Single quotes ''
# 2. Double quotes ""
# 3. Triple quotes ''' ''' or """ """


# -------------------------
# 1. Creating a String
# -------------------------

name = "Anuj"
message = 'Hello Python'

print(name)
print(message)


# -------------------------
# 2. String with Numbers
# -------------------------

# Numbers inside quotes are treated as strings.

age = "21"

print(age)
print(type(age))  # <class 'str'>


# -------------------------
# 3. Empty String
# -------------------------

empty_string = ""

print(empty_string)
print(type(empty_string))  # <class 'str'>


# -------------------------
# 4. Single vs Double Quotes
# -------------------------

name1 = 'Anuj'
name2 = "Anuj"

print(name1)
print(name2)

# Both create the same type: str


# -------------------------
# 5. String containing Quotes
# -------------------------

# Double quotes can contain single quotes
text1 = "It's Python"

# Single quotes can contain double quotes
text2 = 'He said "Hello"'

print(text1)
print(text2)


# -------------------------
# 6. Multi-line String
# -------------------------

# Triple quotes are used for multi-line strings.

paragraph = """Python is easy to learn.
Python is widely used.
Python is useful for backend development."""

print(paragraph)


# -------------------------
# 7. Strings are Sequences
# -------------------------

# A string is a sequence of characters.
# Each character has a position (index).

word = "Python"

print(word)

# Index:
# P  y  t  h  o  n
# 0  1  2  3  4  5


# -------------------------
# 8. Length of String
# -------------------------

word = "Python"

print(len(word))  # 6


# -------------------------
# 9. String Concatenation
# -------------------------

first_name = "Anuj"
last_name = "Rawat"

full_name = first_name + " " + last_name

print(full_name)


# -------------------------
# 10. String Repetition
# -------------------------

word = "Hi "

print(word * 3)

# Output:
# Hi Hi Hi


# -------------------------
# 11. String with Different Data Types
# -------------------------

age = 21

# This will NOT work:
# print("Age: " + age)

# Convert number to string first.

print("Age: " + str(age))


# -------------------------
# 12. Check String Type
# -------------------------

name = "Anuj"

print(type(name))  # <class 'str'>


# -------------------------
# 13. Membership
# -------------------------

# 'in' checks whether something exists inside a string.

word = "Python"

print("P" in word)       # True
print("Py" in word)     # True
print("Java" in word)   # False

print("P" not in word)  # False


# =========================
# Important Points
# =========================

# 1. String type is: str
# 2. Strings are sequences of characters.
# 3. Strings support indexing and slicing.
# 4. Strings are immutable.
# 5. len() gives the number of characters.
# 6. + joins strings (concatenation).
# 7. * repeats a string.
# 8. 'in' checks membership.
# 9. str() converts a value into a string.
