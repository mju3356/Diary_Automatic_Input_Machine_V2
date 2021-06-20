from QT_Design.Main_window import Ui_MainWindow
from PyQt5.QtWidgets import *
import LoginPage
import sys
from msedge.selenium_tools import Edge, EdgeOptions
import configparser
from datetime import datetime

DATEFORMATTER = "%Y-%m-%d"


def SeleniumSettings():
    Options = EdgeOptions()
    Options.use_chromium = True
    # Options.add_argument("--headless")
    # Options.add_argument("disable-gpu")
    # Headlass 옵션
    global Driver
    Driver = Edge(options=Options, executable_path='lib/driver/msedgedriver.exe')


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.login = 0
        self.setupUi(self)
        self.Lock()
        self.ReadConfig()
        self.Signal()

    def Signal(self):
        self.Login_btn.clicked.connect(self.ActionLogin)

    def Lock(self):
        self.Cur_list.setEnabled(False)
        self.Tap_dis.setEnabled(False)

    def Unlock(self):
        self.Cur_list.setEnabled(True)
        self.Tap_dis.setEnabled(True)

    def ActionLogin(self):
        showLoginPage = LoginPage.LoginPage(Driver, self.login)
        showLoginPage.exec_()
        if showLoginPage.lmsOk and showLoginPage.hrdOk:
            # self.User_info.setText('환영합니다.'+Showloginpage.userName)
            self.User_info.setText('환영합니다.' + '###님')
            self.Login_btn.setText('로그아웃')
            self.login = 1
            self.autoLogin = showLoginPage.autoLogin
            self.lmsId = showLoginPage.lmsId
            self.lmsPw = showLoginPage.lmsPw
            self.hrdId = showLoginPage.hrdId
            self.hrdPw = showLoginPage.hrdPw
            self.SaveConfig()
            self.Unlock()
        else:
            self.User_info.setText('로그인이 필요합니다.')
            self.Login_btn.setText('로그인')
            self.login = 0
            self.Cur_list.clear()
            self.autoLogin = 0
            self.SaveConfig()
            self.Lock()

    def ReadConfig(self):
        config = configparser.ConfigParser()
        config.read('Settings.ini')
        settings = config['Settings']
        self.autoLogin = int(settings['autoLogin'])
        self.hrdId = settings['hrdId']
        self.hrdPw = settings['hrdPw']
        self.lmsId = settings['lmsId']
        self.lmsPw = settings['lmsPw']
        self.startDate = datetime.strptime(settings['startDate'], DATEFORMATTER)
        self.showEdge = int(settings['showEdge'])

        if self.autoLogin: self.ActionLogin()

    def SaveConfig(self):
        config = configparser.ConfigParser()
        config['Settings'] = {}
        config['Settings']['autoLogin'] = str(self.autoLogin)
        config['Settings']['hrdId'] = self.hrdId
        config['Settings']['hrdPw'] = self.hrdPw
        config['Settings']['lmsId'] = self.lmsId
        config['Settings']['lmsPw'] = self.lmsPw
        config['Settings']['startDate'] = str(self.startDate.strftime(DATEFORMATTER))
        config['Settings']['showEdge'] = str(self.showEdge)
        with open('Settings.ini', 'w') as configfile:
            config.write(configfile)


if __name__ == '__main__':
    SeleniumSettings()
    app = QApplication(sys.argv)
    Program = Main_Window()
    Program.show()
    app.exec_()
