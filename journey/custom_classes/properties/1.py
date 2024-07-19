import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


c = Circle(1)
print(c.__dict__)  # {'radius': 1} radius value getting fetched from dictionary
print(c.area())
c.radius = 0  # here we have set the radius = 0
print(c.area())
print(c.__dict__)


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def radius(self):
        return self._radius

    def area(self):
        return math.pi * self.radius**2


c = Circle(1)
print(c.radius)


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return math.pi * self.radius**2


c = Circle(1)
print(c.radius)  # radius property is getting called
print(c.area)  # area property is getting called
# c.radius = 10  # this will give error as we have set the property as read only

# defining setter property


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def area(self):
        return math.pi * self.radius**2


c = Circle(1)
c.radius = 10
#####################################Notes from Advance #######################################################################


class Person:
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError("Name must be a non-empty string")


p = Person("Alex")
p.set_name("John")  # setting the name is a pain we want to use direct name
print(p.get_name())
# getting the name is is a pain again we have to call get_name method
# p.set_name("   ")
# print(p.get_name())

# to avoid calling methods to get and set values we have properties which can be used in similar
# lines of attributes usage


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("Getter Called...")
        return self._name

    def set_name(self, value):
        print("setter called....")
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError("Name must be a non-empty string")

    name = property(fget=get_name, fset=set_name)


p = Person("Alex")
print(p.name)
p.name = "Jane"
print(p.name)


# use of delete attribute


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("Getter Called...")
        return self._name

    def set_name(self, value):
        print("setter called....")
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError("Name must be a non-empty string")

    def del_name(self):
        print("Deleter called...")
        del self._name

    name = property(fget=get_name, fset=set_name, fdel=del_name)


p = Person("Alex")
print(p.name)
p.name = "Jane"
print(p.name)
del p.name
p.name = "Jane After delete"

print(p.name)
