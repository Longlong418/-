from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from login.admin_login_ui import Ui_admin_login
import mysql.connector
from PySide6.QtCore import Signal, QObject
from PySide6.QtCore import Slot
from utils.connect import cnx
from admin.admin_main import admin_main


class Communicator(QObject):  # 信号量，用来退出登录等等操作
    logout_signal = Signal()


class Admin_login(QWidget):
    def __init__(self, mainlogin):
        super().__init__()
        self.ui = Ui_admin_login()
        self.ui.setupUi(self)
        self.mainlogin = mainlogin
        self.ui.login.clicked.connect(self.login)
        self.ui.passwords.returnPressed.connect(self.login)
        # 实现注销
        self.communicator = Communicator()
        # 订阅注销信号
        self.communicator.logout_signal.connect(self.logout)

    def login(self):
        adname = self.ui.adname.text().strip()
        passwords = self.ui.passwords.text()
        # print(username)
        # print(passwords)
        if adname == "" or passwords == "":
            QMessageBox.critical(self, '错误', '账号或密码不能为空！')
        else:
            # 创建游标对象
            connection = cnx()
            cursor = connection.cursor()
            # 执行查询语句
            cursor.execute(
                "SELECT uname,passwords FROM users where is_admin>=1")
            results = cursor.fetchall()
            # print(results)
            # print(adname)
            temp = (adname, passwords)
            if temp in results:
                # self.username = username  # 以便于将用户名传递给下一个窗口
                QMessageBox.information(self, "登录成功！", "登陆成功")
                self.hide()
                # from main_login import window  # 放在这里是避免了循环调用
                # 登录成功后关闭主窗口以及其他主窗口
                if self.mainlogin.is_userlogin == True:
                    self.mainlogin.user_login.close()
                if self.mainlogin.is_usersignup == True:
                    self.mainlogin.user_signup.close()
                if self.mainlogin.is_adminlogin == True:
                    self.mainlogin.admin_login.close()
                self.adname = adname
                self.mainlogin.hide()
                # 跳转到主页面
                # print("登录成功")
                self.admin_main = admin_main(self)
                self.admin_main.show()
                cursor.close()
            else:
                QMessageBox.critical(self, "错误", "账号或密码错误")

    @Slot()
    def logout(self):
        self.mainlogin.show()
        self.admin_main.close()
