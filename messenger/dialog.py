# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 300)
        self.btn_write = QtWidgets.QPushButton(Dialog)
        self.btn_write.setGeometry(QtCore.QRect(130, 250, 113, 32))
        self.btn_write.setObjectName("btn_write")
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setGeometry(QtCore.QRect(270, 250, 113, 32))
        self.btn_close.setObjectName("btn_close")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 60, 16))
        self.label.setObjectName("label")
        self.lbl_dep_num = QtWidgets.QLabel(Dialog)
        self.lbl_dep_num.setGeometry(QtCore.QRect(220, 10, 60, 16))
        self.lbl_dep_num.setObjectName("lbl_dep_num")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lbl_FIO = QtWidgets.QLabel(Dialog)
        self.lbl_FIO.setGeometry(QtCore.QRect(100, 40, 291, 16))
        self.lbl_FIO.setObjectName("lbl_FIO")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lbl_phone = QtWidgets.QLabel(Dialog)
        self.lbl_phone.setGeometry(QtCore.QRect(100, 90, 281, 16))
        self.lbl_phone.setObjectName("lbl_phone")
        self.label5 = QtWidgets.QLabel(Dialog)
        self.label5.setGeometry(QtCore.QRect(20, 120, 60, 16))
        self.label5.setObjectName("label5")
        self.lbl_email = QtWidgets.QLabel(Dialog)
        self.lbl_email.setGeometry(QtCore.QRect(100, 120, 281, 16))
        self.lbl_email.setObjectName("lbl_email")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 121, 16))
        self.label_4.setObjectName("label_4")
        self.lbl_birthday = QtWidgets.QLabel(Dialog)
        self.lbl_birthday.setGeometry(QtCore.QRect(140, 190, 231, 16))
        self.lbl_birthday.setObjectName("lbl_birthday")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Информация"))
        self.btn_write.setText(_translate("Dialog", "Написать"))
        self.btn_close.setText(_translate("Dialog", "Закрыть"))
        self.label.setText(_translate("Dialog", "Отдел №"))
        self.lbl_dep_num.setText(_translate("Dialog", "1"))
        self.label_2.setText(_translate("Dialog", "ФИО:"))
        self.lbl_FIO.setText(_translate("Dialog", "Петров Петр Петрович"))
        self.label_3.setText(_translate("Dialog", "Телефон:"))
        self.lbl_phone.setText(_translate("Dialog", "89999999999"))
        self.label5.setText(_translate("Dialog", "E-mail:"))
        self.lbl_email.setText(_translate("Dialog", "mail@mail.ru"))
        self.label_4.setText(_translate("Dialog", "Дата рождения:"))
        self.lbl_birthday.setText(_translate("Dialog", "01.01.1991"))
