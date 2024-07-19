class Person:
    def say_hello():
        print("Hello")


print(Person.say_hello)
Person.say_hello()
p = Person()
print(hex(id(p)))
print(p.say_hello)
# <bound method Person.say_hello of <__main__.Person object at 0x7fd988a43460>>
print(type(p.say_hello))  # <class 'method'>


class Person:
    def say_hello(self):
        print(f"Hello from {self}")


p = Person()
print(hex(id(p)))
p.say_hello()
print(p.say_hello.__func__)
print(p.say_hello.__self__)
