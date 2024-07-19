"""
This script demonstrates the usage of list comprehension, dictionary comprehension, and set comprehension in Python.
It includes examples of unpacking tuples, filtering elements based on conditions, and counting occurrences of elements.
"""

vectors = [(0,0), (0,1), (1,0), (1,1)]
import math
from math import sqrt 

for x ,y in vectors:  #observe how we have unpacked the tuples 
    print(x,y)

magnitude = [sqrt(x)+sqrt(y) for x ,y in vectors]
print(magnitude)    

statement = ['Python','is','a','good','langauage']
modified_statement = [item for item in statement if len(item)>2]
print(modified_statement)

sales = {
    'widget':0,
    'widget_1':1,
    'widget_3':4,
    'widget_4':5
}

high_sales = [key for key,value in sales.items() if value > 2 ]
print(high_sales)

discounted_sales = {key: value * 0.9 for key, value in sales.items() if value > 2}
print(discounted_sales)

widget_sales = [
{'name':'widget 1','sales':10},
{'name':'widget 2','sales':5},
{'name':'widget 3','sales':0}
]

d = { widget_sale['name']:widget_sale['sales'] for widget_sale in widget_sales}
print("output of d is")
print(d)

paragraph = "Python is a high-level programming language. It is versatile and easy to learn."
punc = ["-",".",","]

for x in punc:
    paragraph = paragraph.replace(x,' ')

print(paragraph)

paragraph = paragraph.split()

print(paragraph)

s = {x for x in paragraph}
print(s)

s = {x for x in paragraph if len(x) > 4}
print(s)

data = ['a','a','b','b','c','c','c','d','d','d','d']

d = {}
for item in data:
    if item in d:
        d[item] = d[item] + 1
    else:
        d[item] = 1

print("dictionary is")
print(d)

d = {}
for element in set(data):
    count = len([x for x in data if x == element])
    d[element] = count

print(d)

d = { element:len([x for x in data if x == element])
     for element in set(data)
}
print(d)




