import requests

url = 'http://127.0.0.1:8000/api/events/attend/'

response = requests.post(url, params={
    'event_id' : '3',
    'user_mail' : 'alvaro.ture@gmail.com'
})

print(response)
print(response.json())