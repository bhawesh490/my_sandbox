class Person:
    pass


print(Person.__name__)  # 'Person'


class Program:
    language = "Python"
    version = "3.7"


print(Program.__name__)
print(type(Program))
print(Program.language)
print(Program.version)
# lets set the version attribute of the class to some other value
Program.version = "3.8"
print(Program.version)
# use of getattr and setattr
print(getattr(Program, "language"))
print(getattr(Program, "x", "xdoes not exists"))
print(Program.__dict__)
setattr(Program, "x", 100)
print(getattr(Program, "x"))
# checking the dict dunder method
print(Program.__dict__)

z = 1, 2
print(z)
a, b = 1, 2
print(a)
print(b)
print(*z)

# deleting attributes
print(Program.__dict__)  # lets call dict attribute
# lets delete the x attribute
delattr(Program, "x")
print(Program.__dict__)  # lets call dict attribute
# we can also you del keyword to delete the attribute
del Program.version
print(Program.__dict__)  # lets call dict attribute
