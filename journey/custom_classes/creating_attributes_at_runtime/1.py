class MyClass:
    language = "English"


p = MyClass()
print(p.__dict__)
print(p.language)  # fetching from class attribute
p.hello_world = lambda: "Hi hello world"
print(p.__dict__)
print(p.hello_world())


class MyClass:
    language = "English"


from types import MethodType

p = MyClass()
p.hello_world = MethodType(
    lambda self: f"Hi hello world from {self} and my language is {self.language}", p
)
print(p.hello_world())


class MyClass:
    def __init__(self, name):
        self.name = name


p1 = MyClass("Alex")
p2 = MyClass("Eric")


def say_hello(self):
    return f"{self.name} says hello!"


p1_say_hello = MethodType(say_hello, p1)
print(p1_say_hello)
p1.say_hello = p1_say_hello
print(p1.say_hello())
print(p1.__dict__)


from types import MethodType


class Person:
    def __init__(self, name):
        self.name = name

    def register_do_work(self, func):
        setattr(self, "_do_work", MethodType(func, self))

    def do_work(self):
        do_work_method = getattr(self, "_do_work", None)
        if do_work_method:
            return do_work_method()
        else:
            # return f"{self.name} is not working"
            raise AttributeError("You must register a do_work method")


math_teacher = Person("John")
english_teacher = Person("Jane")
# math_teacher.do_work()


def work_math(self):
    return f"{self.name} is teaching math"


math_teacher.register_do_work(work_math)
print(math_teacher.__dict__)
print(math_teacher.do_work())


def work_english(self):
    return f"{self.name} is teaching English"


english_teacher.register_do_work(work_english)
print(english_teacher.do_work())
