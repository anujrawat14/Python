# =========================
# For Loop
# =========================

# A for loop is used to iterate over a sequence
# such as a list, tuple, string, range, etc.


# =========================
# 1. Loop through a list
# =========================

tea_types = ["Black", "Green", "Oolong"]

for tea in tea_types:
    print(tea)


# =========================
# 2. Loop through a string
# =========================

name = "Anuj"

for char in name:
    print(char)


# =========================
# 3. Using range()
# =========================

# range(start, stop)
# stop value is NOT included

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# =========================
# 4. range(start, stop, step)
# =========================

for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9


# =========================
# 5. Reverse loop
# =========================

for i in range(5, 0, -1):
    print(i)

# Output:
# 5
# 4
# 3
# 2
# 1


# =========================
# 6. for loop with condition
# =========================

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print(num)

# Output:
# 2
# 4


# =========================
# 7. break
# =========================

# break stops the loop completely

for num in range(1, 10):
    if num == 5:
        break

    print(num)

# Output:
# 1
# 2
# 3
# 4


# =========================
# 8. continue
# =========================

# continue skips the current iteration

for num in range(1, 6):
    if num == 3:
        continue

    print(num)

# Output:
# 1
# 2
# 4
# 5