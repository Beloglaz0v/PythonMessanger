import requests


response = requests.get("http://127.0.0.1:5000/status")
print(response.json())

response = requests.get("http://127.0.0.1:5000/history")
print(response.json())

response = requests.post("http://127.0.0.1:5000/send", json={"username": "Nick", "text": "hello2"})
print(response.json())

response = requests.get("http://127.0.0.1:5000/history")
print(response.json())
