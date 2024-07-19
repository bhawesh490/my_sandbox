# Inheritance in the classes
class Polygon:
    pass 

class Triangle(Polygon):
    pass 

class Square(Polygon):
    pass

print(issubclass(Square,Triangle))  # True

# Inherit attributes of the class

class Polygon:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color 

class Triangle(Polygon):
    pass 

my_triangle = Triangle(3,"Green")
print(my_triangle.color)

# if the subclass has its own init method the attributes of the superclasss are not inherited automatically


class Polygon:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color 

class Triangle(Polygon):
    NUM_SIDES = 3


    def __init__(self, base, height,color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base 
        self.height = height

# super() refers to immediate parent class
class Polygon:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color 

class Triangle(Polygon):
    NUM_SIDES = 3


    def __init__(self, base, height,color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base 
        self.height = height



my_triangle = Triangle(3,4,"Green")
print(my_triangle.color)


########################################################################################

class Employee:

    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary =  salary 

class Programmer(Employee):

    def __init__(self, full_name, salary, programming_language):
        Employee.__init__(self, full_name, salary)
        self.programming_language = programming_language


bhawesh = Programmer("Bhawesh Mehta",12000,"Python")
print(bhawesh.full_name)
print(bhawesh.salary)
print(bhawesh.programming_language)


#############################################################################
class Character:

    def __init__(self, x, y, num_lives):
        self.x = x 
        self.y = y 
        self.num_lives = num_lives 

class Player(Character):

    INITIAL_X = 0
    INITIAL_Y = 0 
    INITIAL_NUM_LIVES = 10

    def __init__(self, score=0):
        Character.__init__(self, Player.INITIAL_X, Player.INITIAL_Y, Player.INITIAL_NUM_LIVES)
        self.score = score 



class Enemy(Character):

    def __init__(self, x=15, y=15, num_lives=8, is_poisonous=False):
        Character.__init__(self, x, y ,num_lives)
        self.is_poisonous = is_poisonous



my_player = Player()
print(my_player.score)
print(my_player.x)
print(my_player.y)
print(my_player.INITIAL_NUM_LIVES)

easy_enemy = Enemy(num_lives=1)
hard_enemy = Enemy(num_lives=56, is_poisonous=True)
print(hard_enemy.is_poisonous)
print(hard_enemy.num_lives)
print(hard_enemy.x)
print(hard_enemy.y)


#################################################################
class Vehicle:
    
    def __init__(self, color, speed, fuel_type):
        self.color = color
        self.speed = speed  # In Km/h
        self.fuel_type = fuel_type

# Write your code below:
class Car(Vehicle):
    
    DEFAULT_SPEED = 200
    
    def __init__(self, num_doors, is_electric, color, fuel_type):
        Vehicle.__init__(self, color, Car.DEFAULT_SPEED, fuel_type)
        self.num_doors = num_doors 
        self.is_electric = is_electric
        

my_car = Car(4,"Yes","Red","Diesel")

print(my_car.DEFAULT_SPEED)










