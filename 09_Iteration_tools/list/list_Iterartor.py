myList = [1, 2, 3, 4]

I = iter(myList)
# Creates a list_iterator object.
# It keeps track of where we currently are in the list.

print(I)
# <list_iterator object at 0x000002B3118805E0>

print(I.__next__())   # 1
print(I.__next__())   # 2
print(I.__next__())   # 3
print(I.__next__())   # 4

# print(I.__next__()) # StopIteration exception

#important in list
myNewList=[1,2,3,4]
print(iter(myNewList) is myNewList)
# A list is iterable, but it is not an iterator. A file object is both iterable and an iterator.