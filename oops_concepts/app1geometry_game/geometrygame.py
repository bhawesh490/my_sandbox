'''Development steps
1-Write down objects in a paper
2-writing a class for each object
3-writing methods(functions) for each class
4-calling/instiating the classes and their methods

For our use case our objects are rectangle and points
just like we have int type we will create point type or rectangle type

'''
'''
Classes Nomenclautre
class Point: is correct 
class PinPoint:is correct use Camelcase
class pin_point:not correct these style is used for functions

'''


class Point:
    '''
    what are the minimum requirement for the point to exist 
    these wiil be x,y
    to determine a point we would at least need a x,y coordinate
    so to declare those mimimum requirement we declare a function
    '''
    # this is a special function
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
# Now we have a new type in our python session
# lets create an instance of that type

point1=Point(1,2)

# Point(1,2) is called an object instance now of the Point type
# we are storing this object inside a variable 
print (type(point1))
# <class '__main__.Point'>
# this is equivalent to
number1=int("2")
print (type(number1))
# <class 'int'>

# we can create as many objects we required like we created many integers 
point2=Point(3,4)
point3=Point(6,7)
point4=Point(8,9)

number2=int("4")
number2=4
number3=int("5")
number3=5

print ("the class belongs to",type(point2))
# '__main__.Point' the __main__ means that this type/class belongs to this particular script

# lets take an example

import geometry

print ("This class belongs to",type(geometry.UnderstandMainConcept(1,2)))
print ("The path to the file is",geometry.__file__)

import ipaddress
print (ipaddress.__file__)

my_ip=ipaddress.ip_address("1.1.1.1")
print (type(my_ip))


# self
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print (self)
        
point1=Point(1,2)
point2=Point(3,4)

'''
self is a variable that holds object instance that is being created by that class
in the above Point is the class/type Point(1,2) is the object instance
1 is the value of parameter x
2 is the value of parameter y
in the above example clearly we can see that when we print self it prints two object 
instances we created

'''

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
point1=Point(1,2)
point2=Point(3,4)
print (point1.x)
print (point1.y)

'''
above command confirms that self is the object
x and y are variables of instance objects

'''

class Point:
    def __init__(self,x,y):
        self.x_argument=x
        self.y_argyment=y
        
point1=Point(1,2)
point2=Point(3,4)
print (point1.x_argument)
print (point1.y_argyment)


class Point:
    def __init__(this_object,x,y):
        this_object.x=x
        this_object.y=y
        
point1=Point(1,2)
point2=Point(3,4)


# intatiate a class means creating an object 
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

person1=Person("Bhawesh",31)
print ("the name of the person is",person1.name)
print ("the age of the person is",person1.age)        

# you can see the usage of arguments in the above code but the best way is shown below
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
person1=Person("Bhawesh",31)
print ("the name of the person is ",person1.name)
#So basically we are defining the attribute of the object like name and age
# name is one of the attribute similarly age is other attribute

# Creating a Method
print("hi".upper())

# in the above example we can see that hi object which is of string type/class has a method call upper() 
# method is kind of saying what object can do 

# Similary let's create methods for our class Point

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # __init__is a special method which just defines the args x and y and does not return anything

    def falls_in_rectangle(self,lowleft,rightleft):
        if lowleft[0]<self.x<rightleft[0] and \
        lowleft[1]<self.y<upright[1]:
            return True
        else:
            return False

point1=Point(1,2)

print (point1.falls_in_rectangle((1,2),(2,3)))
# note here falls_in_rectangle is the method of the point1

# Difference between __init__method and Normal Methods




class Point:
    def __init__(self,x,y):
        print ("I am a __init__!")
        self.x=x
        self.y=y
    # __init__is a special method which just defines the args x and y and does not return anything

    def falls_in_rectangle(self,lowleft,rightleft):
        print ("I am Ordinary")
        if lowleft[0]<self.x<rightleft[0] and \
        lowleft[1]<self.y<upright[1]:
            return True
        else:
            return False

point1=Point(2,3)
point1.falls_in_rectangle((5,6),(10,20))

# So basically print function inside init method print as soon as object is instiatied

# Adding distance method to the Point class
import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # __init__is a special method which just defines the args x and y and does not return anything

    def falls_in_rectangle(self,lowleft,rightleft):
        if lowleft[0]<self.x<rightleft[0] and \
        lowleft[1]<self.y<rightleft[1]:
            return True
        else:
            return False
        
    def distance_from_point(self,a,b):
        distance=(a-self.x)**2+(b-self.y)**2    
        final_distance=math.sqrt(distance)
        return final_distance
point1=Point(1,2)
print (point1.distance_from_point(10,8))
print (type(point1))

######################################################################################################


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # __init__is a special method which just defines the args x and y and does not return anything

    def falls_in_rectangle(self,rectangle):
        if rectangle.lowleft.x<self.x<rectangle.upright.x and \
        rectangle.lowleft.y<self.y<rectangle.upright.y:
            return True
        else:
            return False
        
point1=Point(1,2)
print("X coordinate of point1 object is",point1.x)
print("Y coordinate of point1 object is",point1.y)


class Rectangle:
    def __init__(self,lowleft,upright):
        self.lowleft=lowleft
        self.upright=upright

pointx=Point(6,7)
rectanglex=Rectangle(Point(5,6),Point(7,9))
print (pointx.falls_in_rectangle(rectanglex))

###################################################################################################

# Adding Features

from random import randint 


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # __init__is a special method which just defines the args x and y and does not return anything

    def falls_in_rectangle(self,rectangle):
        if rectangle.lowleft.x<self.x<rectangle.upright.x and \
        rectangle.lowleft.y<self.y<rectangle.upright.y:
            return True
        else:
            return False
        


class Rectangle:
    def __init__(self,lowleft,upright):
        self.lowleft=lowleft
        self.upright=upright

rectanglex=Rectangle(Point(randint(0,9),randint(0,9)),Point(randint(10,19),randint(10,19)))
print ("Rectangle Coordinates:",rectanglex.lowleft.x,",",rectanglex.lowleft.y\
      ,",", rectanglex.upright.x,",",rectanglex.upright.y\
       )

user_point=Point(float(input("Guess X:")),float(input("Guess Y:")))
print ("Your Point was inside rectangle:","Inside Rectangle" \
       if user_point.falls_in_rectangle(rectanglex) ==True \
       else "Not Inside Rectange")


# let's add other feature in our code


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # __init__is a special method which just defines the args x and y and does not return anything

    def falls_in_rectangle(self,rectangle):
        if rectangle.lowleft.x<self.x<rectangle.upright.x and \
        rectangle.lowleft.y<self.y<rectangle.upright.y:
            return True
        else:
            return False
        


class Rectangle:
    def __init__(self,lowleft,upright):
        self.lowleft=lowleft
        self.upright=upright

    def area(self):
        return (self.upright.x-self.lowleft.x)*(self.upright.y-self.lowleft.y)    

rectanglex=Rectangle(Point(randint(0,9),randint(0,9)),Point(randint(10,19),randint(10,19)))
print ("Rectangle Coordinates:",rectanglex.lowleft.x,",",rectanglex.lowleft.y\
      ,",", rectanglex.upright.x,",",rectanglex.upright.y\
       )

user_point=Point(float(input("Guess X:")),float(input("Guess Y:")))
user_area=float(input("Guess Rectangle Area: "))


print ("Your Point was inside rectangle:","Inside Rectangle" \
       if user_point.falls_in_rectangle(rectanglex) ==True \
       else "Not Inside Rectange")

print ("Your Area was off by ",rectanglex.area()-user_area)
