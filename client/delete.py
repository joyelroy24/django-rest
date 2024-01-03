import requests


endpoint = "http://localhost:8000/api/products/delete/2" 

get_response = requests.delete(endpoint) # HTTP Request

print(get_response.status_code)
# print(get_response.json())

# print(get_response.status_code)
