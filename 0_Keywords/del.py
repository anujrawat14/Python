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