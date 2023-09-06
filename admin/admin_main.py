from admin.admin_main_ui import Ui_admin_main
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Signal, QObject
import sys
from utils.connect import cnx
from admin.user_mgt import User_mgt
from admin.admin_mgt import Admin_mgt
from admin.record_mgt import Record
import mysql.connector

# from signup import Signup
# from admin_login import Admin_login


class admin_main(QWidget):
    def __init__(self, admin_data):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_admin_main()
        self.ui.setupUi(self)
        self.admin_data = admin_data
        # 连接数据库
        connection = cnx()
        cursor = connection.cursor()
        sql = "SELECT is_admin FROM users where uname=%s"
        cursor.execute(sql, (self.admin_data.adname,)
                       )
        results = cursor.fetchall()
        self.admin_level = results[0][0]
        if self.admin_level == 2:
            self.ui.label.setText("欢迎您,超级管理员")
        if self.admin_level == 1:
            self.ui.admin.setEnabled(False)
            self.ui.admin.setToolTip("只有超级管理员可以访问此页面")
        self.ui.user.clicked.connect(self.user_mgt)
        self.ui.logout.clicked.connect(self.logout)
        self.ui.admin.clicked.connect(self.admin_mgt)
        self.ui.record.clicked.connect(self.record_mgt)
        self.communicator = admin_data.communicator  # 实现退出登录

        # 判断子窗口是否打开
        self.is_usermgt = False
        self.is_adminmgt = False
        self.is_information = False

    def user_mgt(self):
        self.usermgt = User_mgt()
        # 禁止拉伸
        self.usermgt.setFixedSize(
            self.usermgt.width(), self.usermgt.height())
        self.usermgt.show()
        self.is_usermgt = True

    def admin_mgt(self):
        self.adminmgt = Admin_mgt()
        self.adminmgt.setFixedSize(
            self.adminmgt.width(), self.adminmgt.height())
        self.adminmgt.show()
        self.is_adminmgt = True

    def record_mgt(self):
        self.record = Record()
        self.record.setFixedSize(
            self.record.width(), self.record.height())
        self.record.show()
        self.is_information = True

    def logout(self):
        # 发生退出登录的信号
        reply = QMessageBox.question(
            None, '提示', '是否退出登录？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.communicator.logout_signal.emit()

    def closeEvent(self, event):
        # 重写closeEvent方法，在主窗口关闭时关闭子窗口
        if self.is_usermgt == True:
            self.usermgt.close()
        if self.is_adminmgt == True:
            self.adminmgt.close()
        if self.is_information == True:
            self.record.close()

        event.accept()
