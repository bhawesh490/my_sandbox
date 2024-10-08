from functools import wraps


def greet(func):
    @wraps(func)
    def inner(*args, **kargs):
        print("Hello! starting to call the function...")
        result = func(*args, **kargs)
        print("Hello! finished calling the function...")
        return result

    return inner


@greet
def add(x, y):
    return x + y


# print(add(1, 2))

#################################################################################################################


def outer(reps):  # decorator factory as it is returing a decorator function
    def greetings(func):  # decorator function
        @wraps(func)
        def inner(*args, **kargs):
            print(f"Hello!{reps} starting to call the function...")
            result = func(*args, **kargs)
            print(f"Hello!{reps} finished calling the function...")
            return result

        return inner

    return greetings


# you can remane the outer function to greet as it is more meaningful
@outer("bhawesh")
def adds(x, y):
    return x + y


print(adds(1, 2))
