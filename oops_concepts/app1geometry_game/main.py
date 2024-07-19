# import turtle 
# # from this turtle library we we use one class called Turtle() and created an object Instance
# myturtle=turtle.Turtle()
# # calling penup() method of the object instance
# myturtle.penup() 
# myturtle.goto(50,75)
# myturtle.pendown()
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(200)
# myturtle.left(90)
# myturtle.forward(100)
# myturtle.left(90)
# myturtle.forward(200)
# # calling different class named done
# turtle.done()

# # now we want to modify our previous code and add a functionality where we want to draw a rectangle
from random import randint

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)



# Create rectangle object
rectangle = Rectangle(Point(randint(0, 400), randint(0, 400)),
              Point(randint(10, 400), randint(10, 400)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# # Get point and area from user
user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# # Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)


# Its not recommended to mess with the existing classes rather we should extend by creating different class
# which inherits the original classes


class GuiRectangle(Rectangle):
   '''
    Gui Rectangle is the child of Rectangle
    It means Gui Rectangle will have all the attributes of Parent Rectangle Class
    Means it will get the entire __init__ method for itself
    It will have that area method as well
    +
    we can add other methods as well and in our case it would be a draw method

    '''
   def draw(self,canvas):
        canvas.penup() 
        canvas.goto(self.point1.x,self.point1.y)
        canvas.pendown()
        canvas.forward(self.point1.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        # calling different class named done
        canvas.done()

class GuiPoint(Point):
    def draw(self,canvas,size=5,color='red'):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size=size,color=color)


import turtle      
gui_rectangle=GuiRectangle(Point(randint(0, 400), randint(0, 400)),Point(randint(10, 400), randint(10, 400)))       
myturtle=turtle.Turtle() 
'''this creates a canvas instance'''

gui_rectangle.draw(canvas=myturtle)

print (gui_rectangle.area())






