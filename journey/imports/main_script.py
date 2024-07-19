class Person:

    def __init__(self, name, age , sex):
        self.age = age 
        self.sex = sex 
        self.name = name

    def greet(self):
        print("Hi i am ",self.name,"My age is ,", self.age,"My sex is ,", self.sex)



person_1 = Person("Saumya",23,"F")
person_1.greet()


