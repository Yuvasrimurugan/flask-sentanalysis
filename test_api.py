import requests

url = "http://127.0.0.1:5500/analyze"
data = {"text": "I love this new phone!"}

response = requests.post(url, json=data)
print(response.json())