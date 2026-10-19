# Implement a decorator that caches the return values of a function,
# so that when it's called with the same arguments, the cached value
# is returned instead of re-executing the function.

import time


def cache(func):

    cached_value = {}
    print("start cache value", cached_value)

    def wrapper(*args, **kwargs):

        if args in cached_value:
            result = cached_value[args]  # Cache hit
        else:
            result = func(*args, **kwargs)  # Execute function
            cached_value[args] = result  # Store result

        print(" current cache:", cached_value)
        return result

    return wrapper


@cache
def long(a, b):
    time.sleep(4)
    return a + b


print(long(4, 5))  # Executes function: waits 4 seconds
print(long(2, 5))  # Executes function: waits 4 seconds
print(long(4, 5))  # Uses cached value: almost instant
