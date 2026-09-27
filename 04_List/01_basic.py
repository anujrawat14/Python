# List definition:
# A list is an ordered, mutable collection of elements.
# Lists can contain different data types.
# List is mutable: We can change, add, or remove elements after creating the list.


teaVarities = ["Black", "Green", "Oolong"]


# =========================
# Indexing
# =========================

# Positive indexing:
# 0 -> n

# Negative indexing:
# -n -> -1

print(teaVarities[0])  # Black
print(teaVarities[-1])  # Oolong


# =========================
# Slicing
# =========================

# Syntax:
# list[start:end]
# start is included
# end is excluded

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


# =========================
# append()
# =========================

# append() adds an element at the end of the list.

teaVarities.append("Brown")

print(teaVarities)


# =========================
# pop()
# =========================

# pop() removes and returns the last element.

teaVarities.pop()

print(teaVarities)


# pop(index)
# We can also remove an element using its index.

teaVarities.pop(0)


# =========================
# remove()
# =========================

# remove(value) removes the first occurrence
# of the given value.

teaVarities.remove("Green")

print(teaVarities)


# =========================
# insert()
# =========================

# insert(index, value)
# Adds an element at the given position.

teaVarities.insert(0, "Black")

print(teaVarities)


# =========================
# Looping through a List
# =========================

for i in teaVarities:
    print(i, end=" _ ")

# print() normally ends with '\n'
# end=" _ " changes the ending.

print()


# =========================
# Conditional with List
# =========================

if "Oolong" in teaVarities:
    print("I have Oolong tea")



# =========================
# Copying a List
# =========================


teaVaritiesCopyRef=teaVarities
#Both variables refer to the SAME list and This does NOT create a new list..

teaVaritiesCopyRef.append("Green")
print(teaVaritiesCopyRef)
print(teaVarities)
# Both List will be updated

# new copy memory refernce with difernce refrence
teaVaritiesCpy = teaVarities.copy()
teaVaritiesCpy.append("Lemon")
print(teaVarities)
print(teaVaritiesCpy)

#list comprehension