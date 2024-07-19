class Test:
    pass


print(Test.__dict__)


class Program:
    language = "Python"  # data attribute ,these are class attributes as they are in the name space of the class Class.__dict__

    def say_hello():  # function attribute
        print(f"Hello i am learning {Program.language}")


p = Program()
print(type(p))
print(isinstance(p, Program))
print(
    Program.__dict__
)  # {'__module__': '__main__', 'language': 'Python', 'say_hello': <function Program.say_hello at 0x7f8b1c7b7d30>, '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None}
# that is why language is the class attribute as it belongs to this dictionary
print(p.__dict__)  # empty dictionary
print(p.__class__)
print(type(p) is p.__class__)


class MyClass:
    pass


n = MyClass()
print(type(n), n.__class__)

# type is safer to use becuase we can chage the __class__atrribute value


class MyClass:
    __class__ = str


n = MyClass()
print(type(n), n.__class__)


