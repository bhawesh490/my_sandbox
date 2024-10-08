# Decorating class
# here we will decorate the class as opposed to the function
from datetime import datetime, timezone


def info(self):  # think of this as a instance method
    results = []
    results.append(f"time: {datetime.now(timezone.utc)}")
    results.append(f"Class: {self.__class__.__name__}")
    results.append(f"Id: {hex(id(self))}")
    for k, v in vars(self).items():
        results.append(f"{k}: {v}")
    return results


def debug_info(cls):
    cls.debug = info
    return cls


@debug_info
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        return "Hello there!"


p = Person("John", 78)
print(p.debug())
