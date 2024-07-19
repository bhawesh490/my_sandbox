print ("##########################################################################")
print ("#############Encapsulation and Abstraction in Python#######################")
print ("##########################################################################")
# 1-attributes can be public and private(non public in python)
class Car:

    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

my_car=Car("Porche","911 Carrera",2020)
print (my_car.year)     
my_car.year=2056
print (my_car.year)   
my_car_new=Car("Porche","911 Carrera",2020)
print (my_car_new.year)

print ("##########################################################################")
print ("#############Demonstrating Non Public Attributes in Python#################")
print ("#############In Python No attribute is Private3333333333333################")
print ("##########################################################################")




class Car:

    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self._year=year

my_car=Car("Porche","911 Carrera",2020)
# print (my_car.year)     
# my_car.year=2056

class Movie:
    
    _id_counter=1

    def __init__(self,title,year):
        self._id=Movie._id_counter
        self.title=title
        self.year=year

        Movie._id_counter+=1

my_movie=Movie("Animal",2023)
print(Movie._id_counter)
# developer should note that the underscore is actually hinting them not to use outside of this class


# name mangling
# in name mangling the attribute changes to _classname__attribute
class Movie:

    def __init__(self,name,year):
        self.__name=name
        self.year=year

my_movie=Movie("Animal",2023)
print (my_movie.year)
print (my_movie._Movie__name)





class Book:
 
    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.title = title
        self.author = author
        self._num_pages = num_pages
        self._ISBN = ISBN
        self._publisher = publisher