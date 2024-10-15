import json
class Test:
    def __init__(self, name):
        self.name = name
    def to_string(self):
        json.dumps(self.to_dict())

t = Test("bhawesh")
print(t.to_string()) # None
