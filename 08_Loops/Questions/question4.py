string = input("enter a string : ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print(reversed_string)

# for i in range(len(string) - 1, -1, -1):
#     print(string[i], end="")
