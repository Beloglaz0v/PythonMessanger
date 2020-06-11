"""
Выпускная квалификационная работа (дипломный проект),
по теме "Разработка программы обмена информацией внутри предприятия"
Название: Messenger.
Разработал: Белоглазов Даниил Александрович, группа ТМП-81.
Дата и номер версии: 26.05.2020 v2.1.
Язык: Python.
Краткое описание:
Данная программа обеспечивает обмен информацией разного вида
между сотрудниками предприятия.
Используемые классы в программе:
MessangerApp - класс для работы с формой авторизации пользователя;
MessangerMainApp - класс для работы с основной формой программы;
FormChangeInfo - класс для работы с формой редактирования личной информации;
ChangePassword - класс для работы с формой изменения пароля;
DialogInfo - класс для работы с  формой дополнительной информации о сотруднике.

"""
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
import auth_form
import changeinfo
import requests
import main_form
import dialog
import time
import json
import os
import datetime
import changepass_form

"""
MessengerApp() - класс для работы с формой авторизации.
Назначение поля класса:
    server - ссылка на сервер.
Назначения метода класса:
    authorization() - авторизация пользователя.

"""
class MessengerApp(QtWidgets.QMainWindow, auth_form.Ui_form_auth):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация дизайна
        self.btn_auth.pressed.connect(self.authorization)
        self.server = 'http://127.0.0.1:5000'

    def authorization(self):
        login = self.txt_login.text()
        passwd = self.txt_pass.text()
        if not login or not passwd:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Заполнены не все поля')
            return
        response = requests.post(self.server + "/auth", json={"login": login, "password": passwd})
        data = response.json()
        print(data)
        if not data['login']:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Пользователь с таким\nлогином не найден')
        elif not data['password']:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Неверный пароль')
        else:
            id = data['id']
            global main_window
            main_window = MessengerMainApp(id)
            main_window.show()
            self.hide()

