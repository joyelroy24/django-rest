import requests


endpoint = "http://localhost:8000/api/products/update/1" 

get_response = requests.put(endpoint,json={"content":'update','title':"test"}) # HTTP Request

print(get_response.json())
# print(get_response.json())

# print(get_response.status_code)
