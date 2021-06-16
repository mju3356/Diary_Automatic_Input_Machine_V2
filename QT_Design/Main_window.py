# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 444)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(770, 444))
        MainWindow.setMaximumSize(QtCore.QSize(770, 444))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./lib/resources/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, -76, 1051, 211))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./lib/resources/Design_logo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 70, 56, 12))
        self.label_2.setObjectName("label_2")
        self.Login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Login_btn.setGeometry(QtCore.QRect(650, 10, 111, 31))
        self.Login_btn.setObjectName("Login_btn")
        self.User_info = QtWidgets.QLineEdit(self.centralwidget)
        self.User_info.setGeometry(QtCore.QRect(410, 10, 231, 31))
        self.User_info.setReadOnly(True)
        self.User_info.setObjectName("User_info")
        self.Tap_dis = QtWidgets.QTabWidget(self.centralwidget)
        self.Tap_dis.setGeometry(QtCore.QRect(10, 100, 751, 331))
        self.Tap_dis.setObjectName("Tap_dis")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.NotEnter_check_btn = QtWidgets.QPushButton(self.tab_3)
        self.NotEnter_check_btn.setGeometry(QtCore.QRect(650, 220, 91, 71))
        self.NotEnter_check_btn.setObjectName("NotEnter_check_btn")
        self.Not_enter_diary_list = QtWidgets.QListWidget(self.tab_3)
        self.Not_enter_diary_list.setGeometry(QtCore.QRect(10, 10, 631, 281))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Not_enter_diary_list.setFont(font)
        self.Not_enter_diary_list.setObjectName("Not_enter_diary_list")
        self.Tap_dis.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 301, 291))
        self.groupBox.setObjectName("groupBox")
        self.Weeknum_1 = QtWidgets.QSpinBox(self.groupBox)
        self.Weeknum_1.setGeometry(QtCore.QRect(221, 250, 42, 22))
        self.Weeknum_1.setObjectName("Weeknum_1")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(266, 252, 31, 20))
        self.label_9.setObjectName("label_9")
        self.Diary_input = QtWidgets.QPlainTextEdit(self.tab)
        self.Diary_input.setGeometry(QtCore.QRect(330, 90, 391, 161))
        self.Diary_input.setReadOnly(False)
        self.Diary_input.setObjectName("Diary_input")
        self.CalendarWidget_1 = QtWidgets.QCalendarWidget(self.tab)
        self.CalendarWidget_1.setGeometry(QtCore.QRect(20, 50, 281, 191))
        self.CalendarWidget_1.setObjectName("CalendarWidget_1")
        self.Diary_clear_btn = QtWidgets.QPushButton(self.tab)
        self.Diary_clear_btn.setGeometry(QtCore.QRect(330, 260, 161, 31))
        self.Diary_clear_btn.setObjectName("Diary_clear_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 70, 411, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Send_diary_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.Send_diary_btn.setGeometry(QtCore.QRect(180, 190, 131, 31))
        self.Send_diary_btn.setObjectName("Send_diary_btn")
        self.Send_oklms = QtWidgets.QCheckBox(self.groupBox_2)
        self.Send_oklms.setGeometry(QtCore.QRect(320, 186, 81, 20))
        self.Send_oklms.setObjectName("Send_oklms")
        self.Send_hrdnet = QtWidgets.QCheckBox(self.groupBox_2)
        self.Send_hrdnet.setGeometry(QtCore.QRect(320, 206, 81, 20))
        self.Send_hrdnet.setObjectName("Send_hrdnet")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_10.setGeometry(QtCore.QRect(320, 10, 411, 51))
        self.groupBox_10.setObjectName("groupBox_10")
        self.Class_content_dis = QtWidgets.QTextEdit(self.groupBox_10)
        self.Class_content_dis.setGeometry(QtCore.QRect(10, 13, 351, 31))
        self.Class_content_dis.setReadOnly(True)
        self.Class_content_dis.setObjectName("Class_content_dis")
        self.Class_content_check_btn = QtWidgets.QPushButton(self.groupBox_10)
        self.Class_content_check_btn.setGeometry(QtCore.QRect(364, 13, 41, 31))
        self.Class_content_check_btn.setObjectName("Class_content_check_btn")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.Diary_input.raise_()
        self.CalendarWidget_1.raise_()
        self.Diary_clear_btn.raise_()
        self.groupBox_10.raise_()
        self.Tap_dis.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 511, 16))
        self.label_7.setObjectName("label_7")
        self.CalendarWidget_2 = QtWidgets.QCalendarWidget(self.tab_4)
        self.CalendarWidget_2.setGeometry(QtCore.QRect(20, 30, 281, 191))
        self.CalendarWidget_2.setObjectName("CalendarWidget_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 10, 301, 261))
        self.groupBox_6.setObjectName("groupBox_6")
        self.Weeknum_2 = QtWidgets.QSpinBox(self.groupBox_6)
        self.Weeknum_2.setGeometry(QtCore.QRect(220, 223, 42, 22))
        self.Weeknum_2.setObjectName("Weeknum_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(265, 225, 31, 20))
        self.label_10.setObjectName("label_10")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_7.setGeometry(QtCore.QRect(320, 10, 411, 261))
        self.groupBox_7.setObjectName("groupBox_7")
        self.Send_autodiary_btn = QtWidgets.QPushButton(self.groupBox_7)
        self.Send_autodiary_btn.setGeometry(QtCore.QRect(180, 220, 211, 31))
        self.Send_autodiary_btn.setObjectName("Send_autodiary_btn")
        self.Diar_create_btn = QtWidgets.QPushButton(self.groupBox_7)
        self.Diar_create_btn.setGeometry(QtCore.QRect(10, 220, 161, 31))
        self.Diar_create_btn.setObjectName("Diar_create_btn")
        self.Diar_create_btn.raise_()
        self.Send_autodiary_btn.raise_()
        self.Autodiary_input_2 = QtWidgets.QPlainTextEdit(self.tab_4)
        self.Autodiary_input_2.setGeometry(QtCore.QRect(330, 30, 391, 191))
        self.Autodiary_input_2.setObjectName("Autodiary_input_2")
        self.groupBox_6.raise_()
        self.label_7.raise_()
        self.CalendarWidget_2.raise_()
        self.groupBox_7.raise_()
        self.Autodiary_input_2.raise_()
        self.Tap_dis.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(10, 280, 511, 16))
        self.label_8.setObjectName("label_8")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 301, 261))
        self.groupBox_8.setObjectName("groupBox_8")
        self.Weeknum_3 = QtWidgets.QSpinBox(self.groupBox_8)
        self.Weeknum_3.setGeometry(QtCore.QRect(220, 223, 42, 22))
        self.Weeknum_3.setObjectName("Weeknum_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.label_11.setGeometry(QtCore.QRect(265, 225, 31, 20))
        self.label_11.setObjectName("label_11")
        self.CalendarWidget_4 = QtWidgets.QCalendarWidget(self.tab_5)
        self.CalendarWidget_4.setGeometry(QtCore.QRect(20, 30, 281, 191))
        self.CalendarWidget_4.setObjectName("CalendarWidget_4")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_9.setGeometry(QtCore.QRect(320, 10, 411, 261))
        self.groupBox_9.setObjectName("groupBox_9")
        self.Excel_create_btn = QtWidgets.QPushButton(self.groupBox_9)
        self.Excel_create_btn.setGeometry(QtCore.QRect(10, 220, 321, 31))
        self.Excel_create_btn.setObjectName("Excel_create_btn")
        self.Association_input = QtWidgets.QPlainTextEdit(self.groupBox_9)
        self.Association_input.setGeometry(QtCore.QRect(10, 20, 321, 191))
        self.Association_input.setObjectName("Association_input")
        self.Excel_settings_btn = QtWidgets.QPushButton(self.groupBox_9)
        self.Excel_settings_btn.setGeometry(QtCore.QRect(340, 140, 61, 31))
        self.Excel_settings_btn.setObjectName("Excel_settings_btn")
        self.Excel_print_btn = QtWidgets.QPushButton(self.groupBox_9)
        self.Excel_print_btn.setGeometry(QtCore.QRect(340, 180, 61, 31))
        self.Excel_print_btn.setObjectName("Excel_print_btn")
        self.Excel_open_btn = QtWidgets.QPushButton(self.groupBox_9)
        self.Excel_open_btn.setGeometry(QtCore.QRect(340, 220, 61, 31))
        self.Excel_open_btn.setObjectName("Excel_open_btn")
        self.Tap_dis.addTab(self.tab_5, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 301, 291))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 0, 301, 291))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(266, 252, 31, 20))
        self.label_21.setObjectName("label_21")
        self.Weeknum_4 = QtWidgets.QSpinBox(self.groupBox_3)
        self.Weeknum_4.setGeometry(QtCore.QRect(221, 250, 42, 22))
        self.Weeknum_4.setObjectName("Weeknum_4")
        self.CalendarWidget_3 = QtWidgets.QCalendarWidget(self.widget)
        self.CalendarWidget_3.setGeometry(QtCore.QRect(20, 50, 281, 191))
        self.CalendarWidget_3.setObjectName("CalendarWidget_3")
        self.Diary_oklms = QtWidgets.QPlainTextEdit(self.widget)
        self.Diary_oklms.setGeometry(QtCore.QRect(330, 30, 191, 231))
        self.Diary_oklms.setObjectName("Diary_oklms")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setGeometry(QtCore.QRect(320, 10, 411, 291))
        self.groupBox_5.setObjectName("groupBox_5")
        self.Diary_hrdnet = QtWidgets.QPlainTextEdit(self.groupBox_5)
        self.Diary_hrdnet.setGeometry(QtCore.QRect(210, 20, 191, 231))
        self.Diary_hrdnet.setObjectName("Diary_hrdnet")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(70, 260, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(270, 260, 71, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_5.raise_()
        self.groupBox_3.raise_()
        self.CalendarWidget_3.raise_()
        self.Diary_oklms.raise_()
        self.Tap_dis.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.label_5.setObjectName("label_5")
        self.Date_setting = QtWidgets.QDateEdit(self.tab_2)
        self.Date_setting.setGeometry(QtCore.QRect(110, 40, 151, 31))
        self.Date_setting.setObjectName("Date_setting")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 40, 81, 31))
        self.label_6.setObjectName("label_6")
        self.Date_check = QtWidgets.QLabel(self.tab_2)
        self.Date_check.setGeometry(QtCore.QRect(30, 70, 201, 41))
        self.Date_check.setObjectName("Date_check")
        self.Save_setting_btn = QtWidgets.QPushButton(self.tab_2)
        self.Save_setting_btn.setGeometry(QtCore.QRect(650, 280, 91, 21))
        self.Save_setting_btn.setObjectName("Save_setting_btn")
        self.Op_pro_dis_check = QtWidgets.QCheckBox(self.tab_2)
        self.Op_pro_dis_check.setGeometry(QtCore.QRect(20, 110, 111, 21))
        self.Op_pro_dis_check.setObjectName("Op_pro_dis_check")
        self.Tap_dis.addTab(self.tab_2, "")
        self.Cur_list = QtWidgets.QComboBox(self.centralwidget)
        self.Cur_list.setGeometry(QtCore.QRect(520, 50, 241, 31))
        self.Cur_list.setObjectName("Cur_list")
        self.Show_week = QtWidgets.QLineEdit(self.centralwidget)
        self.Show_week.setGeometry(QtCore.QRect(410, 50, 101, 31))
        self.Show_week.setReadOnly(True)
        self.Show_week.setObjectName("Show_week")
        self.label.raise_()
        self.Tap_dis.raise_()
        self.label_2.raise_()
        self.Login_btn.raise_()
        self.User_info.raise_()
        self.Cur_list.raise_()
        self.Show_week.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tap_dis.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "훈련일지자동입력기"))
        self.label_2.setText(_translate("MainWindow", "V2.0"))
        self.Login_btn.setText(_translate("MainWindow", "로그인"))
        self.User_info.setText(_translate("MainWindow", "로그인이 필요합니다."))
        self.NotEnter_check_btn.setText(_translate("MainWindow", "조회"))
        self.Tap_dis.setTabText(self.Tap_dis.indexOf(self.tab_3), _translate("MainWindow", "미입력일지조회"))
        self.groupBox.setTitle(_translate("MainWindow", "입력할 주차 설정"))
        self.label_9.setText(_translate("MainWindow", "주차"))
        self.Diary_clear_btn.setText(_translate("MainWindow", "지우기"))
        self.groupBox_2.setTitle(_translate("MainWindow", "일지 입력"))
        self.Send_diary_btn.setText(_translate("MainWindow", "일지 전송"))
        self.Send_oklms.setText(_translate("MainWindow", "OK-LMS"))
        self.Send_hrdnet.setText(_translate("MainWindow", "HRD-Net"))
        self.groupBox_10.setTitle(_translate("MainWindow", "수업내용"))
        self.Class_content_check_btn.setText(_translate("MainWindow", "조회"))
        self.Tap_dis.setTabText(self.Tap_dis.indexOf(self.tab), _translate("MainWindow", "일지작성"))
        self.label_7.setText(_translate("MainWindow", "OK-LMS의 일지를 기반으로 해당 날짜의 일지를 모두 합하여 한번에 HRD-Net에 작성합니다."))
        self.groupBox_6.setTitle(_translate("MainWindow", "입력할 주차 설정"))
        self.label_10.setText(_translate("MainWindow", "주차"))
        self.groupBox_7.setTitle(_translate("MainWindow", "일지 입력"))
        self.Send_autodiary_btn.setText(_translate("MainWindow", "일지 전송"))
        self.Diar_create_btn.setText(_translate("MainWindow", "일지만들기"))
        self.Tap_dis.setTabText(self.Tap_dis.indexOf(self.tab_4), _translate("MainWindow", "HRD-Net 일지작성"))
        self.label_8.setText(_translate("MainWindow", "OK-LMS의 일지를 기반으로 해당 과목의 학습활동서를 엑셀파일로 생성합니다."))
        self.groupBox_8.setTitle(_translate("MainWindow", "입력할 주차 설정"))
        self.label_11.setText(_translate("MainWindow", "주차"))
        self.groupBox_9.setTitle(_translate("MainWindow", "직무 연관성 입력"))
        self.Excel_create_btn.setText(_translate("MainWindow", "일지만들기"))
        self.Excel_settings_btn.setText(_translate("MainWindow", "설정"))
        self.Excel_print_btn.setText(_translate("MainWindow", "인쇄"))
        self.Excel_open_btn.setText(_translate("MainWindow", "폴더 열기"))
        self.Tap_dis.setTabText(self.Tap_dis.indexOf(self.tab_5), _translate("MainWindow", "학습활동서 생성"))
        self.groupBox_3.setTitle(_translate("MainWindow", "확인할 주차 설정"))
        self.groupBox_4.setTitle(_translate("MainWindow", "확인할 주차 설정"))
        self.label_21.setText(_translate("MainWindow", "주차"))
        self.groupBox_5.setTitle(_translate("MainWindow", "일지 확인"))
        self.label_3.setText(_translate("MainWindow", "<OK-LMS>"))
        self.label_4.setText(_translate("MainWindow", "<HRD-Net>"))
        self.Tap_dis.setTabText(self.Tap_dis.indexOf(self.widget), _translate("MainWindow", "일지확인"))
        self.label_5.setText(_translate("MainWindow", "<주차 계산 재설정>"))
        self.label_6.setText(_translate("MainWindow", "계산 시작일="))
        self.Date_check.setText(_translate("MainWindow", "재설정시 오늘은 ()주차입니다."))
        self.Save_setting_btn.setText(_translate("MainWindow", "확인"))
        self.Op_pro_dis_check.setText(_translate("MainWindow", "작업과정표시"))
        self.Tap_dis.setTabText(self.Tap_dis.indexOf(self.tab_2), _translate("MainWindow", "설정"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
