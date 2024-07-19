# Objects in Memory
# in python everything is object
print(object)
# object is the base class from which all classes in python inherit
print(isinstance(2,object))
print(isinstance("hello",object))
print(isinstance([1,2,3],object))

class Movie:

    def __init__(self, name):
        self.name = name

print(isinstance(Movie,object))        

# id () function returns the address of the object in the memory

print(id(4))
a = [1,2,3,4]
b = [1,2,3,4]
print("id of a is",id(a))
print("id of b is",id(b))


class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items 

my_backpack = Backpack()
your_backpack = Backpack()
print("id of my_backpack",id(my_backpack))
print("id of your_backpack",id(your_backpack))

a = [1,2,3,4,5]
b = [1,2,3,4,5]

print(a is b)
print(a == b)


# unexpected behaviour to optimise memory
a = 5 
b = 5 
print(id(a))
print(id(b))
print(a is b)

a = 257
b = 257 
print(a is b)


