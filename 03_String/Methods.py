# ==========================================
# Python Strings - Methods & Operations
# ==========================================


name = "Anuj Rawat"


# ==========================================
# 1. lower()
# ==========================================

print(name.lower())  # anuj rawat

# islower() checks whether all alphabetic
# characters are lowercase.
print(name.islower())  # False


# ==========================================
# 2. upper()
# ==========================================

print(name.upper())  # ANUJ RAWAT

# isupper() checks whether all alphabetic
# characters are uppercase.
print(name.isupper())  # False


# ==========================================
# 3. strip()
# ==========================================

newString = "    Anuj     Rawat    "

print(newString.strip())

# strip() removes whitespace from the
# beginning and end of a string.
#
# It does NOT remove spaces between words.
#
# Output:
# Anuj     Rawat


# ==========================================
# 4. replace()
# ==========================================

print(newString.replace("Anuj", "Anuj Kumar"))

# replace(old, new)
#
# Replaces occurrences of old text with new text.
#
# Output:
#     Anuj Kumar     Rawat


# ==========================================
# 5. split()
# ==========================================

newStrings = "ram, shyam, mohan, sohan"

print(newStrings.split(","))

# split() breaks a string into a list.
#
# Output:
# ['ram', ' shyam', ' mohan', ' sohan']


# We can remove the extra spaces using strip()
# or use split(", ") when the format is consistent.

print(newStrings.split(", "))

# Output:
# ['ram', 'shyam', 'mohan', 'sohan']


# ==========================================
# 6. find()
# ==========================================

newString = "masala chai"

print(newString.find("chai"))  # 7

print(newString.find("z"))  # -1

# find() returns the index of the first
# occurrence of the substring.
#
# If it is not found, it returns -1.


# ==========================================
# 7. count()
# ==========================================

newString = "hi hi hello hi"

print(newString.count("hi"))  # 3

# count() returns the number of occurrences
# of a substring.


# ==========================================
# 8. String Formatting
# ==========================================

chaiType = "Masala"
quantity = 2

order = "I ordered {} cups of {} chai"

print(order.format(quantity, chaiType))

# {} are placeholders.
#
# format() inserts values into those placeholders.
#
# Output:
# I ordered 2 cups of Masala chai


# ==========================================
# 9. join(): joins elements of an iterable using the given separator.
# ==========================================

chai = ["lemon", "masala", "ginger"]

print(" ".join(chai))

# Output: lemon masala ginger

print(", ".join(chai))

# Output:lemon, masala, ginger


# ==========================================
# 10. len(): returns the number of characters ,Spaces are also counted.
# ==========================================

chai = "lemon chai"

print(len(chai))  # 10

# ==========================================
# 11. Iterating Through a String :A string is iterable.The loop visits each character one by one
# ==========================================

for letter in chai:
    print(letter)

# ==========================================
# 12. Quotes Inside a String
# ==========================================

string = 'he said "how are you? " '

print(string)

# \" allows us to use double quotes inside a double-quoted string.

# Another option: use single quotes outside.

string = 'he said "how are you?"'

print(string)


# ==========================================
# 13. New Line - \n
# ==========================================

string = "he said \nhow are you?"

print(string)

# ==========================================
# 14. Raw String - r""  # Raw strings treat backslashes mostly as normal characters.

# ==========================================

string = r"he said \n how are you?"

print(string)

# Therefore \n is printed instead of
# creating a new line.


# ==========================================
# 15. Backslash - \\  represents one literal backslash.
# ==========================================

print("C:\\user\\pwd")

# Output: C:\user\pwd


# ==========================================
# 16. in Operator checks whether a substring exists inside another string
# ==========================================

print("chai" in "masala chai")  # True

print("coffee" in "masala chai")  # False


# ==========================================
# 17. not in Operator
# ==========================================

print("coffee" not in "masala chai")  # True
