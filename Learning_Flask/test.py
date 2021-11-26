import requests 
BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+"helloworld")#want to send a get request to BASE+ hellworld
print(response.json()); #needs a return type of key value pair
#all information that is returned from API must be serializable -> json format {"data": "hello world"}
#json format -> python dictionaries 
# "data" is they key and "hello world is the value"
#status 200
