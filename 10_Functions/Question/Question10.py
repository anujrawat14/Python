def fact(num):
    # stopping condition
    if num == 1 or num == 0:
        return 1

    return num * fact(num - 2)

print(fact(5))



# fact(5)
#   → 5 * fact(4)
#   → 5 * 4 * fact(3)
#   → 5 * 4 * 3 * fact(2)
#   → 5 * 4 * 3 * 2 * fact(1)
#   → 5 * 4 * 3 * 2 * 1
#   → 120
