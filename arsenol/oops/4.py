# Properties,getter and setters
class Movie:

    def __init__(self,title,rating):
        self._title=title
        self.rating=rating 

    def get_title(self):
        return self._title

my_movie=Movie("Animal",12)
print (my_movie._title) 

print (my_movie.get_title()) 


class Dog:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name 
    
    def set_name(self, new_name):
        if isinstance(new_name,str) and new_name.isalpha():
            self._name=new_name
        else:
            print ("Please enter a valid name")

my_dog=Dog("Blackie",6)
print ("My dog is",my_dog.get_name())  
my_dog.set_name("Milky")

print ("My dog new name is",my_dog.get_name())  
    
class Dog:

    def __init__(self, age):
        self.age = age


my_dog=Dog(12)
print (f"the age of my dog is {my_dog.age}")

my_dog.age=my_dog.age+1

print (f"the age of my dog after one year is {my_dog.age}")



class Dog:

    def __init__(self, age):
        self._age = age

    def get_age(self):
        print ("Getting the getter")
        return self._age
    
    def set_age(self,new_age):
        print ("Getting the setter")
        if isinstance(new_age,int) and 0 < new_age < 30:
            self._age=new_age
        else:
            print ("Please enter a valid age")

    age=property(get_age,set_age)        

my_dog=Dog(20)
# print (my_dog.get_age())
print (my_dog.age)
my_dog.age=my_dog.age+1
print (my_dog.age)


class Circle:

    VALID_COLORS=("RED","BLUE","GREEN")
    # we define the class constants in capital letter to make other developers understand that its not 
    # class attribute

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print ("Please Enter the new radius")

    radius=property(get_radius,set_radius)

    def get_color(self):
        return self._color
    
    def set_color(self,new_color):

        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print ("Please enter a valid color")

    color=property(get_color,set_color)        


my_circle=Circle(5,"Green")
print (my_circle.radius)
print (my_circle.color)

my_circle.color="Black"

print (my_circle.color)


my_circle.color="BLUE"

print (my_circle.color)


print ("Using @property for getter and setter")

class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    
    @property
    def rating(self):
        print ("calling the getter...")
        return self._rating
    @rating.setter
    def rating(self, new_rating):
        print ("calling the setter..")
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print ("Please enter a valid value")



            
my_movie=Movie("Animal",30)
print (my_movie.rating)

my_movie.rating=4.0

print (my_movie.rating)



class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        print ("calling the getter...")
        return self._items
    
    @items.setter
    def items(self,new_items):
        if isinstance(new_items, list):
            self._items=new_items
        else:
            print ("Enter a valid response")




def hello():
    print ("hello how are you")
    return "i am getting printed from outside print"

print (hello())    

        
