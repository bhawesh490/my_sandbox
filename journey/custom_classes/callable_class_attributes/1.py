class Program:
    language = "Python"

    def say_hello():
        print(f"Hello i am learning {Program.language}")


Program.say_hello()
getattr(Program, "say_hell")()
