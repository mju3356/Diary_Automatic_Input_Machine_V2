from QT_Design.Main_window import Ui_MainWindow
from PyQt5.QtWidgets import *
import LoginPage
import sys
from msedge.selenium_tools import Edge, EdgeOptions


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.login = False
        self.setupUi(self)
        self.Lock()
        self.Signal()

    def Signal(self):
        self.Login_btn.clicked.connect(self.Action_Login)

    def Lock(self):
        self.Cur_list.setEnabled(False)
        self.Tap_dis.setEnabled(False)

    def Unlock(self):
        self.Cur_list.setEnabled(True)
        self.Tap_dis.setEnabled(True)

    def Action_Login(self):
        Showloginpage = LoginPage.LoginPage(Driver, self.login)
        Showloginpage.exec_()
        if Showloginpage.lmsOk and Showloginpage.hrdOk:
            self.User_info.setText('환영합니다.'+Showloginpage.userName)
            self.Login_btn.setText('로그아웃')
            self.login=True
            self.Unlock()
        else:
            self.User_info.setText('로그인이 필요합니다.')
            self.Login_btn.setText('로그인')
            self.login=False
            self.Lock()





def SeleniumSettings():
    Options = EdgeOptions()
    Options.use_chromium = True
    # Options.add_argument("--headless")
    # Options.add_argument("disable-gpu")
    # Headlass 옵션
    global Driver
    Driver = Edge(options=Options, executable_path='lib/driver/msedgedriver.exe')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Program = Main_Window()
    Program.show()
    SeleniumSettings()
    app.exec_()
