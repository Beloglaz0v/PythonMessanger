from flask import Flask, request
import time
import datetime
import sqlite3

app = Flask(__name__)


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
        answer = {"id": False, "login": True, "password": True}
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


# @app.route("/getinfo", methods=['POST'])
# def personalinfo():
#     id = request.json['id']
#     conn = sqlite3.connect("messanger.db")
#     cur = conn.cursor()
#     cur.execute(f"SELECT * FROM users WHERE id = {int(id)}")
#     info = cur.fetchall()[0]
#     conn.commit()
#     conn.close()
#     answer = {'phone_num': info[3],
#               'email': info[4],
#               'dep_num': info[5],
#               'surname': info[6],
#               'name': info[7],
#               'patronymic': info[8],
#               'birthday': info[9],
#               }
#     return answer


@app.route("/getemployees")
def allpersonalinfo():
    answer = []
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users ORDER BY dep_num")
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
    return {'employees': answer}


@app.route("/send", methods=['POST'])
def send():

    data = request.json
    print(data)
    user_id = data['user']
    text = data['message']
    dialog_id = data['dialog_id']
    print(data)
    try:
        conn = sqlite3.connect("messanger.db")
        cur = conn.cursor()
        print('norm')
        cur.execute(f'INSERT INTO "main"."messages" ("dialog_id", "user_id", "message", "timedate")'
                    f' VALUES({dialog_id}, {user_id}, \'{text}\', \'{time.time()}\')')

        print('norm')
        conn.commit()
        conn.close()
        print('norm')
        return {'ok': True}

    except Exception as ex:
        print(ex)
        return {'ok': False}


@app.route("/history", methods=['POST'])
def history():
    data = request.json
    print(data)
    answer = []
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id FROM dialogs WHERE user_id = {data['user1']} and user2_id = {data['user2']}")
    dialog = cur.fetchall()
    if dialog:
        cur.execute(f"SELECT * FROM messages WHERE dialog_id = {dialog[0][0]}")
        history = cur.fetchall()
        if history:
            for messange in history:
                mess = {
                    "user_id": messange[1],
                    "message": messange[2],
                    "attachment": messange[3],
                    "time": messange[4],
                }
                answer.append(mess)
    else:
        cur.execute(f'INSERT INTO "main"."dialogs" ("user_id", "user2_id") VALUES({data["user1"]}, {data["user2"]})')
        cur.execute(f"SELECT id FROM dialogs WHERE user_id = {data['user1']} and user2_id = {data['user2']}")
        dialog = cur.fetchall()
        answer = {}
    conn.commit()
    conn.close()
    return {'messages': answer, 'dialog_id': dialog[0][0]}


@app.route("/new_messages", methods=['POST'])
def new_messages():
    data = request.json
    print(data)
    dialog_id = data['dialog_id']
    last_message_time = data['time']
    answer = []
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM messages WHERE dialog_id = {dialog_id} and timedate>{last_message_time}")
    messages = cur.fetchall()
    if messages:
        for message in messages:
            mess = {
                    "dialog_id": message[0],
                    "user_id": message[1],
                    "message": message[2],
                    "attachment": message[3],
                    "time": message[4],
            }
            answer.append(mess)
    return {'messages': answer}


@app.route("/get_dialogs", methods=['POST'])
def get_dialogs():
    data = request.json
    user = data['user']
    answer = []
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"""Select messages.dialog_id, messages.message, x.name, x.surname, max(timedate) from messages join
    (SELECT users.surname as surname, users.name as name, n.d_id as dialog_id FROM USERS JOIN
    (SELECT user_id as id, id as d_id FROM dialogs WHERE user2_id ={user}) as n
    on users.id = n.id
    union
    Select users.surname as surname, users.name, b.d_id as dialog_id FROM users join
    (SELECT user2_id as id, id as d_id FROM dialogs WHERE user_id ={user}) as b
    on users.id = b.id )as x
    on messages.dialog_id = x.dialog_id 
    group by messages.dialog_id""")
    dialogs = cur.fetchall()
    if dialogs:
        for dialog in dialogs:
            dia = {
                    "dialog_id": dialog[0],
                    "message": dialog[1],
                    "name": dialog[2],
                    "surname": dialog[3],
                    "time": dialog[4],
            }
            answer.append(dia)
    return {'dialogs': answer}

app.run()
