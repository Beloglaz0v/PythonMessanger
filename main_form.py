# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(747, 494)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 496))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(0, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_PersonalPage = QtWidgets.QWidget()
        self.tab_PersonalPage.setObjectName("tab_PersonalPage")
        self.lbl_surname1 = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_surname1.setGeometry(QtCore.QRect(160, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        self.lbl_surname1.setFont(font)
        self.lbl_surname1.setObjectName("lbl_surname1")
        self.lbl_name1 = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_name1.setGeometry(QtCore.QRect(160, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        self.lbl_name1.setFont(font)
        self.lbl_name1.setObjectName("lbl_name1")
        self.lbl_patr1 = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_patr1.setGeometry(QtCore.QRect(160, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        self.lbl_patr1.setFont(font)
        self.lbl_patr1.setObjectName("lbl_patr1")
        self.lbl_birthday1 = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_birthday1.setGeometry(QtCore.QRect(160, 320, 141, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        self.lbl_birthday1.setFont(font)
        self.lbl_birthday1.setObjectName("lbl_birthday1")
        self.lbl_phone1 = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_phone1.setGeometry(QtCore.QRect(160, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        self.lbl_phone1.setFont(font)
        self.lbl_phone1.setObjectName("lbl_phone1")
        self.lbl_email1 = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_email1.setGeometry(QtCore.QRect(160, 245, 91, 16))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        self.lbl_email1.setFont(font)
        self.lbl_email1.setObjectName("lbl_email1")
        self.lbl_depnum1 = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_depnum1.setGeometry(QtCore.QRect(280, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        self.lbl_depnum1.setFont(font)
        self.lbl_depnum1.setObjectName("lbl_depnum1")
        self.lbl_patr = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_patr.setGeometry(QtCore.QRect(290, 118, 291, 20))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_patr.setFont(font)
        self.lbl_patr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_patr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_patr.setObjectName("lbl_patr")
        self.lbl_phone = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_phone.setGeometry(QtCore.QRect(290, 210, 291, 20))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_phone.setFont(font)
        self.lbl_phone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_phone.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_phone.setObjectName("lbl_phone")
        self.lbl_birthday = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_birthday.setGeometry(QtCore.QRect(290, 320, 291, 20))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_birthday.setFont(font)
        self.lbl_birthday.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_birthday.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_birthday.setObjectName("lbl_birthday")
        self.lbl_surname = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_surname.setGeometry(QtCore.QRect(290, 58, 291, 20))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_surname.setFont(font)
        self.lbl_surname.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_surname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_surname.setObjectName("lbl_surname")
        self.lbl_email = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_email.setGeometry(QtCore.QRect(290, 243, 291, 20))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_email.setFont(font)
        self.lbl_email.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_email.setObjectName("lbl_email")
        self.lbl_name = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_name.setGeometry(QtCore.QRect(290, 88, 291, 20))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_name.setFont(font)
        self.lbl_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_depnum = QtWidgets.QLabel(self.tab_PersonalPage)
        self.lbl_depnum.setGeometry(QtCore.QRect(420, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(18)
        self.lbl_depnum.setFont(font)
        self.lbl_depnum.setObjectName("lbl_depnum")
        self.btn_changeinfo = QtWidgets.QPushButton(self.tab_PersonalPage)
        self.btn_changeinfo.setGeometry(QtCore.QRect(150, 401, 181, 31))
        self.btn_changeinfo.setObjectName("btn_changeinfo")
        self.btn_changepass = QtWidgets.QPushButton(self.tab_PersonalPage)
        self.btn_changepass.setGeometry(QtCore.QRect(410, 401, 181, 31))
        self.btn_changepass.setObjectName("btn_changepass")
        icon = QtGui.QIcon.fromTheme("Lol")
        self.tabWidget.addTab(self.tab_PersonalPage, icon, "")
        self.tab_employees = QtWidgets.QWidget()
        self.tab_employees.setObjectName("tab_employees")
        self.cmbox_depnum = QtWidgets.QComboBox(self.tab_employees)
        self.cmbox_depnum.setGeometry(QtCore.QRect(130, 422, 71, 26))
        self.cmbox_depnum.setObjectName("cmbox_depnum")
        self.label = QtWidgets.QLabel(self.tab_employees)
        self.label.setGeometry(QtCore.QRect(10, 425, 121, 16))
        self.label.setObjectName("label")
        self.btn_find = QtWidgets.QPushButton(self.tab_employees)
        self.btn_find.setGeometry(QtCore.QRect(630, 419, 113, 32))
        self.btn_find.setObjectName("btn_find")
        self.listWidget = QtWidgets.QListWidget(self.tab_employees)
        self.listWidget.setGeometry(QtCore.QRect(-5, 11, 751, 391))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.listWidget.setFont(font)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setBatchSize(100)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.tab_employees)
        self.label_2.setGeometry(QtCore.QRect(220, 425, 221, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_find = QtWidgets.QLineEdit(self.tab_employees)
        self.lineEdit_find.setGeometry(QtCore.QRect(350, 423, 271, 21))
        self.lineEdit_find.setObjectName("lineEdit_find")
        icon = QtGui.QIcon.fromTheme("Lol")
        self.tabWidget.addTab(self.tab_employees, icon, "")
        self.tab_dialogs = QtWidgets.QWidget()
        self.tab_dialogs.setObjectName("tab_dialogs")
        self.list_dialogs = QtWidgets.QListWidget(self.tab_dialogs)
        self.list_dialogs.setGeometry(QtCore.QRect(0, 10, 751, 461))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.list_dialogs.setFont(font)
        self.list_dialogs.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.list_dialogs.setTextElideMode(QtCore.Qt.ElideRight)
        self.list_dialogs.setViewMode(QtWidgets.QListView.ListMode)
        self.list_dialogs.setBatchSize(100)
        self.list_dialogs.setObjectName("list_dialogs")
        self.tabWidget.addTab(self.tab_dialogs, "")
        self.tab_chat = QtWidgets.QWidget()
        self.tab_chat.setObjectName("tab_chat")
        self.listWidget_chat = QtWidgets.QListWidget(self.tab_chat)
        self.listWidget_chat.setGeometry(QtCore.QRect(0, 40, 741, 331))
        self.listWidget_chat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_chat.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidget_chat.setObjectName("listWidget_chat")
        self.txt_message = QtWidgets.QTextEdit(self.tab_chat)
        self.txt_message.setGeometry(QtCore.QRect(100, 380, 511, 71))
        self.txt_message.setObjectName("txt_message")
        self.btn_send_message = QtWidgets.QPushButton(self.tab_chat)
        self.btn_send_message.setGeometry(QtCore.QRect(620, 390, 111, 51))
        self.btn_send_message.setObjectName("btn_send_message")
        self.lbl_FIO_chat = QtWidgets.QLabel(self.tab_chat)
        self.lbl_FIO_chat.setGeometry(QtCore.QRect(30, 10, 691, 16))
        self.lbl_FIO_chat.setObjectName("lbl_FIO_chat")
        self.btn_file = QtWidgets.QPushButton(self.tab_chat)
        self.btn_file.setGeometry(QtCore.QRect(10, 377, 81, 81))
        self.btn_file.setObjectName("btn_file")
        self.tabWidget.addTab(self.tab_chat, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_surname1.setText(_translate("MainWindow", "Фамилия"))
        self.lbl_name1.setText(_translate("MainWindow", "Имя"))
        self.lbl_patr1.setText(_translate("MainWindow", "Отчество"))
        self.lbl_birthday1.setText(_translate("MainWindow", "Дата рождения"))
        self.lbl_phone1.setText(_translate("MainWindow", "Номер телефона"))
        self.lbl_email1.setText(_translate("MainWindow", "E-mail"))
        self.lbl_depnum1.setText(_translate("MainWindow", "Номер отдела"))
        self.lbl_patr.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_phone.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_birthday.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_surname.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_email.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_name.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_depnum.setText(_translate("MainWindow", "1"))
        self.btn_changeinfo.setText(_translate("MainWindow", "Изменить информацию"))
        self.btn_changepass.setText(_translate("MainWindow", "Изменить пароль"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_PersonalPage), _translate("MainWindow", "ЛИЧНЫЙ КАБИНЕТ"))
        self.label.setText(_translate("MainWindow", "Поиск по отделу"))
        self.btn_find.setText(_translate("MainWindow", "Найти"))
        self.label_2.setText(_translate("MainWindow", "Поиск по фамилии"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_employees), _translate("MainWindow", "СОТРУДНИКИ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dialogs), _translate("MainWindow", "Диалоги"))
        self.btn_send_message.setText(_translate("MainWindow", "Отправить"))
        self.lbl_FIO_chat.setText(_translate("MainWindow", "ФИО"))
        self.btn_file.setText(_translate("MainWindow", "Файл"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_chat), _translate("MainWindow", "Чат"))
