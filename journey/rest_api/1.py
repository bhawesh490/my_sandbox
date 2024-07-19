import json
json_string = '''
    {
    "name":"bhawesh",
    "age":30,
    "phoneNumbers":[{
    "type":"home",
    "number":"8347045789"},
    {
    "type":"work",
    "number":"8347045788"
    }],
    "spouse":null,
    "children":[],
    "employed":true
    }
'''
# deserailise
dict = json.loads(json_string)
print(dict)
# observe how null changes to None ,true changed to True
# serialise it back means series of characters
json_str_1 = json.dumps(dict)
print(json_str_1)
# you can see that there are no whitespaces and when converting to json_string.its good when data is 
# transmitted without extra spaces
# we can put indeneation like
json_str_1 = json.dumps(dict, indent=2)
print(json_str_1)


#######################################################################################
# python dict has lot of datatype which cannot be serialised by default example
from datetime import datetime

d = {
    "name":"Isaac Newton",
    "dob":datetime(1643, 1, 4)
}



print(d)

# we cannot have a dict of below format to pass keys must be str,int,float,bool or None
# d = {
#     datetime(1643, 1, 4):"Isaac Newton",
#     "dob":datetime(1643, 1, 4)
# }


# let's try to serailise this dictionary into json_string 
# print(json.dumps(d))

def my_encoder(obj):
    print(f"my encoder ({obj}) is called...")
    if isinstance(obj, datetime):
        return obj.isoformat()
    # it will come to the raise part if if condtions is false otherwise if its true it will return 
# a values and stop there itself
    raise TypeError

print(json.dumps(d, default=my_encoder))









       