from threading import Thread, current_thread


def display(msg):
    current_thread()
    print(msg, current_thread())


# create an object of thread class
t1 = Thread(target=display, args=("Hello World",))
# start the new thread
t1.start()

for i in range(5):
    # main thread chalayega
    print("Welcome", current_thread())
