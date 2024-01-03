import requests


endpoint = "http://localhost:8000/api/products/create" 

get_response = requests.post(endpoint,json={"content":5,'title':"jo"}) 

print(get_response.json())
# print(get_response.json())

# print(get_response.status_code)
