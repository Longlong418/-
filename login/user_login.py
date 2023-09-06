# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承


import mysql.connector
from login.user_login_ui import Ui_user_login
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import os
import user.user_main
import user.user_main_ui
import user.train
import user.train_ui
import user.user_information
import user.user_information_ui
from utils.connect import cnx
from PySide6.QtCore import Signal, QObject
from PySide6.QtCore import Slot


class Communicator(QObject):  # 信号量，用来退出登录等等操作
    logout_signal = Signal()


class User_login(QWidget):
    def __init__(self, mainlogin):
        super().__init__()
        self.ui = Ui_user_login()
        self.ui.setupUi(self)
        self.mainlogin = mainlogin
        self.ui.login.clicked.connect(self.login)
        self.ui.passwords.returnPressed.connect(self.login)
        # 实现注销
        self.communicator = Communicator()
        # 订阅注销信号
        self.communicator.logout_signal.connect(self.logout)

    def login(self):
        username = self.ui.username.text().strip()  # 将空格去掉
        passwords = self.ui.passwords.text()
        # print(username)
        # print(passwords)
        if username == "" or passwords == "":
            QMessageBox.critical(self, '错误', '账号或密码不能为空！')
        else:
            # 创建游标对象
            connection = cnx()
            cursor = connection.cursor()
            # 执行查询语句
            cursor.execute(
                "SELECT uname,passwords FROM users where is_admin=0")
            results = cursor.fetchall()
            # print(results)
            # print(username)
            temp = (username, passwords)
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
                self.mainlogin.hide()
                # 跳转到主页面
                self.main_user = user.user_main.User_main(
                    username, self.communicator)
                self.main_user.show()
                cursor.close()
            else:
                QMessageBox.critical(self, "错误", "账号或密码错误")

    @Slot()
    def logout(self):
        self.mainlogin.show()
        self.main_user.close()


# 建立数据库连接

# # 执行插入语句
# # cursor.execute("INSERT INTO users  VALUES (%s, %s,%s,%s)", (value1, value2))

# # 执行更新语句

# # 提交更改
# cnx.commit()
