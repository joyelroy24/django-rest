import requests


endpoint = "http://localhost:8000/api?j=joyel" 

get_response = requests.get(endpoint,params={"q":'hello'},json={"hai":5,'title':"haa"}) # HTTP Request

print(get_response.json())
# print(get_response.json())

# print(get_response.status_code)
