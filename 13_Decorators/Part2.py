# create  a decorator to print  the function name and the values of its arguments every time the function is called


def outer(func):

    def wrapper(*args, **kwargs):

        args_value = ", ".join(str(arg) for arg in args)
        # compresion/loops in args
        kwargs_value = ", ".join(f"{key}={val}" for key, val in kwargs.items())
        # compresion/loops in Kwargs

        result = func(*args, **kwargs)
        print(
            f"calling : {func.__name__} with args : {args_value} and kwargs : {kwargs_value}"
        )
        return result

    return wrapper


@outer
def greet(name, greting="Hello"):
    print(f"{greting} {name}")

    greet("Anuj", greting="hanji")
