print(type(object))
print(type(int))


class Person:
    pass


print(issubclass(Person, object))
print(issubclass(int, object))

import math

print(type(math))  # <class 'module'>
ty = type(math)
print(type(ty))  # <class 'type'>
# so module is also a class

print(issubclass(ty, object))  # True
import types

print(dir(types))
print(dir(object))
# revison needed for dir
