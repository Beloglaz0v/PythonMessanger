import requests

with open('widget_icon.png', 'rb') as f:
    file = f.read()
response = requests.get("http://127.0.0.1:5000/get_image")
with open('icon.png', 'wb')as f:
    f.write(response.content)
print(response.content)
