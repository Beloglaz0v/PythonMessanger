import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
import auth_form  # Это наш конвертированный файл дизайна
import requests
import main_form
import dialog
import time


class MessengerApp(QtWidgets.QMainWindow, auth_form.Ui_form_auth):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_auth.pressed.connect(self.authorization)
        #self.btn_auth.pressed.connect(self.testbut)
        self.server = 'http://127.0.0.1:5000'


    def testbut(self):
        global main_window
        main_window = MessengerMainApp(1)
        main_window.show()
        self.hide()

    def authorization(self):
        login = self.txt_login.text()
        passwd = self.txt_pass.text()
        response = requests.post(self.server + "/auth", json={"login": login, "password": passwd})
        data = response.json()
        print(data, login, passwd)
        if not data['login']:
            print('Такого пользователя несуществует')
        elif not data['password']:
            print('Неправильный пароль')
        else:
            id = data['id']
            global main_window
            main_window = MessengerMainApp(id)
            main_window.show()
            self.hide()


class MessengerMainApp(QtWidgets.QMainWindow, main_form.Ui_MainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)  # Инициализация дизайна
        self.server = 'http://127.0.0.1:5000'
        self.id = user_id
        self.personal_info = {}
        self.employees = []
        self.list_of_employees()
        self.filling_1tab()
        self.filling_2tab()
        self.filling_3tab()
        self.tabWidget.currentChanged.connect(self.filling_3tab)
        self.list_dialogs.doubleClicked.connect(self.open_chat)
        self.tabWidget.setCurrentIndex(0)
        self.listWidget.doubleClicked.connect(self.addit_info)
        self.dialog_list = []
        self.dialog_id = -1
        self.count_unread = 0
        self.last_message_time = 0
        self.btn_send_message.pressed.connect(self.send_message)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getUpdates)
        self.timer.start(1000)


    def getUpdates(self):
        if self.tabWidget.currentIndex() == 3 and self.dialog_id != -1:
            response = requests.post(self.server + "/new_messages", json={'dialog_id': self.dialog_id, 'time': self.last_message_time})
            data = response.json()['messages']
            print(data)
            if data:
                    for el in data:
                        if int(el['dialog_id']) == self.dialog_id:
                            if el['user_id'] == self.id:
                                line = f"{time.ctime(float(el['time']))}\n{el['message']} "
                                gg = QtWidgets.QListWidgetItem(line)
                                gg.setTextAlignment(2)
                                self.listWidget_chat.addItem(gg)
                            else:
                                line = f"{time.ctime(float(el['time']))}\n{el['message']}"
                                QtWidgets.QListWidgetItem(line, self.listWidget_chat)
                        else:
                            self.count_unread += 1
                            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dialogs), _translate("MainWindow",
                                                                                             "Диалоги"+ str(self.count_unread)))
                    self.setLast_message_time(data[-1]['time'])

    def setLast_message_time(self, time):
        self.last_message_time = float(time)

    def setdiaologs_list(self, list):
        self.dialog_list = list

    def setDialogid(self, id):
        self.dialog_id = int(id)

    def addit_info(self):
        dia = DialogInfo(self, self.employees[self.listWidget.currentRow()])
        dia.show()
        dia.exec_()


    def open_chat(self):
        dia = self.dialog_list[self.list_dialogs.currentRow()]
        dia['dialog_id']

    def list_of_employees(self):
        response = requests.get(self.server + "/getemployees")
        data = response.json()['employees']
        for element in data:
            if element['id'] == self.id:
                self.personal_info = element
            else:
                self.employees.append(element)

    def filling_1tab(self):
        self.lbl_phone.setText(self.personal_info['phone_num'])
        self.lbl_email.setText(self.personal_info['email'])
        self.lbl_depnum.setText(str(self.personal_info['dep_num']))
        self.lbl_surname.setText(self.personal_info['surname'])
        self.lbl_name.setText(self.personal_info['name'])
        self.lbl_patr.setText(self.personal_info['patronymic'])
        self.lbl_birthday.setText(self.personal_info['birthday'])

    def filling_2tab(self):
        data = self.employees
        for el in data:
            dep = str(el["dep_num"]) if len(str(el["dep_num"])) == 2 else str(el["dep_num"])+'  '
            line = f'Одел №{dep} {el["surname"]} {el["name"]} {el["patronymic"]}'
            self.listWidget.addItem(line)

    def filling_3tab(self):
        self.list_dialogs.clear()
        response = requests.post(self.server + '/get_dialogs', json={'user': self.id})
        dialogs = response.json()['dialogs']
        self.setdiaologs_list(dialogs)
        if dialogs:
            for dialog in dialogs:
                line = f"{dialog['name']} {dialog['surname']} \n {time.ctime(float(dialog['time']))} {dialog['message']}"
                self.list_dialogs.addItem(line)

    def send_message(self):
        message = self.txt_message.toPlainText()
        self.txt_message.clear()
        self.txt_message.repaint()
        if message:
            response = requests.post(self.server+'/send', json={'user': self.id,
                                                                'dialog_id': self.dialog_id,
                                                                'message': message,
                                                                })
            data = response.json()
            if not data['ok']:
                line = f"Ошибка отправки сообщения\n{message}"
                gg = QtWidgets.QListWidgetItem(line)
                gg.setTextAlignment(2)
                self.listWidget_chat.addItem(gg)


class DialogInfo(QtWidgets.QDialog, dialog.Ui_Dialog):
    def __init__(self, main, employee):
        super().__init__()
        self.main = main
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
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
        print({'user1': user1,'user2': user2})
        response = requests.post(self.main.server + "/history",
                                 json={'user1': user1,
                                       'user2': user2
                                       })
        data = response.json()
        print(data)
        self.main.setDialogid(data['dialog_id'])
        history = data['messages']
        if history:
            for el in history:
                if el['user_id'] == self.main.id:
                    line = f"{time.ctime(float(el['time']))}\n{el['message']} "
                    gg = QtWidgets.QListWidgetItem(line)
                    gg.setTextAlignment(2)
                    self.main.listWidget_chat.addItem(gg)
                else:
                    line = f"{time.ctime(float(el['time']))}\n{el['message']}"
                    QtWidgets.QListWidgetItem(line, self.main.listWidget_chat)
            self.main.setLast_message_time(history[-1]['time'])
        self.close()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MessengerApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()
