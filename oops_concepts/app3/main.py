class Canvas:
    def __init__(self,a,b,color):
        self.color=color
        self.a=a
        self.b=b
    def make(self):
        pass


class Rectangle:
    def __init__(self,x,y,a,b,color):
        self.x=x
        self.y=y
        self.a=a
        self.b=b
        self.color=color

    def draw(self,canvas):
        pass

class Square:
    def __init__(self,x,y,a,color):
        self.x=x
        self.y=y
        self.a=a
        self.color=color
    def draw(self,canvas):
        pass 

    
        



