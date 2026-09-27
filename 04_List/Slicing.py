
# =========================
# Slicing
# =========================

# Syntax:
# list[start:end]
# start is included
# end is excluded

teaVarities = ["Black", "Green", "Oolong"]

print(teaVarities[1:3])
# Output: ['White', 'Oolong']


# =========================
# Giving values through slicing
# =========================

# IMPORTANT:
# When assigning through slicing, the right side must be an iterable.

teaVarities = ["Black", "Green", "Oolong"]

teaVarities[1:2] = ["White"]

print(teaVarities)
# Output: ['Black', 'White', 'Oolong']


# If we assign a string directly:

teaVarities = ["Black", "Green", "Oolong"]

teaVarities[1:2] = "White"

print(teaVarities)
# Output: ['Black', 'W', 'h', 'i', 't', 'e', 'Oolong']

# Why?
# A string is also an iterable.
# Python takes each character separately.


teaVarities = ["Black", "Green", "Oolong"]

teaVarities[1:3] = ["White", "Brown"]

print(teaVarities)
# Output: ['Black', 'White', 'Brown']

teaVarities = ["Black", "Green", "Oolong"]

print(teaVarities[2:2])
# empty array

teaVarities[0:0] = ["test1", "test2"]
print(teaVarities)
# this willl add the value at 0 position without removing an elemnt form prvious list

# insert nothing also call as delete
teaVarities[0:2] = []
print(teaVarities)
