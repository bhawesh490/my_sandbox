class xyz:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b 
        self.c=c
    def test(self):
        print ("I am from xyz class") 

class xyz1:
    def __init__(self,p,q,r):
        self.p=p
        self.q=q
        self.r=r
    def test2(self):
        print ("I am from xyz1 class") 

class abc(xyz):
    def test3(self):
        print ("I am from class abc") 


a=abc(1,2,3)
a.test()                  
a.test3() 


print ("############Multiple Inheritance################")

class alpha(xyz,xyz1):
    def __init__(self,*args,**kwargs):
        xyz.__init__(self,*args)
        xyz1.__init__(self,**kwargs)

    def test4(self):
        print ("I am from alpha class")

a=alpha(1,2,3,p=4,q=5,r=7)
print (a.a)
print (a.p)

print ("############ Multi LeveL Inheritance ################")


class xyz:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b 
        self.c=c
    def test(self):
        print ("I am from xyz class") 

class xyz1(xyz):
    def test2(self):
        print ("I am from xyz1 class") 

class xyz2(xyz1):
    def test3(self):
        print ("I am from class abc") 

z=xyz2(1,2,3)
print (z.a)