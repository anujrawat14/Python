def add(*args):
    print(*args)
    print(args)
    # it will give a tuple
    result = 0
    for num in args:
        result += num

    return result
    # return sum(args)


print(add(4, 1, 1, 1, 1))
