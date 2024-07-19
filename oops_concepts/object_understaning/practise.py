# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y 

# point1=Point(1,2)
# print (point1)  
# print (type(point1))  
# # __main__==location where the script or the class locates
# print (point1.x)
# print (point1.y)    

# Tips to write the classes and methods
# think of attributes first not the methods 

# step 1
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y 

# class Rectangle:
#     def __init__(self,lowleft,upright):
#         self.lowleft=lowleft
#         self.upright=upright

# step 2

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y 

    def point_fall_in_rectangle(self,rectangle):
        if rectangle.lowleft.x<=self.x<=rectangle.upright.x\
            and rectangle.lowleft.y<=self.y<=rectangle.upright.y:
            return True
        else:
            return False
        
            


class Rectangle:
    def __init__(self,lowleft,upright):
        self.lowleft=lowleft
        self.upright=upright
