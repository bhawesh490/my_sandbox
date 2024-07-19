class list_parser:
    def __init__(self,l):
        self.l=l

    def parcer(self):
        if type(self.l)==list:
            for i in self.l:
                print (l)
    def reverse_list(self):
        if type(self.l)==list:
            return self.l[::-1]
                        
print (list_parser)
my_list=list_parser([1,2,3])
print (my_list.l)
print (my_list.reverse_list())



