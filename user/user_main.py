from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Signal, QObject
from user.user_main_ui import Ui_user_main
import sys
from user.user_information import User_information
from user.train import Train
from exp.record import Record
import mysql.connector

# from signup import Signup
# from admin_login import Admin_login


class User_main(QWidget):
    def __init__(self, username, communicator):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_user_main()
        self.ui.setupUi(self)
        self.ui.train.clicked.connect(self.train_show)
        self.ui.record.clicked.connect(self.record_show)
        self.ui.information.clicked.connect(self.information_show)
        self.ui.logout.clicked.connect(self.logout)
        self.communicator = communicator  # 实现退出登录
        self.username = username
        self.ui.username.setText("欢迎您,"+self.username)
        # 判断子窗口是否打开
        self.is_train = False
        self.is_record = False
        self.is_information = False

    def train_show(self):
        self.train = Train(self.username)
        self.train.show()
        self.is_train = True

    def record_show(self):
        self.record = Record(self.username)
        self.record.show()
        self.is_record = True

    def information_show(self):
        self.information = User_information(self.username, self)
        self.information.show()
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
        if self.is_train == True:
            self.train.close()
        if self.is_record == True:
            self.record.close()
        if self.is_information == True:
            self.information.close()

        event.accept()


# if __name__ == "__main__":

#     app = QApplication(sys.argv)

#     # 初始化并展示我们的界面组件
#     window = User_main()
#     window.setStyleSheet('''QWidget{background-color:CornflowerBlue;}''')  # 颜色
#     window.setFixedSize(window.width(), window.height())  # 禁止拉伸窗口

#     window.show()

#     # 结束QApplication
#     sys.exit(app.exec_())
