from time import perf_counter
from functools import wraps


def timed(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print(f"{fn.__name__} ran in {elapsed:.6f}s")
        return result

    return inner


# @timed
# def hello():
#     print("Hello, World!")


# hello()
