# dunder method 
# double underscore
# example __init__(self)
print(5+6)
print((5).__add__(6))

# __str__ method

# print(obj)--->__str__() 
class Point2D:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __str__(self):
        return f"({self.x},{self.y})"

my_point = Point2D(4,5)
print(my_point)    
# print(my_point.__str__())  

class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name 
        self.gpa = gpa 
        self.age = age

    def __str__(self):
        return f"Student: {self.name}\nid: {self.student_id}\nage: {self.age}"    
    
student = Student(1,"Bhawesh",31,8)
print(student)    


# __len__ method

my_string = "Bhawesh Mehta"
print(len(my_string))
print(my_string.__len__())


class Backpack:

    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def remove_items(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("This item is not in the backpack")

    def __len__(self):
        return len(self.items)                



my_backpack = Backpack()
print(len(my_backpack))
my_backpack.add_items("Bhawesh")
print(len(my_backpack))

# __getitem__() method

my_list = ["a","b","c","d"]
print(my_list[0])
print(my_list[1])
print(my_list.__getitem__(0))
print(my_list.__getitem__(1))
