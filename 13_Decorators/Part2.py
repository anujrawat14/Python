# create  a decorator to print  the function name and the values of its arguments every time the function is called


def outer(func):

    def inner(*args, **kargs):

        result= func(*args, **kargs)
        print(f"the name of function is {func__name__} and  arguments are {*args}")
        return result

    return inner
