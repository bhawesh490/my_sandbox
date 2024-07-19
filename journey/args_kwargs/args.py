def my_func(a, b, *args):
    print(a)
    print(b)
    print(args)

print(my_func(1,2))
print(my_func(1,2,3,4,5))
z= [1,2,3]
print(*z) #unpact the list
z = (1,2,3)
print(*z) #unpact the tuple


