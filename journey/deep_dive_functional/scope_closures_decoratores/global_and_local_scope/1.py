a = 20


def hello():
    a = 10
    print(a)


hello()
print(a)


def hello1():
    global a
    a = 10
    print(a)


hello1()
print(a)
