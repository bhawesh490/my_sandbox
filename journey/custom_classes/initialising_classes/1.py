class Person:
    """class to represent a Person"""
p1 = Person()
print(p1) # <__main__.Person object at 0x7fea08b03f10>
print(type(p1)) # <class '__main__.Person'> means this Person call is in the main module of my notebook
print(hex(id(p1))) # 0x7fea08b03f10

class Person:
    def __init__(self):
        print('custom init...')

p = Person() # custom init... 
# print(p)

class Person:
    def __init__(self):
        print('custom init...',self)
p = Person() # custom init... <__main__.Person object at 0x7fea08b03f10>
print(hex(id(p))) # 0x7fea08b03f10
# so when we create the person instance python called the init function.it passed the instance of the class in the init function 

class Person():
    def __init__(self):
        self.first_name = "Eric"
        self.last_name = "Jane"

p1 = Person()
p1.first_name # Eric
p1.last_name # Jane
print("Calling dunder dict method\n",p1.__dict__)        


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

p1 = Person("Eric","Jane")
p1.first_name # Eric
p1.last_name # Jane
print("Calling dunder dict method\n",p1.__dict__)        

p2 = Person("John","Doe")
p2.first_name # John
p2.last_name # Doe
print("Calling dunder dict method\n",p2.__dict__)

class Point:
    def __init__(self, *coords):
        self.coordinates = coords 
        print(f'dimension :{len(coords)}')
p = Point(1,2,3,4,5)  #* coords will actually be a tuple
print(p.coordinates) # (1, 2, 3, 4, 5)
print(p.__dict__)


class Circle:
    def __init__(self, *, radius=1):
        self.radius = radius 
c = Circle()
c.radius # 1    
c = Circle(radius=10) 
# as we have given * we mean no pass mandatory key word argument
c.radius # 10
print(c.__dict__)
print(vars(c))


class Circle:
    def __init__(self, *, radius=1):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius 
c = Circle()
c.radius # 1    
c = Circle(radius=10) 
# as we have given * we mean no pass mandatory key word argument
c.radius # 10
print(c.__dict__)
print(vars(c))


def condition(x):
    if x < 0:
        print("x is less than 0")
    print("ok")   
condition(-1) # x is less than 0 ok 
condition(1) # ok


def condition(x):
    if x < 0:
        raise ValueError("x is less than 0") #it will raise and error and terminate since we have not handled errors using try and except
    print("ok")   
condition(10) # ok
condition(-1) # ValueError: x is less than 0