"""
MessengerMainApp() - класс для работы с основной формой программы.
Формальный параметр:
    user_id - айди пользователя.
Назначение поля класса:
    server - ссылка на сервер;
    id - айди пользователя;
    personal_info - личная информация о пользователе;
    all_employees - список всех сотрудников;
    files_inchat - список файлов в открытом чате;
    employees - результат выборки по сотрудникам;
    dialog_list - список диалогов пользователя;
    dialog_id - айди открытого чата;
    last_message_time - время последнего сообщения;
    last_date - последняя дата сообщений.
Назначения методов класса:
    change_pass() - открытие окна изменения пароля;
    change_info() - открытие окна редактирования информации;
    download() - скачивание выбранного файла;
    choose_file() - отправка файла;
    getUpdates() - получение новых сообщений;
    setLast_message_time() - установка времени последнего сообзения;
    setdiaologs_list() - установка списка диалогов;
    setDialogid() - установка айди открытого чата;
    search_bydep() - поиск по отделу;
    addit_info() - дополнительная информация о сотруднике;
    find_employee() - поиск сотрудников по фамилии;
    open_chat() - открытие чата;
    list_of_employees() - список всех сотрудников;
    filling_1tab() - заполнение первой вкладки;
    filling_2tab() - заполнение второй вкладки;
    filling_depnum() - заполнение списка отделов;
    filling_3tab() - заполнение третьей вкладки;
    send_message() - отправка сообщения;
    get_history() - получение истории сообщений;
    output_messages() - вывод сообщений;
    
"""
class MessengerMainApp(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)  # Инициализация дизайна
        self.server = 'http://127.0.0.1:5000'
        self.id = user_id
        self.personal_info = {}
        self.all_employees = []
        self.files_inchat = {}
        self.employees = []
        self.list_of_employees()
        self.filling_1tab()
        self.filling_2tab()
        self.filling_3tab()
        self.filling_depnum()
        self.tabWidget.currentChanged.connect(self.filling_3tab)
        self.list_dialogs.doubleClicked.connect(self.open_chat)
        self.tabWidget.setCurrentIndex(0)
        self.listWidget.doubleClicked.connect(self.addit_info)
        self.btn_find.pressed.connect(self.find_employee)
        self.btn_file.pressed.connect(self.choose_file)
        self.btn_changeinfo.pressed.connect(self.change_info)
        self.btn_changepass.pressed.connect(self.change_pass)
        self.listWidget_chat.doubleClicked.connect(self.download)
        self.cmbox_depnum.currentIndexChanged.connect(self.search_bydep)
        self.dialog_list = []
        self.dialog_id = -1
        self.count_unread = 0
        self.last_message_time = 0
        self.btn_send_message.pressed.connect(self.send_message)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getUpdates)
        self.timer.start(1000)
        self.last_date = 0

    def change_pass(self):
        changepass = ChangePassword(self.id)
        changepass.show()
        changepass.exec_()

    def change_info(self):
        change_form = FormChangeInfo(self, self.personal_info, self.id)
        change_form.show()
        change_form.exec_()

    def download(self):
        print(self.listWidget_chat.currentRow())
        print(self.files_inchat)
        file = self.files_inchat[self.listWidget_chat.currentRow()]
        response = requests.post(self.server + "/get_file", json={'file_id': file[0]})
        if not os.path.exists('downloads'):
            os.mkdir('downloads')
        with open(f'downloads/{file[1]}', 'wb') as f:
            f.write(response.content)
        QtWidgets.QMessageBox.information(self, 'Успешно', 'Файл сохранен в папку downloads')

    def choose_file(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if file_path and self.dialog_id != -1:
            print(file_path)
            files = {'file': open(file_path, 'rb')}
            message = {'user': self.id, 'dialog_id': self.dialog_id}
            response = requests.post(self.server + "/send_file", data={'data': json.dumps(message)}, files=files)

    def getUpdates(self):
        self.listWidget_chat.repaint()
        if self.tabWidget.currentIndex() == 3 and self.dialog_id != -1:
            response = requests.post(self.server + "/new_messages",
                                     json={'dialog_id': self.dialog_id, 'time': self.last_message_time})
            data = response.json()['messages']
            if data:
                self.output_messages(data)
                self.listWidget_chat.repaint()
                self.last_message_time = float(data[-1]['time'])

    def setLast_message_time(self, time):
        self.last_message_time = float(time)

    def setdiaologs_list(self, list):
        self.dialog_list = list

    def setDialogid(self, id):
        self.dialog_id = int(id)

    def search_bydep(self):
        self.employees.clear()
        dep_num = self.cmbox_depnum.currentText()
        if dep_num != 'Все':
            for el in self.all_employees:
                if el['dep_num'] == int(dep_num):
                    self.employees.append(el)
        else:
            self.employees = self.all_employees[:]
        self.filling_2tab()
        self.listWidget.repaint()

    def addit_info(self):
        dia = DialogInfo(self, self.employees[self.listWidget.currentRow()])
        dia.show()
        dia.exec_()

    def find_employee(self):
        self.cmbox_depnum.setCurrentIndex(0)
        self.cmbox_depnum.repaint()
        surname = self.lineEdit_find.text()
        self.employees.clear()
        for el in self.all_employees:
            if surname.lower() == el['surname'].lower():
                self.employees.append(el)
        if self.employees:
            self.filling_2tab()
        else:
            self.listWidget.clear()
            self.listWidget.addItem("Сотрудников с фамилией " + surname + " не найдено")

    def open_chat(self):
        self.listWidget_chat.clear()
        dia = self.dialog_list[self.list_dialogs.currentRow()]
        self.lbl_FIO_chat.setText(f'{dia["surname"]} {dia["name"]}')
        self.get_history(None, None, dia['dialog_id'])
        self.tabWidget.setCurrentIndex(3)

    def list_of_employees(self):
        response = requests.get(self.server + "/getemployees")
        data = response.json()['employees']
        for element in data:
            if element['id'] == self.id:
                self.personal_info = element
            else:
                self.all_employees.append(element)
        self.employees = self.all_employees[:]

    def filling_1tab(self):
        self.lbl_phone.setText(self.personal_info['phone_num'])
        self.lbl_email.setText(self.personal_info['email'])
        self.lbl_depnum.setText(str(self.personal_info['dep_num']))
        self.lbl_surname.setText(self.personal_info['surname'])
        self.lbl_name.setText(self.personal_info['name'])
        self.lbl_patr.setText(self.personal_info['patronymic'])
        self.lbl_birthday.setText(self.personal_info['birthday'])

    def filling_2tab(self):
        self.listWidget.clear()
        self.listWidget.repaint()
        data = self.employees
        for el in data:
            dep = str(el["dep_num"]) if len(str(el["dep_num"])) == 2 else str(el["dep_num"]) + '  '
            line = f'Одел №{dep} {el["surname"]} {el["name"]} {el["patronymic"]}'
            self.listWidget.addItem(line)

    def filling_depnum(self):
        items = sorted(set(int(el['dep_num']) for el in self.all_employees))
        items = [str(el) for el in items]
        self.cmbox_depnum.addItem('Все')
        self.cmbox_depnum.addItems(items)

    def filling_3tab(self):
        self.list_dialogs.clear()
        response = requests.post(self.server + '/get_dialogs', json={'user': self.id})
        dialogs = response.json()['dialogs']
        self.setdiaologs_list(dialogs)
        if dialogs:
            for dialog in dialogs:
                if dialog['message'] is None:
                    line = f"{dialog['name']} {dialog['surname']} \n {time.strftime('%H:%M', time.localtime(float(dialog['time'])))} файл"
                else:
                    line = f"{dialog['name']} {dialog['surname']} \n {time.strftime('%H:%M', time.localtime(float(dialog['time'])))} {dialog['message']}"
                self.list_dialogs.addItem(line)

    def send_message(self):
        message = self.txt_message.toPlainText()
        self.txt_message.clear()
        self.txt_message.repaint()
        if message:
            response = requests.post(self.server + '/send', json={'user': self.id,
                                                                  'dialog_id': self.dialog_id,
                                                                  'message': message,
                                                                  })
            data = response.json()
            if not data['ok']:
                line = f"Ошибка отправки сообщения\n{message}"
                gg = QtWidgets.QListWidgetItem(line)
                gg.setTextAlignment(2)
                self.listWidget_chat.addItem(gg)

    def get_history(self, user1, user2, dialog_id):
        response = requests.post(self.server + "/history",
                                 json={'user1': user1,
                                       'user2': user2,
                                       'dialog_id': dialog_id
                                       })
        data = response.json()
        print(data)
        self.setDialogid(data['dialog_id'])
        history = data['messages']
        if history:
            self.files_inchat.clear()
            self.output_messages(history)
            self.last_message_time = float(history[-1]['time'])

    def output_messages(self, data):
        for el in data:
            if self.last_date != time.strftime('%d.%m.%Y', time.localtime(float(el['time']))):
                self.last_date = time.strftime('%d.%m.%Y', time.localtime(float(el['time'])))
                line = f"\n{time.strftime('%d.%m.%Y', time.localtime(float(el['time'])))}\n"
                gg = QtWidgets.QListWidgetItem(line)
                gg.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.listWidget_chat.addItem(gg)
            if int(el['dialog_id']) == self.dialog_id:
                if el['user_id'] == self.id:
                    if el['attachment'] is not None:
                        self.files_inchat.update({self.listWidget_chat.count(): [el['attachment_id'], el['attachment']]})
                        line = f"{time.strftime('%H:%M', time.localtime(float(el['time'])))}\nФайл: {el['attachment']}"
                        gg = QtWidgets.QListWidgetItem(line)
                        gg.setTextAlignment(2)
                        font = QtGui.QFont()
                        font.setBold(True)
                        gg.setFont(font)
                    else:
                        line = f"{time.strftime('%H:%M', time.localtime(float(el['time'])))}\n{el['message']} "
                        gg = QtWidgets.QListWidgetItem(line)
                        gg.setTextAlignment(2)
                    self.listWidget_chat.addItem(gg)
                else:
                    if el['attachment'] is not None:
                        self.files_inchat.update({self.listWidget_chat.count(): [el['attachment_id'], el['attachment']]})
                        line = f"{time.strftime('%H:%M', time.localtime(float(el['time'])))}\nФайл: {el['attachment']}"
                        gg = QtWidgets.QListWidgetItem(line)
                        font = QtGui.QFont()
                        font.setBold(True)
                        gg.setFont(font)
                    else:
                        line = f"{time.strftime('%H:%M', time.localtime(float(el['time'])))}\n{el['message']}"
                        gg = QtWidgets.QListWidgetItem(line)
                    self.listWidget_chat.addItem(gg)
                self.listWidget_chat.scrollToBottom()


"""
FormChangeInfo() - класс для работы с формой редактирования личной информации.
Формальные параметры:
    main - объект основного класса;
    personal_info - персональная информация;
    id - айди пользователя.
Назначение поля класса:
    server - ссылка на сервер;
    personal_info - персональная информация;
    new_info - новая информация.
Назначения методов класса:
    filling() - заполнение полей;
    save_new_info() - сохранение новой информации.

"""
class FormChangeInfo(QtWidgets.QDialog, changeinfo.Ui_Dialog):
    def __init__(self, main, personal_info, id):
        super().__init__()
        self.setupUi(self)
        self.main = main
        self.server = 'http://127.0.0.1:5000'
        self.personal_info = personal_info
        self.new_info = {'id': id}
        self.filling()
        self.btn_save.pressed.connect(self.save_new_info)
        self.btn_cancel.pressed.connect(self.close)

    def filling(self):
        self.lineEdit_depnum.setText(str(self.personal_info['dep_num']))
        self.lineEdit_name.setText(self.personal_info['name'])
        self.lineEdit_surname.setText(self.personal_info['surname'])
        self.lineEdit_patronymic.setText(self.personal_info['patronymic'])
        self.lineEdit_phone.setText(self.personal_info['phone_num'])
        self.lineEdit_email.setText(self.personal_info['email'])
        self.dateEdit.setDate(datetime.datetime.strptime(self.personal_info['birthday'], '%d.%m.%Y'))

    def save_new_info(self):
        self.new_info['dep_num'] = self.lineEdit_depnum.text()
        self.new_info['name'] = self.lineEdit_name.text()
        self.new_info['surname'] = self.lineEdit_surname.text()
        self.new_info['patronymic'] = self.lineEdit_patronymic.text()
        self.new_info['phone_num'] = self.lineEdit_phone.text()
        self.new_info['email'] = self.lineEdit_email.text()
        self.new_info['birthday'] = self.dateEdit.text()
        response = requests.post(self.server + '/update_info', json=self.new_info)
        data = response.json()
        if data:
            self.main.personal_info = data['info']
            self.main.filling_1tab()
            self.close()
        else:
            QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Произошла ошибка\nпопробуйте еще раз')


"""
ChangePassword() - класс для работы с формой изменения пароля.
Формальный параметр:
    id - айди пользователя.
Назначение поля класса:
    server - ссылка на сервер;
    new - новый пароль.
Назначение метода класса:
    save_new_pass() - сохранение нового пароля.
"""
class ChangePassword(QtWidgets.QDialog, changepass_form.Ui_Dialog):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.server = 'http://127.0.0.1:5000'
        self.new = {'id': id}
        self.btn_save.pressed.connect(self.save_new_pass)
        self.btn_cancel.pressed.connect(self.close)

    def save_new_pass(self):
        new_pass = self.lineEdit_newpass1.text()
        if new_pass == self.lineEdit_newpass2.text():
            self.new['old_pass'] = self.lineEdit_oldpass.text()
            self.new['new_pass'] = new_pass
            response = requests.post(self.server + '/update_pass', json=self.new)
            if response.json()['ok']:
                self.close()
            else:
                QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Введен неверный старый\nпароль')
                self.lineEdit_oldpass.clear()
        else:
            QtWidgets.QMessageBox.critical(self, 'Ошибка', 'Пароли не совпадают')
            self.lineEdit_newpass1.clear()
            self.lineEdit_newpass2.clear()


"""
DialogInfo() - класс для работы с формой дополнительной информации о сотруднике.
Формальный параметр:
    main - объект основного класса;
    employee - информация о выбранном сотруднике.
Назначение поля класса:
    main - объект основного класса;
    employee - информация о выбранном сотруднике;
    fio - ФИО сотрудника.
Назначение метода класса:
    openchat() - сохранение нового пароля.
"""
class DialogInfo(QtWidgets.QDialog, dialog.Ui_Dialog):
    def __init__(self, main, employee):
        super().__init__()
        self.main = main
        self.setupUi(self)
        self.employee = employee
        self.fio = f"{employee['surname']} {employee['name']} {employee['patronymic']}"
        self.lbl_FIO.setText(self.fio)
        self.lbl_birthday.setText(employee['birthday'])
        self.lbl_email.setText(employee['email'])
        self.lbl_phone.setText(employee['phone_num'])
        self.lbl_dep_num.setText(str(employee['dep_num']))
        self.btn_close.pressed.connect(self.close)
        self.btn_write.pressed.connect(self.openchat)

    def openchat(self):
        self.main.tabWidget.setCurrentIndex(3)
        self.main.lbl_FIO_chat.setText(self.fio)
        self.main.listWidget_chat.clear()
        if self.main.id < self.employee['id']:
            user1 = self.main.id
            user2 = self.employee['id']
        else:
            user1 = self.employee['id']
            user2 = self.main.id
        self.main.get_history(user1, user2, None)
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MessengerApp()
    window.show()
    app.exec_()