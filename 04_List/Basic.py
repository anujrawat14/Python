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

squared_num=[x**2 for x in range(10)]
print(squared_num)