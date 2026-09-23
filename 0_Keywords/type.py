# -------------------------
# type() - Python Keyword / Built-in
# -------------------------

# type() is used to check the type (class)
# of an object/value.

x = 10
name = "Anuj"
price = 99.5
is_active = True

print(type(x))
# <class 'int'>

print(type(name))
# <class 'str'>

print(type(price))
# <class 'float'>

print(type(is_active))
# <class 'bool'>


# -------------------------
# Checking Different Types
# -------------------------

print(type(10))
# <class 'int'>

print(type(10.5))
# <class 'float'>

print(type(2 + 3j))
# <class 'complex'>

print(type([1, 2, 3]))
# <class 'list'>

print(type((1, 2, 3)))
# <class 'tuple'>

print(type({1, 2, 3}))
# <class 'set'>

print(type({"name": "Anuj"}))
# <class 'dict'>


# -------------------------
# type() vs Type Conversion
# -------------------------

# type() only checks the type.
x = 10

print(type(x))
# <class 'int'


# int(), float(), str(), etc. can be used
# to convert a value into another type.

x = "10"

print(type(x))
# <class 'str'>

x = int(x)

print(type(x))
# <class 'int'>
print(x)
# 10


# -------------------------
# Comparing Types
# -------------------------

x = 10

print(type(x) == int)
# True

print(type(x) == str)
# False