# create  a decorator to print  the function name and the values of its arguments every time the function is called


def outer(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        print(
            f"the name of function is {func.__name__} and  arguments are {args},{kwargs}"
        )
        return result

    return wrapper


@outer
def greet(name, greting="Hello"):
    print(f"{greting} {name}")


greet("Anuj", greting="hanji")
