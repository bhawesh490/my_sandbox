from temp import timed


@timed
def hello():
    print("Hello, World!")


hello()
