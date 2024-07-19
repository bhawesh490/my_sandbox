# raising exceptions
# a = 1
# b = 0
# result = a/b 
# print(result)
# print("Line at 6")
# python will not terminate the program will instead raise the exception in the backend

try:
    a=1
    b=0
    result=a/b
except:
    print("there was an error")

print("code executed")    

# to see the type of error call Exception super class
try:
    a=1
    b=0
    result=a/b
except Exception as e:
    print("there was an error:" ,str(e))


# Exception is a super class
# ZeroDivisionError

try:
    a=1
    b=0
    result=a/b
except ZeroDivisionError as e:
    print("there was an error:" ,str(e))

print("--------------------------------------")
try:
    a=1
    b=1
    result=a/b
except ZeroDivisionError as e:
    print("there was an error:" ,str(e))
else:
    print("Try block executed suceesfully then only else block will be use")


print("--------------------------------------")
try:
    print ("I am in try block")
    a=1
    b=0
    result=a/b
    print ("I was in try block")
except ZeroDivisionError as e:
    print("there was an error:" ,str(e))
finally:
    print("I will print everytime whether code fails or runs")


print("--------------------------------------")

def ask_int():
    while True:
        try:   
            a = int(input("Enter a Interger"))
            return a
        except Exception as e :
            print("This is my input error: ",e)

     
# ask_int()  

print("--------------------------------------")

def test(a):
    if a < 0:
        raise Exception("Usr Entererd a wrong number")
    return a 

print(test(-4))

