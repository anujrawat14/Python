teaVarities = ["Black", "Green", "Oolong"]

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
