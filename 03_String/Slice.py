# ========================================== 
# Python Strings - Indexing & Slicing 
# ==========================================

# Slicing  Syntax :-
# string[start:stop:step] # # start -> included # stop -> excluded step->jump/hop

chai = "lemon  chai"
print(chai)

chai = "red tea"
print(chai)

# this will give char at first index
firstChar = chai[0]

print(firstChar)


#this will make a copy
sliceChai = chai[:]
print(sliceChai)
#

#start with o ends at 5
sliceChai = chai[0:5]
print(sliceChai)
#

numList = "0123456789"

print(numList[3:])
#3456789

print(numList[:7])
#0123456

print(numList[2:5:2])
#24

print(numList[:-1])
#012345678

print(numList[-1:])
#9

print(numList[6:0:-2])
#642

print(numList[0:6:-2])
#This gives an empty string because the direction is wrong.

print(numList[-1:0:-1])
# reverse string: 987654321

print(numList[:0])
#Stop before index 0. Therefore, nothing is selected