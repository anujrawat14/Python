# continue — Skip the current iteration

# The continue statement skips the remaining code in the current iteration and moves to the next iteration of the loop.

# continue: Skips even numbers

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

# Output:
# 1
# 2
# 4
# 5
