# api key =  cnj98qhr01qkq94gck50cnj98qhr01qkq94gck5g
# Example of requests library 
# --->search terms:python http requests
# --->number of results:5 
# https://www.google.com/search?q=python+http+requests&num=5 
# here + means space 
# using requests to retreive the HTML search results 

import requests
response = requests.get(
    url = 'https://www.google.com/search',
    params = {'q':'python http requests', 'num': 5}

)
# print(response.status_code)
# print(response.reason)
# print(response.text)

response = requests.get('https://www.stackoverflow.com')
print(response)
print(response.reason)

# respone also have headers which are returned from the server
# headers are in form on dictionary
for key,value in response.headers.items():
    print(f"{key}:{value}")

# Note:
# from the above response headers we can see contet-encoding is gzip means server is compressing the data before sending us in respones and browser will have to then decompress it again 
# also notice Content-Type:text/html 

# lets try to use google and use search query parameter
query_params = {
'q':'box8 outlets',
'num':5
}
# num means how many search result i need?

print("Exploring Google\n")
response = requests.get(
    "https://www.google.com",
    params=query_params
)
print(response.status_code,response.reason)
print(response.headers['content-type'])
print(response.headers['content-encoding'])

print("Exploring bad request\n")
response = requests.get("https://www.google.com/some_dummy_page")
print(response.status_code,response.reason)

# Note:
# we do not get an exception when we get 404 response for a bad request 
# we can use exception flow to raise an exception
#we can use if else condtion to raise an exceptio or we can use below method 
try:
    response.raise_for_status()
except:
    print("ok")
# Note
# in all those cases where we dont have error no exception will be raises
print("Exploring good request and checking exception\n")
response = requests.get('https://www.stackoverflow.com')
response.raise_for_status()

print("Concept of cookies")
# Note
# server stores cookies so that whenever we make a request next time it refers that cookies and sends it to the browser
# cookies like headers are also kind of dict objects
# note how are advertisement sent to use.in that case we have to block the cookies
response = requests.get('https://www.nyt.com')
print(response.status_code)
for key,values in response.cookies.items():
    print(f"{key},{value}")

print("####### Working with REST API ##########")

# API_KEY = 'cnj98qhr01qkq94gck50cnj98qhr01qkq94gck5g'
# Note not recommended to keep api key here instead we will store it in secrets.txt file and we will not share this secrets.txt file 
# lets open the secrets txt file 
# from the documentation of finnhub
# Base URL: /api/v1
# Authentication
# All GET request require a token parameter token=apiKey in 
# the URL or a header X-Finnhub-Token : apiKey. 
# You can find your API Key under Dashboard.
# If you are logged in, your API key will be automatically used in the examples so you can copy 
# and paste them as is.


with open('secrets.txt') as f:
    API_KEY = next(f).strip()

print(API_KEY)

base_url =  'https://finnhub.io/api/v1'
url = f'{base_url}/quote'
params = {
'token':API_KEY ,
'symbol': 'AAPL'
}

response = requests.get(url, params)
print(response.reason)

print(response.headers)
# in the headers you can see tthat content-type is json so we can use response.json()
d = response.json()
print("type of d is")
print(type(d)) # note although respone content was in json text but it got desearilized to dict object automatically by request library 

print("Use of headers to pass the token instead of passing the token in params")

headers = {
    'X-Finnhub-Token': API_KEY
}

for symbol in ['AAPL','MSFT','GOOG']:
    try:
        response = requests.get(
            url = url,
            params = {'symbol': symbol},
            headers = headers

        )
    except requests.HTTPError as e:
        print(e)
            