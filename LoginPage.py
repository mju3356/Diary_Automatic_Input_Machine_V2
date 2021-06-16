from QT_Design.Login_window import Ui_Dialog
import  sys
from PyQt5.QtWidgets import *
class LoginPage(QDialog,Ui_Dialog):
    def __init__(self,Driver):
        super().__init__()
        self.setupUi(self)
        self.Signal()
        self.Driver=Driver

    def Signal(self):
        self.Login_btn_hrdnet.clicked.connect(self.HrdLogin)
        self.Login_btn_oklms.clicked.connect(self.LmsLogin)

    def HrdLogin(self):
        self.Driver.get('https://www.hrd.go.kr/hrdp/mb/pmbao/PMBAO0100T.do')

    def LmsLogin(self):
        self.Driver.get('https://oklms.koreatech.ac.kr/lu/login/goLmsUserLogin.do')








if __name__=='__main__':
    app=QApplication(sys.argv)
    Program=LoginPage()
    Program.show()
    app.exec_()