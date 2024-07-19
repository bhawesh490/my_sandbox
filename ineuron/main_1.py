class dict_parser:
    def __init__(self,dictionary):
        self.dictionary=dictionary

    def notdict(self):
        if type(self.dictionary)!=dict:
            raise Exception(self.dictionary,"Not a dictionary")
        else:
            return True    
        
    def get_keys(self):
        if self.notdict():
            return list(self.dictionary.keys())
    
    def give_keys(self):
        if type(self.dictionary)==dict:
            return self.dictionary.keys()
        
    def give_values(self):
        if type(self.dictionary)==dict:
            return self.dictionary.values()

            
dictionary=dict_parser({"Bhawesh":1,"Mehta":2})
test="dictionary.get_keys()"
print (eval(test))


