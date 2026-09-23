
x = 2
y = 3
z = 3

print(x + (y * z))
# Output: 11

print(40 + 2.335)
# Python automatically converts the integer to float
# Output: 42.335

print(40 + int(2.35))
# int(2.35) -> 2
# Output: 42

print(float(40) + 2.35)
# float(40) -> 40.0
# Output: 42.35


# -------------------------
# Multiple Assignment
# -------------------------

print(x, y, z)
# Output: 2 3 3


# In Python shell:
#
# >>> x = 2
# >>> y = 3
# >>> z = 3
# >>> x, y, z
# (2, 3, 3)
#
# Python can return multiple values as a tuple.


# Multiple expressions in Python shell:
#
# >>> x + 1, y * 2
# (3, 6)


# -------------------------
# Arithmetic Operators
# -------------------------

# Addition
print(x + y)
# Output: 5


# Multiplication
print(y * z)
# Output: 9


# Subtraction
print(y - x)
# Output: 1


# Remainder / Modulus
print(y % 2)
# Output: 1


# Division
print(y / 2)
# Output: 1.5
# / always performs normal division and returns a float.


# Power / Exponentiation
print(x ** y)
# 2 ** 3 -> 8


# -------------------------
# Floating Point
# -------------------------

result = 1 / 3.0

print(result)
# Output: 0.3333333333333333


# -------------------------
# repr() and str()
# -------------------------

repr('chai')
# Returns the representation of the string.
# Output: "'chai'"

str('chai')
# Converts the value into its string form.
# Output: "chai"

print('chai')
# Displays the string:
# chai


# -------------------------
# Bitwise Operation
# -------------------------

# left shift
x=2;
print(x<<2)

#right shift
x=2
print(x>>2)

