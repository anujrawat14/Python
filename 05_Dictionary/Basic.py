# dictionary definition

# syntax
# 1 :- using dict keyword
chai_types = dict()
# 2 :- using curly braces {key: value}
chai_types = {"Masala": "spicy", "Ginger": "zesty", "Green": "Mild"}

print(chai_types)

# accessing each value using key
print(chai_types["Ginger"])

# add items in dictornary
chai_types["Early Grey"] = "citrus"
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
            "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
              "tea": {"Green":"Mild","Black":"Strong"}
            }


print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])
print(tea_shop["tea"])
print(tea_shop["tea"]["Black"])

#Dictionary compression comprehension

squared_nums={key:key**2 for key in range(5)}
print(squared_nums)
print(squared_nums[3])


# create dictionary using keys list and default values 
keys=["Masala","Ginger","Lemon"]
default_value="Delicious"
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)