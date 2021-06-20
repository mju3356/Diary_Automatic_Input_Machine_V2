# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(392, 180))
        Dialog.setMaximumSize(QtCore.QSize(392, 180))
        Dialog.setSizeIncrement(QtCore.QSize(392, 248))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Diary_Automatic_Input_Machine/lib/resource/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 141))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(13, 30, 56, 12))
        self.label.setObjectName("label")
        self.Id_input_oklms = QtWidgets.QLineEdit(self.groupBox)
        self.Id_input_oklms.setGeometry(QtCore.QRect(40, 20, 131, 31))
        self.Id_input_oklms.setObjectName("Id_input_oklms")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.Pw_input_oklms = QtWidgets.QLineEdit(self.groupBox)
        self.Pw_input_oklms.setGeometry(QtCore.QRect(40, 60, 131, 31))
        self.Pw_input_oklms.setObjectName("Pw_input_oklms")
        self.Pw_input_oklms.setEchoMode(QLineEdit.Password)
        self.Login_btn_oklms = QtWidgets.QPushButton(self.groupBox)
        self.Login_btn_oklms.setGeometry(QtCore.QRect(10, 100, 161, 31))
        self.Login_btn_oklms.setObjectName("Login_btn_oklms")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 20, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(203, 30, 56, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 60, 131, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 10, 181, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.Login_btn_hrdnet = QtWidgets.QPushButton(self.groupBox_3)
        self.Login_btn_hrdnet.setGeometry(QtCore.QRect(10, 100, 161, 31))
        self.Login_btn_hrdnet.setObjectName("Login_btn_hrdnet")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(12, 30, 56, 12))
        self.label_5.setObjectName("label_5")
        self.Id_input_hrdnet = QtWidgets.QLineEdit(self.groupBox_3)
        self.Id_input_hrdnet.setGeometry(QtCore.QRect(40, 20, 131, 31))
        self.Id_input_hrdnet.setObjectName("Id_input_hrdnet")
        self.Pw_input_hrdnet = QtWidgets.QLineEdit(self.groupBox_3)
        self.Pw_input_hrdnet.setGeometry(QtCore.QRect(40, 60, 131, 31))
        self.Pw_input_hrdnet.setObjectName("Pw_input_hrdnet")
        self.Pw_input_hrdnet.setEchoMode(QLineEdit.Password)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_6.setObjectName("label_6")
        self.Login_result_hrdnet = QtWidgets.QLabel(self.groupBox_3)
        self.Login_result_hrdnet.setGeometry(QtCore.QRect(10, 150, 161, 41))
        self.Login_result_hrdnet.setText("")
        self.Login_result_hrdnet.setObjectName("Login_result_hrdnet")
        self.Auto_login_check = QtWidgets.QCheckBox(Dialog)
        self.Auto_login_check.setGeometry(QtCore.QRect(10, 160, 81, 16))
        self.Auto_login_check.setObjectName("Auto_login_check")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "로그인"))
        self.groupBox.setTitle(_translate("Dialog", "OK-LMS"))
        self.label.setText(_translate("Dialog", "ID:"))
        self.label_2.setText(_translate("Dialog", "PW:"))
        self.Login_btn_oklms.setText(_translate("Dialog", "로그인"))
        self.label_3.setText(_translate("Dialog", "PW:"))
        self.label_4.setText(_translate("Dialog", "ID:"))
        self.groupBox_3.setTitle(_translate("Dialog", "HRD-Net"))
        self.Login_btn_hrdnet.setText(_translate("Dialog", "로그인"))
        self.label_5.setText(_translate("Dialog", "ID:"))
        self.label_6.setText(_translate("Dialog", "PW:"))
        self.Auto_login_check.setText(_translate("Dialog", "자동로그인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
