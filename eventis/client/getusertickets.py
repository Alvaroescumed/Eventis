import requests

url = 'http://127.0.0.1:8000/api/users/tickets/1'

response = requests.get(url)

print(response)
print(response.json())