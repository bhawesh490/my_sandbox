from math import pi

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center = center_x,center_y   #this will create a tuple or we can give (center_x,center_y) also
        self.radius = radius 

    def area(self):
        return pi * self.radius ** 2

    def translate(self, x, y):
        self.center = (self.center[0] + x, self.center[1] + y)

c = Circle(1,2,3)
print(c)
print(c.radius)
print(c.center)

import csv
class Forex:
    def __init__(self, file_name):
        with open(file_name) as f:
            reader = csv.reader(f)
            self.headers = next(reader)
            self.data = list(reader)

test = Forex('test.csv')
print(test.headers)
print(test.data)
import datetime
from math import Decimal
####################################
class DataPoint:
    def __init__(self, date, value):
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        self.value = Decimal(value)


class Forex:
    def __init__(self, file_name):
        with open(file_name) as f:
            reader = csv.reader(f)
            self.headers = next(reader)
            self.data = [DataPoint(row[0], row[1]) for row in reader]  
#observe how DataPoint class in available in other class for usage 

class DataPoint:
    def __init__(self, date, value):
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        self.value = Decimal(value)


class Forex:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.process_data()

    def process_data(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            next(reader)
            return [DataPoint(row[0], row[1]) for row in reader]
        