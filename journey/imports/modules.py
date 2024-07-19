import math 
print(math)
print(math.factorial(3))

import os.path as os_path 
# note here modules inside modules pattern 

from math import sqrt
print(sqrt)

list1 = ['a', 'b']
list2 = ['a']
result_list = list(set(list2) - set(list1))
print(result_list)