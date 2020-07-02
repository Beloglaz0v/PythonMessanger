# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_auth(object):
    def setupUi(self, form_auth):
        form_auth.setObjectName("form_auth")
        form_auth.resize(297, 233)
        self.btn_auth = QtWidgets.QPushButton(form_auth)
        self.btn_auth.setGeometry(QtCore.QRect(90, 170, 113, 32))
        self.btn_auth.setObjectName("btn_auth")
        self.txt_login = QtWidgets.QLineEdit(form_auth)
        self.txt_login.setGeometry(QtCore.QRect(20, 50, 251, 21))
        self.txt_login.setObjectName("txt_login")
        self.txt_pass = QtWidgets.QLineEdit(form_auth)
        self.txt_pass.setGeometry(QtCore.QRect(20, 120, 251, 21))
        self.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_pass.setObjectName("txt_pass")
        self.label = QtWidgets.QLabel(form_auth)
        self.label.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(form_auth)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 60, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(form_auth)
        QtCore.QMetaObject.connectSlotsByName(form_auth)

    def retranslateUi(self, form_auth):
        _translate = QtCore.QCoreApplication.translate
        form_auth.setWindowTitle(_translate("form_auth", "Авторизация"))
        self.btn_auth.setText(_translate("form_auth", "Войти"))
        self.label.setText(_translate("form_auth", "Логин:"))
        self.label_2.setText(_translate("form_auth", "Пароль:"))
