# decorator class
# we will decorate a function using a class not the function


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):  # similar to decorator function
        def inner(*args, **kwargs):
            print(f"Args are {self.a} and {self.b}")
            print("Hello! starting to call the function...")
            result = fn(*args, **kwargs)
            print("Hello! finished calling the function...")
            return result

        return inner


@MyClass(10, 20)
def add(x, y):
    return x + y


print(add(1, 2))
