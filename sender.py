import requests

print('Enter username:')
username = input()
print('Enter password')
password = input()

while True:
    print('Enter message:')
    text = input()

    response = requests.post(
        'https://127.0.0.1:5000/send',
        json={"username": username, "password": password, "text": text}
    )
    if not response.json()['ok']:
        print("Access denide")
        break
