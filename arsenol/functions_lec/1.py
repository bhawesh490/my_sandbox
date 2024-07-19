# if a function does not return anything it return None
from pprint import pprint 
def hello():
    return "Hi"

# global (namespaces) is a dictionay key are parameters and values are arguments
print (globals())   
a=10 
pprint (globals()) 
f=hello
pprint (globals()) 

li=[1,2,3]
pprint (globals()) 
l2=li
pprint (globals()) 
# function has a property called name 
print (hello.__name__)

def add(a,b,c):
    print (a)
    print (b)
    print (c)
    return a+b+c
# we have global dictionary with belong to tihs notebook but apart from this we also have local dictionay which
# are local to the function when functions are runnning 

pprint(globals())
result=add(1,2,3)
pprint(globals())


def add(a,b,c):
    print ("Initial Namespace",locals())
    sum_=a+b+c
    print ("After Namespace",locals())
    return a+b+c
result=add(1,2,3)

add(10,20,30)
# we can clearly see that in locals we have short lived dictionaries

data=[1,2,3,4,1]
for element in data:
    if element<0:
        break
else:
    print ("processing all positive elements")

def is_all_positive(data):
    for element in data:
        if element < 0:
            # as soon as it finds any element less than 0 it return false and breaks the loop and exits 
            return False
        
    return True

print (is_all_positive([1,2,3]))

def gen_matrix(m,n,default_values):
    return [[default_values for i in range(n)] for j in range(n)]

print (gen_matrix(5,10,5))        

list_=[1,2,3,4]
print (*list_)