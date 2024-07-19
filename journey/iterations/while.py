price = 100 
while price  > 90 :
    print(f'price = {price}..waiting for price to come down..')
    # price = price - 1
    price -= 1
print(f'buying at {price}')    

# Note:
# lets say i have to add elements in list or delete elements from list for loop is not advisable as it 
# may introduce the bugs 

data = [100,200,300,400,500]
while len(data) > 0:
    last_element = data.pop()

print(data)

