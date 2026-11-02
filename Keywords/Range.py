# range() — Generate a sequence of integers

# range() is a built-in function that represents an immutable sequence of integers. It is commonly used in loops without creating a list of all the numbers in advance.

# Example 1: range(stop)

for i in range(5):
    print(i)

# Output: 0 1 2 3 4


# Example 2: range(start, stop)

for i in range(2, 6):
    print(i)

# Output: 2 3 4 5


# Example 3: range(start, stop, step)

for i in range(2, 11, 2):
    print(i)

# Output: 2 4 6 8 10


# Example 4: Reverse counting

for i in range(5, 0, -1):
    print(i)

# Output: 5 4 3 2 1