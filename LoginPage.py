from QT_Design.Login_window import Ui_Dialog
import sys
from PyQt5.QtWidgets import *
import time
from bs4 import BeautifulSoup
import configparser


class LoginPage(QDialog, Ui_Dialog):
    def __init__(self, driver, login):
        super().__init__()
        self.setupUi(self)
        self.Signal()
        self.driver = driver
        self.login = login
        self.hrdOk = self.lmsOk = False
        self.ReadConfig()
        self.CheckAutoLogin()
        self.CheckLogOut()

    def Signal(self):
        self.Login_btn_hrdnet.clicked.connect(self.HrdLogin)
        self.Login_btn_oklms.clicked.connect(self.LmsLogin)
        self.Auto_login_check.stateChanged.connect(self.ActionAutoSave)

    def ActionAutoSave(self):
        if self.Auto_login_check.isChecked():
            self.autoLogin = 1
        else:
            self.autoLogin = 0

    def HrdLogin(self):
        if not self.hrdOk:
            self.hrdId=id = self.Id_input_hrdnet.text()
            self.hrdPw=pw = self.Pw_input_hrdnet.text()
            if id is None or id == '' or not id:
                QMessageBox.about(self, 'Error', 'ID를 입력하세요')
                self.Id_input_hrdnet.setFocus(True)
                return
            if pw is None or pw == '' or not pw:
                QMessageBox.about(self, 'Error', 'PassWord를 입력하세요')
                self.Pw_input_hrdnet.setFocus(True)
                return
            self.driver.get('https://www.hrd.go.kr/hrdp/mb/pmbao/PMBAO0100T.do')
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id('userloginId').send_keys(id)
            self.driver.find_element_by_id('userloginPwd').send_keys(pw)
            self.driver.find_element_by_id('loginBtn').click()
            time.sleep(1)

            try:
                self.driver.switch_to.alert.accept()
                QMessageBox.about(self, 'Error', 'Hrd-Net 로그인에 실패했습니다.')
                return
            except:
                self.hrdOk = True
                self.Login_btn_hrdnet.setText('로그아웃')
        else:
            self.driver.get('http://www.hrd.go.kr/hrdp/mb/pmbao/logout.do')
            self.hrdOk = False
            self.Login_btn_hrdnet.setText('로그인')

    def LmsLogin(self):
        if not self.lmsOk:
            self.lmsId = id = self.Id_input_oklms.text()
            self.lmsPw = pw = self.Pw_input_oklms.text()
            if id is None or id == '' or not id:
                QMessageBox.about(self, 'Error', 'ID를 입력하세요')
                self.Id_input_hrdnet.setFocus(True)
                return
            if pw is None or pw == '' or not pw:
                QMessageBox.about(self, 'Error', 'PassWord를 입력하세요')
                self.Pw_input_hrdnet.setFocus(True)
                return
            self.driver.get('https://oklms.koreatech.ac.kr/lu/login/goLmsUserLogin.do')
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_name('memId').send_keys(id)
            self.driver.find_element_by_name('memPasswordEncript').send_keys(pw)
            self.driver.find_element_by_name('login-btn').click()
            time.sleep(1)
            try:
                self.driver.switch_to.alert.accept()
                QMessageBox.about(self, 'Error', 'OK-LMS 로그인에 실패했습니다.')
                return None
            except:
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                self.userName = soup.select_one('#info-area > dl > dd.info-text > b').text

                self.lmsOk = True
                self.Login_btn_oklms.setText("로그아웃")
        else:
            self.driver.get('https://oklms.koreatech.ac.kr/commbiz/login/logout.do')
            self.lmsOk = False
            self.Login_btn_oklms.setText('로그인')

    def ReadConfig(self):
        config = configparser.ConfigParser()
        config.read('Settings.ini')
        settings = config['Settings']
        self.autoLogin = int(settings['autoLogin'])
        self.hrdId = settings['hrdId']
        self.hrdPw = settings['hrdPw']
        self.lmsId = settings['lmsId']
        self.lmsPw = settings['lmsPw']

    def CheckAutoLogin(self):
        if self.autoLogin and not self.login:
            self.Auto_login_check.setChecked(True)
            self.Id_input_oklms.setText(self.lmsId)
            self.Pw_input_oklms.setText(self.lmsPw)
            self.Id_input_hrdnet.setText(self.hrdId)
            self.Pw_input_hrdnet.setText(self.hrdPw)
            self.HrdLogin()
            self.LmsLogin()
            QMessageBox.about(self, '완료', '자동로그인 완료되었습니다.')

    def CheckLogOut(self):
        if self.login:
            self.lmsOk = self.hrdOk = True
            self.LmsLogin()
            self.HrdLogin()
            QMessageBox.about(self, '완료', '로그아웃되었습니다.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Program = LoginPage()
    Program.show()
    app.exec_()
