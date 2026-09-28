# dictionary definition

# syntax
# 1 :- using dict keyword
chai_types = dict()
# 2 :- using curly braces {key: value}
chai_types = {"Masala": "spicy", "Ginger": "zesty", "Green": "Mild"}

print(chai_types)

# accessing each value using key
print(chai_types["Ginger"])

# Methods
# 1 get()
print(chai_types.get("ginger"))
# return null if value is  not matched

chai_types["Green"] = "fresh"

# 2:

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
