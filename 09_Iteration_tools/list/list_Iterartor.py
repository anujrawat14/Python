myList=[1,2,3,4]

I=iter(myList) #it will map to the memory location where the list i stored

print(I)
# output <list_iterator object at 0x000002B3118805E0>

print(I.__next__()) #1
print(I.__next__()) #2
print(I.__next__()) #3
print(I.__next__()) #4
# print(I.__next__()) #exception