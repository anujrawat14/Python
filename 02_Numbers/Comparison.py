# -------------------------
# Comparison Operators
# -------------------------

# Less than
print(1 < 2)
# True

print(int(1 < 2))
# True -> 1
# bool can be converted to int:
# True = 1
# False = 0


# -------------------------
# Equal to
# -------------------------

print(5.0 == 5.0)
# True


# -------------------------
# Not equal to
# -------------------------

print(5.0 != 5.0)
# False


# -------------------------
# Logical AND
# -------------------------

print(1 < 2 and 2 < 3)
# True
#
# Both conditions must be True.


# -------------------------
# Logical OR
# -------------------------

print(1 < 2 or 2 < 3)
# True
#
# At least one condition must be True.


# -------------------------
# Chained Comparison
# -------------------------

print(1 == 2 < 3)
# False

# Python treats this as:
#
# (1 == 2) and (2 < 3)
#
# False and True
# -> False


# Same logic written explicitly:

print(1 == 2 and 2 < 3)
# False