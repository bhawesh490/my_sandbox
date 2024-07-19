# Methods
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circle_diameter(self):
        print (f"the diameter of the circle is {2*self.radius}")

my_circle=Circle(12)
my_circle.circle_diameter()  



class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item,str):
            self._items.append(item)

        else:
            print ("Please provide a valid item")

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
            return 1 
        else:
            return 0
        
    def has_item(self, item):
        return item in self._items

my_backpack=Backpack()
print (my_backpack.items)
my_backpack.add_item("water bottle")
print (my_backpack.items)
my_backpack.add_item("sleeping bag")
print (my_backpack.items)
print (my_backpack.has_item("water bottle"))
my_backpack.remove_item("sleeping bag")
print (my_backpack.items)

# default values

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def move_up(self, steps=5):
        self.y += steps

    def move_down(self, steps=5):
        self.y -= steps

    def move_left(self, steps=2):
        self.x -= steps

    def move_right(self, steps=2):
        self.x += steps

my_player=Player(1,2)   
print (my_player.y)
my_player.move_up()
print (my_player.y)
my_player.move_up(10)
print (my_player.y)
    





class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item,str):
            self._items.append(item)

        else:
            print ("Please provide a valid item")

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
            return 1 
        else:
            return 0
        
    def has_item(self, item):
        return item in self._items
    
    def sorted_list(self, sorted_list=False):
        if sorted_list:
            return sorted(self._items)
        else:
            return self._items
        

my_backpack=Backpack()

my_backpack.add_item("water bottle")
my_backpack.add_item("Sleeping bag")
print (my_backpack.items)
sorted_list=my_backpack.sorted_list(True)
print (sorted_list)
sorted_list=my_backpack.sorted_list()
print (sorted_list)

# calling a method from other method

class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_multiple_items(self,items):
        for item in items:
            self.add_item(item)


    
    def add_item(self, item):
        if isinstance(item,str):
            self._items.append(item)

        else:
            print ("Please provide a valid item")

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
            return 1 
        else:
            return 0
        
    def has_item(self, item):
        return item in self._items
    
    def sorted_list(self, sorted_list=False):
        if sorted_list:
            return sorted(self._items)
        else:
            return self._items
my_backpack=Backpack()
my_backpack.add_multiple_items(["pen","pencil"])
print (my_backpack.items)


print ("Return and print in a function")

class Calculator:
 
    def add(self, a, b):
        print(a + b)
        return True
 
    def multiply(self, a, b):
        return a * b
    

my_calc=Calculator()
my_calc.add(1,2)
print (my_calc.add(1,2))

my_calc.multiply(3,4)
return_variable=my_calc.multiply(3,4)
print (return_variable)


# method chaining

class Pizza:
 
    def __init__(self):
        self.toppings = []
 
    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self
 
    def show_toppings(self):
        print("This Pizza has:")
        for topping in self.toppings:
            print(topping.capitalize()) 



my_pizza=Pizza()
print (my_pizza.add_topping("oregano").add_topping("Chilly Flakes"))
my_pizza.show_toppings()
print (my_pizza.toppings)


# Assignment

class Cashregister:

    def __init__(self):
        self.products = []


        

