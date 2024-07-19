try:
    print("Running the try block")
    exit(1)
    print(1 / 0)
    print("This will not be printed")
    print(1 / 1)
except Exception as e:
    print("An exception occurred: ", e)
    exit(1)
