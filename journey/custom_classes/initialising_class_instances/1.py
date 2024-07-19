class Person:
    def __init__(self):
        print(f"Initialising a new Person object:{self}")


p = Person()
print(hex(id(p)))


class Person:
    language = "English"

    def __init__(self, name):
        self.name = name
        self.language = Person.language


p = Person("John")
print(p.name)
print(p.__dict__)
print(Person.__dict__)
