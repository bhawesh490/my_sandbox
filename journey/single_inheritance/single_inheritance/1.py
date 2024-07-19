# shape
# Ellipse Polygon
# Circle  Rectangle  Triangle
# Square


class Shape:
    pass


class Ellipse(Shape):
    pass


class Circle(Ellipse):
    pass


class Polygon(Shape):
    pass


class Rectangle(Polygon):
    pass


class Square(Rectangle):
    pass


class Triangle(Polygon):
    pass


print(issubclass(Rectangle, Polygon))
print(issubclass(Rectangle, Shape))
s = Shape()
sq = Square()
print(isinstance(s, Shape))
print(isinstance(sq, Rectangle))

print(type(Shape))
print(type(s))  # gives very specific type or the class from which it was created

sq = Square()
p = Polygon()
# i want to know if sq is the instance of whatever class p was created from
print(isinstance(sq, type(p)))

# shape inhertis from object (built in class)
print(type(object))


class Person:
    pass


print(issubclass(Person, object))
print(issubclass(Shape, object))
