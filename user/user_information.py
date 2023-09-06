from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from user.user_information_ui import Ui_user_information
import mysql.connector
from utils.connect import cnx
import re


class User_information(QWidget):
    def __init__(self, username, usermain):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_user_information()
        self.ui.setupUi(self)
        self.ui.save.clicked.connect(self.save)
        self.ui.email.returnPressed.connect(self.save)
        self.ui.change.clicked.connect(self.change)
        self.ui.passwords_3.returnPressed.connect(self.change)
        self.username = username
        self.usermain = usermain
        # 读取个人信息
        self.get_info()

    def get_info(self):
        connection = cnx()
        cursor = connection.cursor()
        sql = "SELECT * FROM users where uname=%s"
        cursor.execute(sql, (self.username,))
        results = cursor.fetchall()
        self.ui.username.setText(self.username)
        self.ui.email.setText(results[0][1])
        self.oldpasswords = results[0][2]
        self.ui.dates.setText(str(results[0][3]))
        cursor.close()

    def change(self):
        if self.ui.passwords.text() == "" or self.ui.passwords_3.text() == "" or self.ui.passwords_2.text() == "":
            QMessageBox.critical(self, "错误", "请输入密码！")
        elif self.ui.passwords.text() != self.oldpasswords:
            QMessageBox.critical(self, "错误", "原密码错误！")
        elif self.ui.passwords_3.text() != self.ui.passwords_2.text():
            QMessageBox.critical(self, "错误", "请输入两次相同的新密码！")
        elif len(self.ui.passwords_3.text()) < 6:
            QMessageBox.critical(self, "错误", "请设置6位数以上的密码！")
        else:
            reply = QMessageBox.question(
                None, '提示', '是否修改？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                connection = cnx()
                cursor = connection.cursor()
                sql = "UPDATE users SET  passwords = %s WHERE uname = %s"
                cursor.execute(
                    sql, (self.ui.passwords_2.text(), self.username))
                # self.username = newname
                connection.commit()
                # print("修改成功:", cursor.rowcount)
                QMessageBox.information(
                    self, "修改成功!", "请重新登录")
                self.usermain.communicator.logout_signal.emit()

    def save(self):
        reply = QMessageBox.question(
            None, '提示', '是否保存？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            newname = self.ui.username.text()
            newemail = self.ui.email.text()
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # 检查邮箱格式
            if not re.match(pattern, newemail):
                QMessageBox.critical(self, '错误', '请输入正确的邮箱格式(xxx@xx.xxx)')
            else:
                connection = cnx()
                cursor = connection.cursor()
                cursor.execute("SELECT uname FROM users")
                results = cursor.fetchall()
                temp = (newname,)
                if temp in results and newname != self.username:
                    QMessageBox.critical(self, "错误", "该用户名已存在")
                else:
                    sql = "UPDATE users SET uname=%s,email = %s WHERE uname = %s"
                    cursor.execute(
                        sql, (newname, newemail, self.username))
                    # self.username = newname
                    connection.commit()
                    # print("修改成功:", cursor.rowcount)

                    QMessageBox.information(
                        self, "修改成功!", "请重新登录")
                    self.usermain.communicator.logout_signal.emit()

                    # cursor.close()
                    # connection.close()
        else:
            pass
