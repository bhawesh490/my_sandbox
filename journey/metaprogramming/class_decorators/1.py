def savings(cls):
    cls.account_type = "Savings"
    return cls


def checking(cls):
    cls.account_type = "Checking"
    return cls


class Account:
    pass


@savings
class Bank1Savings(Account):
    pass


@savings
class Bank2Savings(Account):
    pass


@checking
class Bank1Checking(Account):
    pass


@checking
class Bank2Checking(Account):
    pass


print(Bank2Checking.__dict__)


# lets use parameterised decorator
# decorator factory
def account_type(type_):
    def decorator(cls):
        cls.account_type = type_
        return cls

    return decorator


@account_type("Savings")
class Bank1Savings(Account):
    pass


@account_type("Checking")
class bank1Checking(Account):
    pass


print(Bank1Savings.__dict__)

# adding methods in the function using decorators


def hello(cls):
    def hello(self):
        return f"{self} says hello"

    cls.hello = hello
    return cls


@hello
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


print(vars(Person))
p = Person("John")
print(p.hello())


# Example 2

from functools import wraps
from typing import Any


def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"Log: {fn.__qualname__}({args}, {kwargs}) = {result}")
        return result

    return inner


class Person:
    @func_logger
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @func_logger
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"


print("Example2")
p = Person("John", 78)
p.greet()

# example 3
# we have to repeat the fun_logger decorator for each callable in the class
# instead we want to implement a class decorator that can automatically
# be applied to all the callables in the class


def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print("decorating...", cls, name)
            setattr(cls, name, func_logger(obj))
    return cls


@class_logger
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"


print("Example3")
print(vars(Person))
p = Person("John", 78)


# example4
# class decorator are decorating instance methods not the class and static methods
print("Example4 decorating with class decorator")


@class_logger
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def static_method(default=1):
        print(f"Static method called by {default}")

    @classmethod
    def class_method(cls):
        print(f"Class method called for {cls}")

    def instance_method(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"


p = Person("John", 78)
# print(p.instance_method())
print(p.static_method())
# print(p.class_method())
# print(Person.__dict__)
# print(Person.__dict__["static_method"])
# print(callable(Person.__dict__["static_method"]))


# debugging static method

print("Example6")


class Person:
    @staticmethod
    @func_logger
    def static_method():
        return "Static method called"


Person.static_method()


class Person:
    @func_logger
    @staticmethod
    def static_method():
        return "Static method called"


Person.static_method()
