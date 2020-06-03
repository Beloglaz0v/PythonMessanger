# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepass_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(270, 228)
        self.lineEdit_oldpass = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_oldpass.setGeometry(QtCore.QRect(20, 36, 231, 21))
        self.lineEdit_oldpass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_oldpass.setObjectName("lineEdit_oldpass")
        self.lineEdit_newpass1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_newpass1.setGeometry(QtCore.QRect(20, 86, 231, 21))
        self.lineEdit_newpass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_newpass1.setObjectName("lineEdit_newpass1")
        self.lineEdit_newpass2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_newpass2.setGeometry(QtCore.QRect(20, 136, 231, 21))
        self.lineEdit_newpass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_newpass2.setObjectName("lineEdit_newpass2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(23, 16, 201, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(23, 66, 201, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(23, 116, 151, 16))
        self.label_3.setObjectName("label_3")
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(19, 176, 113, 32))
        self.btn_save.setObjectName("btn_save")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(140, 176, 113, 32))
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Изменение пароля"))
        self.label.setText(_translate("Dialog", "Введите старый пароль:"))
        self.label_2.setText(_translate("Dialog", "Введите новый пароль:"))
        self.label_3.setText(_translate("Dialog", "Повторите пароль:"))
        self.btn_save.setText(_translate("Dialog", "Сохранить"))
        self.btn_cancel.setText(_translate("Dialog", "Отменить"))
