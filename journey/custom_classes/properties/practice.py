class Learn:
    def __init__(self, name):
        self._name = name
        print("Calling constructor and initialising name attribute", self.name)

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, value):
        print("setting name")
        self._name = value

    def test(self):
        print(self.name)

    name = property(fget=get_name, fset=set_name)


test = Learn("Alex")
# test.test()
test.name = "Jane"
print(test.name)
