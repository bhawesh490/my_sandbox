# all elements are in this code
a=4
b=5
c=[6,7]
d="Hi"
"Hello"
def area(x):
    return x**2
area(3)

'''
objects:
all objects occupy some space in memory in ram
I am an object and my name is identifier
objects:4,5,[6,7],6,7,"Hello","Hi"
function definition ,2,3,9
function definition is also an object because it 
stores the logic of the function like it has to store square of x

identifiers:
a,b,c,d,area,x
operators:
**
delimiters:
=," () :[]
keywords:def,return
comments:#code with different element
Blank lines
white spaces
Indentation

'''
# understaning objects in python
import sys
inty=5
listy=[6,7]
stringy="Hi"
# import folium 
# azores=folium.folium.Map(location=(38,-27),zoom_start=6)

'''
objects:5,[6,7](compound object),6,7,"Hi",
folium.folium.Map(location=(38,-27),zoom_start=6)(compund object)
38,-27,6

All objects have something in common.all object have a type.variables dont have type
type(inty),type(listy),type(stringy),type(azores)
(int,list,str,folium.folium.Map)

all those are indentifers we can refer object directly
type(5),type([6,7]),type("Hi"),type(folium.folium.Map(location=(38,-27))
(int,list,str,folium.folium.Map)

5,"Hi" looks not similar to folium.folium.Map(location=(38,-27)
even though 5 looks simple its just a shortcut of int(x=5)
so int is a class Map is also a class and these classes create objects

[6,7]=list((6,7))
list is a class which created the object 
these are just shortcut and developed by python developers becuase they are frequently used.
"Hi"=str(object="Hi")
str is a class

folium.folium.Map(location=(38,-27))
each object is like an atom and we can do some operations there.they have some properties like
int object can do addition
4+5
"hi".capitalise()
folium.folium.Map(location=(38,-27)).save('output.html')
we can save our map object in html file

'''
# lets look at the library path

# print (folium.__file__)
# C:\Users\SESA733833\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\folium\__init__.py
'''
here we can find what all this object can do .in this path a 
file is created where classes are defined 
when arguments object can take etc are defined here

like def is a keyword for creating a function class is the keyword for creating an object 
int,str objects are desiged by python developers and are written in c python and these objects are written
in c language therefore we cannot view the code of those objects.

'''
import pandas 
print (pandas.__file__)

