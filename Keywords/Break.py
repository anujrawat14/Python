# break — Terminate the loop

# The break statement immediately terminates the nearest enclosing loop, even if the loop condition is still True.


# break: Stops the loop immediately

for i in range(1, 6):
    if i == 3:
        break

    print(i)

# Output:
# 1
# 2
