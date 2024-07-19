# concept of alias 
a = [1,2,3,4,5]
b = a 
print(id(a))
print(id(b))
print(a is b)
# print(globals())

# print(__file__)
# Alias are different names assigned to the same object
print("#############################################################################")
print("##################Defining Circle Class######################################")
print("#############################################################################")

class Circle:

    def __init__(self, radius):
        self.radius = radius

my_circle = Circle(4)
your_circle = my_circle
print(my_circle.radius)
your_circle.radius  = 5
print(my_circle.radius)
print(your_circle is my_circle)


class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            print("This item is not present in the backpack")
            
                        