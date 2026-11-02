# break — Terminate the Loop

# The break statement immediately terminates the nearest enclosing loop,
# even if the loop condition is still True.

# break: Stops the loop immediately.
# Execution continues with the first statement after the loop.


# --------------------------------------------------
# Example 1: Basic break
# --------------------------------------------------

for i in range(1, 6):
    if i == 3:
        break

    print(i)

# Output:
# 1
# 2


# --------------------------------------------------
# Example 2: Break after finding an element
# --------------------------------------------------

nums = [10, 20, 30, 40, 50]
target = 30

for num in nums:
    if num == target:
        print("Found:", num)
        break

# Output:
# Found: 30


# --------------------------------------------------
# Example 3: break in a while loop
# --------------------------------------------------

count = 1

while count <= 10:
    if count == 4:
        break

    print(count)
    count += 1

# Output:
# 1
# 2
# 3


# --------------------------------------------------
# Example 4: Infinite loop with break
# --------------------------------------------------

# while True creates an infinite loop.
# break is used to exit it when required.

while True:
    user_input = input("Enter something (or 'exit'): ")

    if user_input == "exit":
        break

    print("You entered:", user_input)


# --------------------------------------------------
# Example 5: break in nested loops
# --------------------------------------------------

# break terminates only the nearest enclosing loop.

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break

        print(i, j)

# Output:
# 1 1
# 2 1
# 3 1


# --------------------------------------------------
# Important:
# --------------------------------------------------

# 1. break exits the loop immediately.
# 2. It does not terminate the entire program.
# 3. In nested loops, it exits only the inner loop.
# 4. break cannot be used outside a loop.
# 5. break exits the loop, whereas continue skips
#    the current iteration and proceeds to the next one.