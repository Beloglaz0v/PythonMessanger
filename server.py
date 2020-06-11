"""
Выпускная квалификационная работа (дипломный проект),
по теме "Разработка программы обмена информацией внутри предприятия"
Название: Server.
Разработал: Белоглазов Даниил Александрович, группа ТМП-81.
Дата и номер версии: 26.05.2020 v2.1.
Язык: Python.
Краткое описание:
Данная программа обеспечивает обмен информацией разного вида
между сотрудниками предприятия.
Функции используемые в программе:
auth() - авторизация;
allpersonalinfo() - информация о пользователях;
get_file() - отправка файла;
send_file() - получение файла;
send() - обработка сообщения;
history() - история сообщений;
new_messages() - новые сообщения;
get_dialogs() - список диалогов;
update_info() - изменение личной информации;
update_pass() - изменение пароля.
"""
from flask import Flask, request, send_from_directory
import time
import sqlite3
import os
import json

app = Flask(__name__)

"""
auth() - функция авторизации.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    users - список пользователей;
    login - логин;
    password - пароль;
    answer - ответ клиенту.
"""
@app.route("/auth", methods=['POST'])
def auth():
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id, login, password FROM users")
    users = cur.fetchall()
    data = request.json
    login = data['login']
    password = data['password']
    for user in users:
        answer = {"id": False, "login": True, "password": True}
        if user[1] == login and user[2] == password:
            answer["login"] = True
            answer["id"] = user[0]
            break
        elif user[1] != login:
            answer["login"] = False
            answer["password"] = False
        elif user[2] != password:
            answer["password"] = False
            break
    conn.commit()
    conn.close()
    return answer


"""
allpersonalinfo() - информация о пользователях.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    info - список информации о пользователях;
    answer - ответ клиенту.
"""
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


"""
get_file() - отправка файла.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    id - айди файла;
    file_name - имя файла.
"""
@app.route("/get_file", methods=['POST'])
def get_file():
    data = request.json
    id = data['file_id']
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM Files WHERE file_id ={int(id)}')
    file_name = cur.fetchall()[0][1]
    conn.commit()
    conn.close()
    return send_from_directory('files/' + str(id), file_name)


"""
send_file() - получение файла.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    file - файл;
    user_id - айди пользователя;
    dialog_id - айди диалога;
    id - айди файла;
    file_path - путь к файлу;
    file_name - имя файла;
    answer - ответ клиенту.
"""
@app.route("/send_file", methods=['POST'])
def send_file():
    file = request.files['file']
    data = json.loads(request.form['data'])
    user_id = data['user']
    dialog_id = data['dialog_id']
    if file:
        conn = sqlite3.connect("messanger.db")
        cur = conn.cursor()
        cur.execute(f'SELECT MAX(file_id) FROM Files')
        id = cur.fetchall()[0][0] + 1
        file_path = 'files/' + str(id)
        file_name = file.filename
        cur.execute(f'INSERT INTO "main"."files" ("file_id", "file") VALUES ({int(id)}, \'{file_name}\')')
        os.mkdir(file_path)
        file.save(os.path.join(file_path, file_name))
        cur.execute(f'INSERT INTO "main"."messages" ("dialog_id", "user_id", "attachment", "timedate")'
                    f' VALUES({dialog_id}, {user_id}, {id}, \'{time.time()}\')')
        conn.commit()
        conn.close()
    return 'ok'

"""
send() - обработка сообщения.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    text - текст сообщения;
    dialog_id - айди диалога;
    user_id - айди пользователя;
    answer - ответ клиенту.
"""
@app.route("/send", methods=['POST'])
def send():
    data = request.json
    user_id = data['user']
    text = data['message']
    dialog_id = data['dialog_id']
    try:
        conn = sqlite3.connect("messanger.db")
        cur = conn.cursor()
        cur.execute(f'INSERT INTO "main"."messages" ("dialog_id", "user_id", "message", "timedate")'
                    f' VALUES({dialog_id}, {user_id}, \'{text}\', \'{time.time()}\')')
        conn.commit()
        conn.close()
        return {'ok': True}
    except Exception as ex:
        return {'ok': False}


