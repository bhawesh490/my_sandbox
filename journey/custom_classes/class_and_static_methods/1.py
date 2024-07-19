class Person:
    def hello(arg="default"):
        print(f"Hello, with arg = {arg} ")


Person.hello()
p = Person()
p.hello()  # hello is a bound method to the instance now.instance is injected as first argument


class MyClass:
    def hello():
        print("hello...")

    def instance_hello(arg):
        print(f"hello from {arg}")

    @classmethod
    def class_hello(arg):
        print(f"hello from {arg}")

    @staticmethod
    def static_hello():
        print(f"hello i am static method")


m = MyClass()
MyClass.hello()
# m.hello()  #will not work
print(MyClass.hello)  # <function MyClass.hello at 0x7f6667df3d90>
print(m.hello)
# <bound method MyClass.hello of <__main__.MyClass object at 0x7faa9869e2c0>>
print(MyClass.instance_hello)  # <function MyClass.instance_hello at 0x7f6667df3e50>
print(m.instance_hello)
m.instance_hello()
# <bound method MyClass.instance_hello of <__main__.MyClass object at 0x7faa9869e2c0>>
print(MyClass.class_hello)  # <bound method MyClass.class_hello
print(m.class_hello)
MyClass.class_hello()
m.class_hello()
# nothing gets injected in the static hello function and it is not bound to any class or method
print(MyClass.static_hello)
MyClass.static_hello()
print(m.static_hello)
m.static_hello()


class Test:
    a = "Bhawesh"

    def __init__(self):
        self.b = Test.a

    @classmethod
    def greet(cls):
        print(f"Hello {cls.a}")


h = Test()
print(h.b)
h.greet()
Test.greet()
