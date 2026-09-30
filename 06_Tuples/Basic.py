# =========================
# Tuple
# =========================

# A tuple is immutable, while a list is mutable.
tea_types = ("Black", "Green", "Oolong")


# =========================
# Indexing
# =========================

print(tea_types[0])      # Black
print(tea_types[-1])     # Oolong


# =========================
# Slicing
# =========================

print(tea_types[1:])     # ('Green', 'Oolong')


# =========================
# Immutable
# =========================

# We cannot change an existing element of a tuple.

# tea_types[0] = "Masala"

# TypeError:
# 'tuple' object does not support item assignment


# =========================
# Concatenation
# =========================

more_tea = ("Herbal", "Early Grey")

all_tea = tea_types + more_tea

print(all_tea)
# ('Black', 'Green', 'Oolong', 'Herbal', 'Early Grey')


# =========================
# Membership
# =========================

if "Herbal" in all_tea:
    print(True)


# =========================
# count()
# =========================

print(more_tea.count("Herbal"))
# 1


# =========================
# Tuple Unpacking
# =========================

(black, green, oolong) = tea_types

print(black)      # Black
print(green)      # Green
print(oolong)     # Oolong


# =========================
# List Unpacking
# =========================

li = ["One", "Two"]

[one, two] = li

print(one)        # One
print(two)        # Two