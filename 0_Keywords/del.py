# del is a Python keyword used to delete a variable, list item, dictionary item, or other objects/references.

teaVarities = ["Black", "Green", "Oolong"]

del teaVarities[1]

print(teaVarities)
# ['Black', 'Oolong']

student = {
    "name": "Anuj",
    "age": 21
}

del student["age"]

print(student)
# {'name': 'Anuj'}


# Delete multiple items using slicing

numbers = [10, 20, 30, 40, 50]
del numbers[1:3]

print(numbers)
# Output: [10, 40, 50]