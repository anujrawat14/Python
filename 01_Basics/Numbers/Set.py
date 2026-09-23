# -------------------------
# Sets
# -------------------------

# A set is an unordered collection of unique elements.

set_one = {1, 2, 3, 4}
set_two = {1, 3, 5}


# -------------------------
# Intersection
# -------------------------

# & returns elements that are present
# in BOTH sets.

print(set_one & set_two)
# Output: {1, 3}


# -------------------------
# Union
# -------------------------

# | combines elements from both sets.
# Duplicate elements are automatically removed.

print(set_one | set_two)
# Output: {1, 2, 3, 4, 5}


# -------------------------
# Difference
# -------------------------

# - returns elements that are in the first set
# but NOT in the second set.

print(set_one - set_two)
# Output: {2, 4}


# or

set_one = {1, 2, 3, 4}
set_two = {1, 3, 5}


# Elements only in set_one
print(set_one.difference(set_two))
# {2, 4}


# Elements only in set_two
print(set_two.difference(set_one))
# {5}


# Common elements
print(set_one.intersection(set_two))
# {1, 3}


# All unique elements
print(set_one.union(set_two))
# {1, 2, 3, 4, 5}


# Check membership
print(2 in set_one)
# True


# Add an element
set_one.add(6)
print(set_one)


# Remove an element
set_one.remove(6)
print(set_one)

#  empty_set=set() as {} it is an dictionary

print({1,2}-{1,2})
# it will give set()
