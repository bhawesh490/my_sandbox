# Special Methods
# 1-dunder string methods
class Circle:
    def __init__(self, radius):
        self.radius = radius


c = Circle(3)
print(c.radius)  # 3
print(c)  # <__main__.Circle object at 0x7f8b1c3b3d30>
print(str(c))  # <__main__.Circle object at 0x7f8b1c3b3d30>

# but the is not what we want to get from c object as output of print(list[1,2,3]) would be [1,2,3]
l = [1, 2, 3]
print(l)  # [1,2,3]
print(
    str(l)
)  # [1,2,3] its more meaningful than seeing well its a list object at some memory address

# so now we can tell python how to do a string represenation for our custom object


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return "this s our custom str representation"


c = Circle(1)
print("Checking dunder str method")
print(c)  # this s our custom str representation
print(str(c))  # this s our custom str representation
print(c.__str__())  # this s our custom str representation


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle({self.radius})"


c = Circle(1)
print(c.__str__())  # Circle(1)
print(c)  # Circle(1)

# use of __repr__ method


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle({self.radius})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"


c = Circle(1)
print(c)
print(c.__str__())  # same as print(str(c))
print(c.__repr__())  # same as print(repr(c))
print(str(c))
print(c)

# Method for Equality
# __eq__ method
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)
print(l1 == l2)
c1 = Circle(1)
c2 = Circle(1)
print(c1 is c2)
print(c1 == c2)  # its actually doing c1.__eq__(c2) behind the scenes


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius


c1 = Circle(1)
print(type(c1))  # <class '__main__.Circle'>
print(type(c1) is Circle)
# we can also type by using isinstance
print(
    isinstance(c1, Circle)
)  # True recommeneded for classes where inheritance is involved
print(isinstance([1, 2, 3], object))  # True
print(type([1, 2, 3]))  # <class 'list'>
