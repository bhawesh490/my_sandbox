class Person:
    pass


a = Person()
print(a.__class__)
print(a.__class__.__name__)
print(type(a).__name__)


class Person:
    pass


p = Person()
print(str(p))  # <__main__.Person object at 0x7f18ed033430>


class Person:
    def __str__(self):
        return "Person Class"


p = Person()
print(str(p))
print(p)


class Person:
    def __repr__(self):
        return "Person Class with extra debugging"


p = Person()
print(str(p))

#########################################################################################

# from abc import ABC, abstractmethod

# class AbstractClassExample(ABC):
#     @abstractmethod
#     def do_something(self):
#         pass

# class AnotherSubclass(AbstractClassExample):
#     def do_something(self):
#         super().do_something()
#         print("The subclass is doing something")


class Shape:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Shape.info called from shape({self.name})"

    def extended_info(self):
        return f"Shape.extended_info called from shape({self.name})"


class Polygon(Shape):
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Polygon info called from Polygon({self.name})"


p = Polygon("square")
print(p.info())
print(p.extended_info())


class Shape:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Shape.info called from shape({self.name})"

    def extended_info(self):
        return f"Shape.extended_info called from shape({self.name},{self.info()})"


class Polygon(Shape):
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Polygon info called from Polygon({self.name})"


p = Polygon("square")
print(p.info())
print(p.extended_info())


class Person:
    def __str__(self):
        return "Person class"


class Student(Person):
    def __repr__(self):
        return "Student class"


s = Student()
print(str(s))  # Person class
print(repr(s))  # Student class


class Person:
    def __str__(self):
        print("__str__ called in Person Class")
        return self.__repr__()

    def __repr__(self):
        return "Person class"


class Student(Person):
    def __repr__(self):
        return "Student class"


s = Student()
p = Person()
print(str(s))  # Student class
print(repr(s))  # Student class
print(str(p))  # Person class
