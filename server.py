from flask import Flask, request
import time
import datetime
import sqlite3

app = Flask(__name__)

messages = [
    {"username": "Jack", "text": "Hi", 'time': time.time()},
    {"username": "Polly", "text": "Kokoko", 'time': time.time()},
]
users = [
    {"id": 1, "login": 123, "password": 'qwe'},
    {"id": 2, "login": 1234, "password": 'qweq'},
    {"id": 3, "login": 1235, "password": 'qwee'},
]


@app.route("/auth", methods=['POST'])
def auth():
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id, login, password FROM users")
    users = cur.fetchall()
    data = request.json
    print(data)
    login = data['login']
    password = data['password']
    for user in users:
        print(user)
        answer = {"id": False, "login": True, "password": True}
        print(login, password)
        if user[1] != login:
            answer["login"] = False
        elif user[2] != password:
            answer["password"] = False
        else:
            answer["id"] = user[0]
            break
    conn.commit()
    conn.close()
    return answer


@app.route("/getinfo", methods=['POST'])
def personalinfo():
    id = request.json['id']
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {int(id)}")
    info = cur.fetchall()[0]
    conn.commit()
    conn.close()
    answer = {'phone_num': info[3],
              'email': info[4],
              'dep_num': info[5],
              'surname': info[6],
              'name': info[7],
              'patronymic': info[8],
              'birthday': info[9],
              }
    return answer


@app.route("/getemployees")
def allpersonalinfo():
    answer = []
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users")
    info = cur.fetchall()
    conn.commit()
    conn.close()
    for el in info:
        answer.append({'phone_num': el[3],
                       'email': el[4],
                       'dep_num': el[5],
                       'surname': el[6],
                       'name': el[7],
                       'patronymic': el[8],
                       'birthday': el[9],
                       'id': el[0],
                       })
    print(answer)
    return {'employees': answer}


@app.route("/send", methods=['POST'])
def send():
    """
    request: {"username": "str", "text": "str"}
    response: {"ok": true}
    """
    data = request.json
    username = data['username']
    text = data['text']

    messages.append({'username': username, 'text': text, 'date': time.time()})

    return {'ok': True}


@app.route("/history")
def history():
    return {'messages': messages}


app.run()
