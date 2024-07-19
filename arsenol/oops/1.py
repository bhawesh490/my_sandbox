# Instance are objects of the class 
class House:
    def __init__(self, price):
        self.price=price 

# see the space between the args
class Backpack:
    def __init__(self, color, size):
        self.items = []
        self.color = color
        self.size = size


class Circle:
    def _init__(self, radius):
        self.radius = radius 
        self.color = "Blue"


        

print (globals())

class Backpack:
    def __init__(self):
        self.items = []
        print (self)


my_backpack=Backpack()
print (my_backpack)
print (my_backpack.items)

my_backpack.items=[1,2,3]

# to access the attribute inside a class use
# self.attribute
# outside a class
# object.attribute




class Circle:
    def __init__(self, radius=5):
        self.radius = radius


my_circle=Circle(10)
print (my_circle.radius)



# update the value of instance attributes
class Backpack:
    def __init__(self, color):
        self.color = color
        self.items = []

my_backpack=Backpack('Red')
print (f"Color of backpack is {my_backpack.color}")
# let's update the color of Backup now
my_backpack.color='Blue'
print (f"Color of my backpack is now {my_backpack.color}")





