import requests

url = 'http://127.0.0.1:8000/api/events/Madrid'

response = requests.get(url)

print(response)
print(response.json())