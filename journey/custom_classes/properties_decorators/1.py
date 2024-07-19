# Concept of decorators
def my_decorator(fn):
    print("Decorating my function...")
    return fn


def add(a, b):
    return a + b


# print(add(1, 2))
add = my_decorator(add)
print(add(1, 2))


# same thing can be written as
@my_decorator
def sub(a, b):
    return a - b


print(sub(2, 2))


# Example 2
def my_decorator(fn):
    print("Decorating my function...")

    def inner(*args, **kwargs):
        print("Executing my function...", fn)
        return fn(*args, **kwargs)

    return inner


def un_decorated(a, b):
    print("Running original function")
    return a + b


decorate_func = my_decorator(un_decorated)
print(decorate_func)
print(decorate_func(1, 2))

# instead of the above we could name the undecorated function same
un_decorated = my_decorator(un_decorated)


# or we can use @symbol
@my_decorator
def un_decorated(a, b):
    print("Running original function")
    return a + b


@my_decorator
def hello(a, b):
    return a + b


print(hello(1, 2))


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """This is a getter method"""
        return self._name

    @name.setter
    def name(self, values):
        # no doc string required in setter
        self._name = values


p = Person("Alex")
# print(help(Person))

# how to create a class which has only setters and not getters


# approach 1
class Person:
    def prop_set(self, value):
        print("setter called")

    prop = property(fset=prop_set)


p = Person()
p.prop = 100


# approach 2
class Person:
    prop = property(doc="This is a write only property")

    @prop.setter
    def prop(self, value):
        print("setter called")


# doc string only picks up from getter not setter
