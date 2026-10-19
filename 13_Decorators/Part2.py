# create  a decorator to print  the function name and the values of its arguments every time the function is called


def outer(func):

    def inner(*args, **kwargs):

        result = func(*args, **kwargs)
        print(f"the name of function is {func.__name__} and  arguments are {args},{kwargs}")
        return result

    return inner


@outer
def getName(name):
    pass

getName("Anuj")