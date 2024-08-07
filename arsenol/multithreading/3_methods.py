from threading import Thread, current_thread


class Example:
    def display(self, msg):
        print(current_thread())
        print(msg)


t1 = Thread(target=Example().display, args=("Hello World",))
t1.start()
for i in range(5):
    print("Welcome", current_thread())
