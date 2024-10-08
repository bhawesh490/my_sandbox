def greet(func):

    def inner(*args, **kwargs):
        print(f"Hi there ! {args[0]}")
        result = func(*args, **kwargs)
        print("Nice meeting you")
        return result

    return inner


@greet
def my_name(name):
    print(f"My name is {name}")
    return "you passed the name"


# my_name("bhawesh")


# using a decorator factory
def factory(alpha):
    def greet(func):

        def inner(*args, **kwargs):
            print(alpha)
            print(f"Hi there ! {args[0]}")
            result = func(*args, **kwargs)
            print("Nice meeting you")
            return result

        return inner

    return greet


@factory("hohohoho")
def my_names(name):
    print(f"My name is {name}")
    return "you passed the name"


################Using decorators inside a class################
class MyName:
    def __init__(self, name):
        self.name = name

    @greet
    def my_name(self):
        print(f"My name is {self.name}")
        return "you passed the name"


name = MyName("bhawesh")
name.my_name()
