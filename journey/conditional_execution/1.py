import boto3

ask_price = 100 

if ask_price > 50:
    volume = 50 
else:
    volume = 80 

print(volume)

volume = 50 if ask_price > 50 else 80 
print(volume)