"""
history() - функция возвращающая историю сообщений.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    dialog - информация о диалоге;
    dialog_id - айди диалога;
    history - история сообщений
    attachment - вложения сообщения;
    messange - сообщение;
    answer - ответ клиенту.
"""
@app.route("/history", methods=['POST'])
def history():
    data = request.json
    answer = []
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    if data['dialog_id'] is None:
        cur.execute(f"SELECT id FROM dialogs WHERE user_id = {data['user1']} and user2_id = {data['user2']}")
        dialog = cur.fetchall()
        if dialog:
            dialog_id = dialog[0][0]
        else:
            cur.execute(
                f'INSERT INTO "main"."dialogs" ("user_id", "user2_id") VALUES({data["user1"]}, {data["user2"]})')
            cur.execute(f"SELECT id FROM dialogs WHERE user_id = {data['user1']} and user2_id = {data['user2']}")
            dialog = cur.fetchall()
            dialog_id = dialog[0][0]
            answer = {}
    else:
        dialog_id = data['dialog_id']
    cur.execute(f"SELECT * FROM messages WHERE dialog_id = {dialog_id} order by timedate")
    history = cur.fetchall()
    if history:
        for messange in history:
            if messange[3]:
                cur.execute(f"SELECT * FROM files WHERE file_id = {messange[3]}")
                attachment = cur.fetchall()[0]
                mess = {
                    "dialog_id": messange[0],
                    "user_id": messange[1],
                    "message": messange[2],
                    "attachment": attachment[1],
                    "attachment_id": attachment[0],
                    "time": messange[4],
                }
            else:
                mess = {
                    "dialog_id": messange[0],
                    "user_id": messange[1],
                    "message": messange[2],
                    "attachment": None,
                    "time": messange[4],
                }
            answer.append(mess)
    conn.commit()
    conn.close()
    return {'messages': answer, 'dialog_id': dialog_id}


"""
new_messages() - функция возвращающая новые сообщения.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    last_message_time - время последнего сообщения;
    dialog_id - айди диалога;
    messages - список сообщений;
    attachment - вложения сообщения;
    message - сообщение;
    answer - ответ клиенту.
"""
@app.route("/new_messages", methods=['POST'])
def new_messages():
    data = request.json
    dialog_id = data['dialog_id']
    last_message_time = data['time']
    answer = []
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM messages WHERE dialog_id = {dialog_id} and timedate>{last_message_time}")
    messages = cur.fetchall()
    if messages:
        for message in messages:
            if message[3]:
                cur.execute(f"SELECT * FROM files WHERE file_id = {message[3]}")
                attachment = cur.fetchall()[0]
                mess = {
                    "dialog_id": message[0],
                    "user_id": message[1],
                    "message": message[2],
                    "attachment": attachment[1],
                    "attachment_id": attachment[0],
                    "time": message[4],
                }
            else:
                mess = {
                    "dialog_id": message[0],
                    "user_id": message[1],
                    "message": message[2],
                    "attachment": None,
                    "time": message[4],
                }
            answer.append(mess)
    print(answer)
    return {'messages': answer}


"""
get_dialogs() - функция возвращающая список диалогов.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    dialogs - список диалогов;
    dia - новое сформированное сообщение;
    answer - ответ клиенту.
"""
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
    conn.commit()
    conn.close()
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


"""
update_info() - функция изменяющая личную информацию.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    info - данные пользователя;
    answer - ответ клиенту.
"""
@app.route("/update_info", methods=['POST'])
def update_info():
    data = request.json
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE users "
                f"SET name = '{data['name']}', surname = '{data['surname']}', patronymic = '{data['patronymic']}', dep_num = {data['dep_num']}, phone_num = '{data['phone_num']}', email = '{data['email']}', birthday = '{data['birthday']}' "
                f"WHERE id = {data['id']}")
    cur.execute(f"SELECT * FROM users WHERE id = {data['id']}")
    info = cur.fetchall()[0]
    answer = {'phone_num': info[3],
              'email': info[4],
              'dep_num': info[5],
              'surname': info[6],
              'name': info[7],
              'patronymic': info[8],
              'birthday': info[9],
              'id': info[0],
              }
    conn.commit()
    conn.close()
    return {'info': answer}


"""
update_pass() - функция изменяющая пароль.
Локальные переменные:
    conn - подключение к бд;
    cur - переменная для осуществления запросов к бд;
    data - данные полученные от клиента;
    passwd - парол.
"""
@app.route("/update_pass", methods=['POST'])
def update_pass():
    data = request.json
    conn = sqlite3.connect("messanger.db")
    cur = conn.cursor()
    cur.execute(f"SELECT password FROM users WHERE id = {data['id']}")
    passwd = cur.fetchall()[0][0]
    if passwd == data['old_pass']:
        cur.execute(f"UPDATE users "
                    f"SET password = '{data['new_pass']}' "
                    f"WHERE id = {data['id']}")
    else:
        return {'ok': False}
    conn.commit()
    conn.close()
    return {'ok': True}


app.run()
