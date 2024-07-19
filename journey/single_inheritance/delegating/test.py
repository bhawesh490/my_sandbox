class Test:
    @property
    def greet(self):
        return "Hi greeting from property"


t = Test()
t.greet
# print(t.greet)


class Test:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print("Getter Called..")
        return self._name

    @name.setter
    def name(self, value):
        print("Setter Called..")
        self._name = value

    def greet(self):
        return f"Hi greeting from property {self._name}"


t = Test("John")
print("----------")
print(t.name)
print("----------")
t.name = "Doe"
print("----------")
print(t.name)
print("----------")
print(t.greet())
