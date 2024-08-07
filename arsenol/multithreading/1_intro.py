import threading

print(threading.current_thread())
# <_MainThread(MainThread, started 140318092554240)> no is pid
print(threading.current_thread().is_alive())
# There are 2 ways of creating multi threading in python:
# 1. Using Thread Class present in threading module
# 2. by extending Thread Class

# Steps:
# 1-Import Thread class from threading ModuleNotFoundError
# 2-create a function  containing code to be executed parallelly
# 3-create an object of thread class
# 4-start the thread using start() method


from threading import Thread


# def display():
#     print(threading.current_thread())

#     for _ in range(4):
#         print("Hello World")


# t1 = Thread(target=display)
# t1.start()


# # Arguemt passing to the function
# def display_with_args(n, msg):
#     print(threading.current_thread())

#     for _ in range(n):
#         print(msg)


# t2 = Thread(target=display_with_args, args=(5, "Hello World"))
# t2.start()


# Single Arguemt passing to the function
# def display_with_args(n):
#     print(threading.current_thread())

#     for _ in range(n):
#         print("single args")


# t2 = Thread(target=display_with_args, args=(5,))
# t2.start()
