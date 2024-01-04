import requests


endpoint = "http://localhost:8000/api/products/" 

get_response = requests.post(endpoint,json={"content":5,'title':"rr"}) 

print(get_response.json())
# print(get_response.json())

# print(get_response.status_code)
