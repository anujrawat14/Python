# Decorators: Like a toll booth
# A decorator adds extra functionality to a function
# without changing the original function's code.

import time

# if u want to make a decorator u make a nested function
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"{func.__name__} ran in {end_time - start_time} seconds")

        return result

    return wrapper


# @func_name is used to apply a decorator
@timer
def example_func(n):
    time.sleep(n)


example_func(3)

# The function passes through the timer decorator.
