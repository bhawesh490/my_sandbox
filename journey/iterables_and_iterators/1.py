l = [1,2,3,4,5]
iterator = iter(l)
try:
    while True:
        #return next(iterator)  -->here we will just print it
        # print(next(iterator))
        print(iterator.__next__())
except StopIteration:
    #expected when we reach the end
    #so silence this exception
    pass

# Concept of iterator and iterable is very important in python.
l = [1,2,3]
iterator = iter(l)

print(type(iterator))   #<class 'list_iterator'>
print(next(iterator))   #1
print(next(iterator))   #2
print(next(iterator))   #3
# print(next(iterator))   #StopIteration Error
# the only way to now call the iterator is to define the new iterator
print(id(iterator))     #140355974283216
iterator = iter(l)
print(id(iterator))     #140355974283168
print(next(iterator))   #1
print(next(iterator))   #2

l = [1,2,3]
for i in l:
    print(i)
# let;s mimick the for loop

itertor = iter(l)
try:
    while True:
        element = next(iterator)
        print(element)

except StopIteration:
    pass

# range is also an iterable like list and can be called multiple times but it is a lazy iterable
r = range(10)
r = range(1000000)
# if we define range of such large numbers it does not create a list but rather iterable and iterator 
# and is created on the fly.it is called lazy iterable
# Example:
for i in range(1000000):
    print(i)
    if i > 4:
        break

# the advantage we get from range is that we dont have to store the entire list in memory and we 
# dont have to encur the cost of defining the large list of million elements in memory
# this is the concept of lazy evaluation
# we can confirm the same behaviour using perfcouter
from time import perf_counter

start = perf_counter()
l = range(10000000)
end = perf_counter()
print(end-start)    #2.8999638743698597e-06

start = perf_counter()
l = list(range(10000000))
end = perf_counter()
print(end-start)    #0.5718664999585599
del l #delete the list to free up the memory
# so range is a lazy iterable not a iterator
r = range(10)
print(list(r))  #can call r multiple times
print(list(r))  #can call r multiple times

# but enumerate is an iterator object and can be not called multiple times as iterator is of one time use

enum = enumerate('abc')
print(list(enum))  #[(0, 'a'), (1, 'b'), (2, 'c')]
print(list(enum))  #[]
print(list(enum))  #[]  --->basically it is empyt now it does not have next object to iterate over
# next(enum)  #StopIteration Error as it is empty now
# so enumerate is an iterator object and can be called only once
# to rerun the enumerate we have to define the new enumerate object
enum = enumerate('abc')
print(list(enum))


# Generators
squares = [i**2 for i in range(10)]
print(squares)

# lets create a generator now 
squares = (i**2 for i in range(10))
print(squares)  #<generator object <genexpr> at 0x7f8b1c3b3f90>
print(type(squares))   #<class 'generator'>
# We see that is of a generator type and so an iterator and can be used only one time 

# iterating over squares generator(iterator) first time
for i in squares:
    print(i)

# iterating over squares generator(iterator) second time
for i in squares:
    print(i)   #no output as it is empty now

# so lets redifine the generator
squares = (i**2 for i in range(10))
# since square is an iterator if we use iter function it returns the same object
print(iter(squares) is squares)
#since square is an iterator we can also use next function of __next__ dunder method
print(next(squares))  #0

#we have to bit careful using generator example 
square = (i for i in range(10))
print(3 in square)  #True
print(list(square)) # u see that it will give [4, 5, 6, 7, 8, 9] because it has exhausted the elements until 3 in above statement
