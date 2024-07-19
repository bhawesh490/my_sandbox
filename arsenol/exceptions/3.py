try:
    print ("I am in try block")
    a=1
    b=1
    result=a/b
    print ("I was in try block")
except ZeroDivisionError as e:
    print ("Now i am trying exception")
    print("there was an error:" ,str(e))
# finally:
#     print("I will print everytime whether code fails or runs")

