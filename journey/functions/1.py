def test_func():
    return 1

a = test_func()
print(a)

print("#######################")
f = lambda a, b : a + b
# f is the function object that lambda has created and returned a + b
z  = f(1,3)
print(z)

f1 =  lambda a, b, c : max(a, b, c)
z = f1(1,2,3)
print(z)

# right side of lambda is a return expression what ever a normal function can return we can put in
# the right side of the lambda 

# using args in lambda as we used in normal function
f = lambda a ,*args:a * max(args)
z = f(8, 2, 3, 4)
print(z)

# using default args in lambda as we used in normal function
f = lambda a=10 ,b=20 : a + b
z = f(2)
print(z)

#concept of global scopes

a= 100
def hello():
    print(a)

# is is printing 100 as result
hello()

# The behavior you’re observing in your Python code is due to variable scoping. Let’s break it down:

# You’ve defined a variable a with the value 100 in the global scope.
# Next, you’ve defined a function called hello().
# Inside the function, you’re trying to print the value of a.
# Here’s what’s happening:

# When you call the hello() function, it looks for the variable a within its local scope (i.e., inside the function). If it doesn’t find a locally, it looks in the enclosing scope (which is the global scope in this case).
# Since a is not defined within the function, Python looks in the global scope and finds the variable a with the value 100.
# Therefore, when you call hello(), it prints the value of a, which is 100.
# In Python, functions have access to variables defined in their enclosing scope (such as the global scope). This behavior is known as lexical scoping or closure. So yes, functions can access variables from outer scopes.

# However, if you were to define a new local variable a inside the hello() function, it would shadow the global a, and the function would use the local a instead.

# Remember that this behavior is specific to Python and its scoping rules. Other programming languages may have different scoping behaviors.


# Passing and returning functions

z = 2,3
print(z) #note z is a tuple 
# we can unpack z using *z 
print(*z)
print("####################################################")

def add(a, b):
    return a + b 

def greet(name):
    return f'Hello, {name}!'

def apply(func, *args):
    result = func(*args)
    return result 

z = apply(add, 2, 3)
print(z)

z = apply(greet,'John')
print(z)

z = apply(lambda a,b,c : a + b + c, 10, 20, 30)
print(z)

def mult(a, b):
    return a * b 

def power(a, n):
    return a ** n 

def choose_operator(name):
    if name == 'add':
        return add     # where this add is return from we dont have anything defined in the local name space of function
        # actually it gets called from the global name space.it find add function in the global namespace
    if name == 'mult':
        return mult 
    if name =='power':
        return power 

z = choose_operator('add')    
print(z)  #it will give this message <function add at 0x7fe037603eb0> these memory address are tempory evertime you run the script it gets changed
z = choose_operator('mult')   
print(z)  #it will give this message <function mult at 0x7f549959c0d0>

def choose_operator(name):
    def add(a, b):
        return a + b 
    
    if name == 'add':
        return add
    # now this add will come from local namespace as it is contained inside the function 

z = choose_operator('add')
print(z)     #<function choose_operator.<locals>.add at 0x7f4de454c1f0> focus of the local word 

# what if we used lambda function 
def choose_operator(name):

    if name == 'add':
        return lambda a, b : a + b
    # now this add will come from local namespace as it is contained inside the function 

z = choose_operator('add')
print(z)     #<function choose_operator.<locals>.<lambda> at 0x7fe8fc7f0280>
#now you can see that its bit hard to debug where this lambda is actually.that's why it is
# called anonymous function

#####################################################################################
print("\n###################### Map Concept #########################################")
#####################################################################################

data = ['a','aa','bbb','cccc']
length = [ len(i) for i in data ]
print(length)

# we can use generator to get this length but remember generator can be used only once as they are iterator
length = (len(i) for i in data)
print(length) #generator object at 0x7f4de454c1f0
print(list(length))
print(list(length)) #it will give empty list as generator can be used only once

#the same logic can be applied using map function 
length = map(len,data)
print(length) #<map object at 0x7f4de454c1f0>
print(list(length)) # [1, 2, 3, 4]
print(list(length)) #[]
# print(next(length)) #it will give error as map object is exhausted stopIteration error

#####################################################################################
print("\n###################### Closures Concept ###################################")
#####################################################################################

def outer(a: int, b: int) -> callable:
    """
    This is the outer function that takes two arguments, `a` and `b`.
    It returns an inner function that calculates the product of `a` and `b`
    and prints the values of `a`, `b`, the sum of `a` and `b`, and the product of `a` and `b`.
    """

    sum_ = a + b

    def inner() -> str:
        prod = a * b
        print(a, b, sum_, prod)
        return "You just called a closure"

    return inner

func = outer(2, 3)
print(func) #<function outer.<locals>.inner at 0x7f4de454c1f0>
print(func()) #2 3 5 6 You just called a closure
print(func.__closure__) #(<cell at 0x7f4de454c1f0: int object at
#0x7f4de4f3c3c0>, <cell at 0x7f4de454c1f0: int object at 0x7f4de4f3c3e0>)
# this is a dunder function on func object which gives the closure object

def outer(a, b):
    def inner(c):
        return c ** 2
    return inner 

func = outer(2, 3)
print(func(2))
print(func.__closure__) #None
# this dunder method return none as there is no closure in this case inner function uses it inner scope variable

# args can be function also
# note we have passed func not func() as we are passing the function object not the result of the function
def execute(func):
    def inner(a, b):
        result = func(a, b)
        return result
    return inner    

def add(a, b):
    return a + b

add_executor = execute(add) 
print(add_executor.__closure__) #(<cell at 0x7f2208c179d0: function object at 0x7f2208c244c0>,)
# this add_executor is a closure function as it has a closure object
print(add_executor(2, 3)) #5
