import requests


endpoint = "http://localhost:8000/" 

get_response = requests.post(endpoint,params={"q":'hello'},json={"content":5,'title':"haa"}) # HTTP Request

print(get_response.json())
# print(get_response.json())

# print(get_response.status_code)
