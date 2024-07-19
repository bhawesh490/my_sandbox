class Test:
    def __init__(self, name):
        self.name = name
        self.greetings = self.greet()

    def greet(self):
        return f"Hi greeting from property {self.name}"


t = Test("John")
print(t.name)
print(t.greetings)
print(t.greet())


class Hi:
    a = Test("John cena").greetings
    b = Test("Alex great").greetings


print(Hi.a)
print(Hi.b)
