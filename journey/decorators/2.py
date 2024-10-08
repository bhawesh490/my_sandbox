from functools import wraps
import inspect

# wraps is a decorator that copies the metadata of the passed function to the inner function


def counter(func):
    count = 0

    @wraps(func)
    def inner(*args, **kargs):
        nonlocal count
        count += 1
        print(count)
        return func(*args, **kargs)

    return inner


def add(x, y):
    return x + y


add = counter(add)
add(1, 2)


#################other way################################
@counter
def adds(x, y):
    return x + y


adds(1, 2)
print(adds.__name__)
print(inspect.signature(adds))
