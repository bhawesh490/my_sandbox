# # print(add())
# def decorate(func):
#     def inner(*args,**kwargs):
#         print("arguments passed are: ",args)
#         print("Decoration started...")
#         a = func(*args,**kwargs)
#         print("Decoration ended...")
#         return a
#     return inner
# @decorate
# def add(*args):
#     print("Hello friend i am inside add function")
#     return 2
# print(add(1,2,3,4,5,6,7,8,9,10))


# print(add())
def outer(custom_args):
    print(custom_args)
    def decorate(func):
        def inner(*args,**kwargs):
            print("arguments passed are: ",args)
            print("Decoration started...")
            a = func(*args,**kwargs)
            print("Decoration ended...")
            return a
        return inner
    return decorate
@outer("hello")
def add(*args):
    print("Hello friend i am inside add function")
    return 2
print(add(1,2,3,4,5,6,7,8,9,10))

