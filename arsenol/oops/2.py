# We have instance attributes as well as class attributes in this 
# section we will learn class attributes
# class attributes belongs to the class not the instance 
class Dog:

    species="Canis Lupus"

    def __init__(self,name,age,breed):
        self.age=age
        self.name=name
        self.breed=breed 

# species is the class attribute
print (f"class attribute is: {Dog.species}")


class Movie:

movie_id = 1

    def __init__(self, name):
        self.id = Movie.movie_id
        self.name = name

        Movie.movie_id=Movie.movie_id+1


m_1 = Movie("1st Movie")
print (m_1.id)
print (m_1.name)   
print (Movie.movie_id)
m_2 = Movie("2nd Movie")
print (m_2.id)
print (m_2.name)   
print (Movie.movie_id)


print (globals())
# print (__file__)


class random:

    id=1

    def __init__(self):
        pass

ri=random()
print (random.id)    #can access class attribute directly with the class.attribute
print (ri.id)        #can access class attrivute using instance.attribute because these class attrbiutes are same for all instances


print ("##########################################################################")
print ("#############how to modify the attributes of the class####################")
print ("##########################################################################")

class Circle:

    radius=5

    def __init__(self,color):
        self.color=color

print (Circle.radius)

my_circle=Circle("Blue")
your_circle=Circle("Green")
print (my_circle.radius)
print (your_circle.radius)
Circle.radius=10

print (my_circle.radius)
print (your_circle.radius)


print ("##########################################################################")
print ("#############Assignment of the class attributes###########################")
print ("##########################################################################")


class Programmer:
    
     # Add the class attributes
    salary=100000
    monthly_bonus=10000
    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages
 
 
class Assistant:
    salary=10000
    monthly_bonus=1234
    
    # Add the class attributes
    
    def __init__(self, name, age, address, phone, is_bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.is_bilingual = is_bilingual
 
 
# Function that prints the monthly salary of each worker
# and the total amount that the startup owner has to pay per month.
def calculate_payroll(employees):
 
    total = 0
 
    print("\n========= Welcome to our Payroll System =========\n")
 
    # Iterate over the list of instances to calculate
    # and display the monthly salary of each employee,
    # and add the monthly salary to the total for this month.
    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary
 
    # Display the total
    print("\nThe total payroll this month will be: $", total)
 
# Instances (employees)
jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True)
 
# List of instances
employees = [jack, isabel, nora]
 
# Function call (Passing the list of instances as argument)
calculate_payroll(employees)


