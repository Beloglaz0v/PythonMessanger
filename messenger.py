import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import auth_form  # Это наш конвертированный файл дизайна
import requests
import main_form


class MessengerApp(QtWidgets.QMainWindow, auth_form.Ui_form_auth):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.btn_auth.pressed.connect(self.authorization)
        self.btn_auth.pressed.connect(self.testbut)
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
        self.employees = self.list_of_employees()
        self.filling_1tab()
        self.filling_2tab()
        self.listWidget.doubleClicked.connect(self.addit_info)

    def addit_info(self):
        print(self.employees)
        print(self.listWidget.currentRow())
        print(self.employees[self.listWidget.currentRow()])

    def list_of_employees(self):
        response = requests.get(self.server + "/getemployees")
        data = response.json()
        return data['info']

    def filling_1tab(self):
        for element in self.employees:
            if element['id'] == self.id:
                data = element
                break
        self.lbl_phone.setText(data['phone_num'])
        self.lbl_email.setText(data['email'])
        self.lbl_depnum.setText(str(data['dep_num']))
        self.lbl_surname.setText(data['surname'])
        self.lbl_name.setText(data['name'])
        self.lbl_patr.setText(data['patronymic'])
        self.lbl_birthday.setText(data['birthday'])

    def filling_2tab(self):
        response = requests.get(self.server + "/getallinfo")
        data = response.json()
        self.employees = data['info']
        for el in self.employees:
            line = f'{el["surname"]} {el["name"]} {el["patronymic"]} {el["phone_num"]}'
            self.listWidget.addItem(line)


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MessengerApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()
