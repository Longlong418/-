from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from login.signup_ui import Ui_Signup
import mysql.connector
from datetime import date
from utils.connect import cnx


class Signup(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Signup()
        self.ui.setupUi(self)
        self.ui.sign.clicked.connect(self.sign)
        self.ui.passwords2.returnPressed.connect(self.sign)

    def sign(self):
        username = self.ui.username.text().strip()  # 删除空格
        passwords1 = self.ui.passwords1.text()
        passwords2 = self.ui.passwords2.text()
        # print(username)
        # print(passwords)
        if username == "" or passwords1 == "" or passwords2 == "":
            QMessageBox.critical(self, '错误', '账号或密码不能为空！')
        elif passwords1 != passwords2:
            QMessageBox.critical(self, '错误', '请输入两次相同的密码')
        elif len(passwords1) < 6:
            QMessageBox.critical(self, '错误', '密码请设置在6位数以上')
        else:

            # 连接数据库
            connection = cnx()
            # 创建游标对象
            cursor = connection.cursor()
            # 执行查询语句
            cursor.execute("SELECT uname FROM users")
            results = cursor.fetchall()  # 查询单个结果
            # print(results)
            tname = username.lower()  # 转为小写
            judge = True
            for i in range(len(results)):
                if results[i][0].lower() == tname:
                    judge = False
                    break
            if judge == False:
                QMessageBox.critical(self, "错误", "该用户名已存在")
            else:
                QMessageBox.information(self, "注册成功！", "注册成功")
                current_date = date.today()
                # print(current_date)
                cursor.execute("INSERT INTO users (uname, passwords,entime,email,is_admin) VALUES (%s, %s,%s,%s,%s)", (
                    username, passwords1, current_date, "", 0))
                connection.commit()
                cursor.close()
                self.hide()
