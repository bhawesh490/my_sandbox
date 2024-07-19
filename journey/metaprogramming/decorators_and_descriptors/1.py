# https://www.geeksforgeeks.org/args-kwargs-pytho
from functools import wraps


# Decorator Example
def debugger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print(f"Function {fn.__name__} called with args {args} and kwargs {kwargs}")
        print(f"Function Quanlname {fn.__qualname__}")
        return fn(*args, **kwargs)

    return inner


@debugger
def add(a, b):
    return a + b


@debugger
def sub(a, b):
    return a - b


print(add(1, 2))


# descriptor example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
print(p.x)
print(p.y)
# redo descriptors
