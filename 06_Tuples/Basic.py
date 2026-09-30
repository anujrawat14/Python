# Tuple is immutable, while a list is mutable.

tea_types = ("Black", "Green", "Oolong")

# indexing
print(tea_types[0])     # Black
print(tea_types[-1])    # Oolong


#slicing

print(tea_types[1:])    # ('Green', 'Oolong')

#Immutable

# We cannot change an existing element of a tuple.

tea_types[0] = "Masala"

# TypeError: 'tuple' object does not support item assignments



