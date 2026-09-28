chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

# Methods

#1. get() is used to access a value using its key.

print(chai_types.get("Ginger"))
# Output: Zesty

# If the key is not found, get() returns None.

print(chai_types.get("ginger"))
#  Output: None

# We can also provide a default value

print(chai_types.get("Black", "Key not found"))
# Output: Key not found


# 2: # len() returns the number of key-value pairs in the dictionary.

length = len(chai_types)
print(length)

# pop() removes an item based on its key and returns the removed value.

removed_value = chai_types.pop("Earl Grey")
print(removed_value)
print(chai_types)

# popitem() removes and returns the LAST inserted key-value pair.

removed_item = chai_types.popitem()

print(removed_item)
print(chai_types)

# clear() removes ALL items from the dictionary.

chai_types.clear()
print(chai_types)

# Output: {}