# List definition:
# A list is an ordered, mutable collection of elements.
# Lists can contain different data types.
# List is mutable: We can change, add, or remove elements after creating the list.


teaVarities = ["Black", "Green", "Oolong"]


# =========================
# Indexing
# =========================

# Positive indexing:
# 0 -> n

# Negative indexing:
# -n -> -1

print(teaVarities[0])    # Black
print(teaVarities[-1])   # Oolong


# =========================
# Slicing
# =========================

# Syntax:
# list[start:end]
# start is included
# end is excluded

print(teaVarities[1:3])
# Output: ['White', 'Oolong']


# =========================
# Giving values through slicing
# =========================

# IMPORTANT:
# When assigning through slicing, the right side must be an iterable.

teaVarities = ["Black", "Green", "Oolong"]

teaVarities[1:2] = ["White"]

print(teaVarities)
# Output: ['Black', 'White', 'Oolong']


# If we assign a string directly:

teaVarities = ["Black", "Green", "Oolong"]

teaVarities[1:2] = "White"

print(teaVarities)
# Output: ['Black', 'W', 'h', 'i', 't', 'e', 'Oolong']

# Why?
# A string is also an iterable.
# Python takes each character separately.


teaVarities = ["Black", "Green", "Oolong"]

teaVarities[1:3] = ["White", "Brown"]

print(teaVarities)
# Output: ['Black', 'White', 'Brown']

teaVarities = ["Black", "Green", "Oolong"]

print(teaVarities[2:2]) 
# empty array

teaVarities[0:0]=["test1","test2"]
print(teaVarities)
# this willl add the value at 0 position without removing an elemnt form prvious list

# insert nothing also call as delete
teaVarities[0:2]=[]
print(teaVarities)


#append  : add in list at end
teaVarities.append("brown")
print(teaVarities)

#pop : delete last  elemnt from list 
teaVarities.pop();
print(teaVarities)

#remove :it delete values give in remove method
teaVarities.remove("Black")
print(teaVarities)

#insert :add in list at iven  positon
teaVarities.insert(0,"Black")
print(teaVarities)


# looping in array
for i in teaVarities:
    print(i,end=" _ ");
    # by default it end with /n

print()

#conditional
if "Oolong" in teaVarities:
    print("i have Oolong tea ");


#new copy memory refernce with difernce refrence
teaVaritiesCpy=teaVarities.copy()