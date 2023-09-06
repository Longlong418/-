from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from login.login_ui import Ui_login
from login.user_login import User_login
from login.signup import Signup
from login.admin_login import Admin_login
import sys


class Login(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.user_login.clicked.connect(self.user_login_show)
        self.ui.user_signup.clicked.connect(self.user_signup_show)
        self.ui.admin_login.clicked.connect(self.admin_login_show)
        # 判断子窗口是否打开
        self.is_userlogin = False
        self.is_usersignup = False
        self.is_adminlogin = False

    def user_login_show(self):
        self.user_login = User_login(self)
        self.user_login.show()
        self.is_userlogin = True

    def user_signup_show(self):
        self.user_signup = Signup()
        self.user_signup.show()
        self.is_usersignup = True

    def admin_login_show(self):
        self.admin_login = Admin_login(self)
        self.admin_login.show()
        self.is_adminlogin = True

    def closeEvent(self, event):
        # 重写closeEvent方法，在主窗口关闭时关闭子窗口
        if self.is_userlogin == True:
            self.user_login.close()
        if self.is_usersignup == True:
            self.user_signup.close()
        if self.is_adminlogin == True:
            self.admin_login.close()

        event.accept()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     # 初始化并展示我们的界面组件
#     window = Login()
#     window.setStyleSheet('''QWidget{background-color:CornflowerBlue;}''')  # 颜色
#     window.setFixedSize(window.width(), window.height())  # 禁止拉伸窗口

#     window.show()

#     # 结束QApplication
#     sys.exit(app.exec_())
