class Person:
    """This string can be used to document this
    class called a doc string"""


p1 = Person()
print(p1)  # <__main__.Person object at 0x7f8b1c1b5b50>
print(Person.__doc__)  # dunder method to access doc string
print(Person.__name__)  # dunder method to access class name

# Instance also has some propety that python puts for us
print(p1.__class__)  # <class '__main__.Person'>
# instead of using above dunder class for p1 we can use
print(type(p1))
print(type(p1) is Person)
print(type([1, 2, 3]) is list)

a = 1
isinstance(a, int)  # True
type(a) is int  # True

# we can use is instance or type but when we deal with inheritance we should use isinstance

# we can set arguments from object also
p1.name = "John"
print(p1.name)

# but it does not mean that we can set from inbuilt objects
a = 10
# a.name = 'John' # AttributeError: 'int' object has no attribute 'name'
# but we can set this on a function object


def hello():
    pass


print(type(hello))
hello.name = "John"
print(hello.name)

# we can delete the attribute from object
del p1.name

# dict dunder method stores attributes of object in a dictionary
print(p1.__dict__)
p1.name = "John"
print(p1.__dict__)

p2 = Person()
print(p2.__dict__)
p2.name = "Jane"
print(p2.__dict__)
p2.first_name = "Bhawesh"
p2.last_name = "Mehta"
print(p2.__dict__)  # {'name': 'Jane', 'first_name': 'Bhawesh', 'last_name': 'Mehta'}


print(type([1, 2, 3]))


class Person:
    pass


print(type(Person))  # <class 'type'>
# any class we create it is going to be of type class
print(type(type))

print(Person.__name__)
p = Person()
print(p)
print(p.__class__)  # we can use type(p) also
print(type(p))
# other method we can use is instance
print(isinstance(p, Person))
