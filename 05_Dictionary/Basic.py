# A dictionary is an ordered, mutable collection of key-value pairs.

# Syntax:
# {key: value}

# Creating a Dictionary

# 1. Using dict() keyword/function

chai_types = dict()
print(chai_types)

# 2 :- using curly braces {key: value}
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types)


# Access a value using its key
print(chai_types["Ginger"])
# Zesty


# Using get()
print(chai_types.get("Ginger"))
# Zesty

# get() is safer because it returns None if the key does not exist instead of raising KeyError.

print(chai_types.get("Black"))
# None

# Add a new key-value pair
chai_types["Earl Grey"] = "Citrus"
print(chai_types)

# If the key already exists, its value is updated

chai_types["Green"] = "Light"
print(chai_types)



# looping in dictionary

for chai in chai_types:
    print("type is ", chai, " with ", chai_types[chai], " flavour ")
# print("type is ", chai, " with ",chai_types.get(chai) ," flavour ")

print()
# important u cant loop directly to dictionry u need to convert to items

for key, value in chai_types.items():
    print("type is ", key, " with ", value, " flavour ")
# print("type is ", chai, " with ",chai_types.get(chai) ," flavour ")


# membership in
if "Masala" in chai_types:
    print(True)


# copy of the dictionary

chai_types_copy = chai_types.copy()
print(chai_types_copy)

# nested dictionary

tea_shop = {
    "chai": {
        "Masala": "Spicy",
        "Ginger": "Zesty"
    },

    "tea": {
        "Green": "Mild",
        "Black": "Strong"
    }
}


# Access nested dictionary

print(tea_shop["chai"])
# {'Masala': 'Spicy', 'Ginger': 'Zesty'}


print(tea_shop["chai"]["Ginger"])
# Zesty


print(tea_shop["tea"])
# {'Green': 'Mild', 'Black': 'Strong'}


print(tea_shop["tea"]["Black"])
# Strong


# Dictionary compression comprehension

squared_nums = {key: key**2 for key in range(5)}
print(squared_nums)
print(squared_nums[3])


#  Creating Dictionary Using fromkeys()

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
