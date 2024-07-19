# Method Inheritance
# Inherit method from the other class

class Polygon:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color

    def describe_polygon(self):
        print(f"This Polygon has {self.num_sides} sides and it's {self.color}")        

class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base ,height ,color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base 
        self.height = height

    def get_area(self):
        return (self.base*self.height)/2    
   

class Square(Polygon):

    NUM_SIDES = 4

    def __init__(self ,side_length, color):
        Polygon.__init__(self, Square.NUM_SIDES, color)
        self.side_length = side_length

    def get_area(self):
        return (self.side_length**2)
         
        
my_triangle = Triangle(2,3,"Red")
my_triangle.describe_polygon()
print(my_triangle.get_area())


my_square = Square(4,"Green")
my_square.describe_polygon()
print(my_square.get_area())


########################################################################################

class Triangle:
 
    def __init__(self, base, height):
        self.base = base
        self.height = height
	
    def find_area(self):
        print((self.base * self.height)/2)
 
 
class RightTriangle(Triangle):
	
    def display_area(self):
        print("=== Right Triangle Area ===")
 
        # This line calls the method from the Triangle class.
        Triangle.find_area(self)
 
		
right_triangle = RightTriangle(5, 6)
right_triangle.display_area()

###########################################################################################
# Method Overiding
# child class method takes precedence is case we have the same method name
class Teacher:

    def __init__(self, full_name, teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id

    def welcome_students(self):
        print(f"Welcome to class I am your teacher.My name is {self.full_name}")    

class ScienceTeacher(Teacher):

    def welcome_students(self):
        print("Science is Amazing")
        print(f"Welcome to class I am your teacher.My name is {self.full_name}")    

teacher = ScienceTeacher("Bhawesh","122")
teacher.welcome_students()