# Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function
import time


def cache(func):

    cached_value = {}
    print(cached_value)

    def wrapper(*args, **kwargs):

        if args in cached_value:
            return cached_value[args]
        else:
            cached_value[args] = result
            result = func(*args, **kwargs)

        return result

    return wrapper


def long(a, b):
    time.sleep(4)
    return a + b


long(4, 5)
