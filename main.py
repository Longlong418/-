

# sys.path.append('project\login1signup')
# sys.path.append('D:\课设\大二下-机器学习(数据库)课设\project\login1signup\main_login.py')
# print(sys.path)
import login.admin_login
import login.admin_login_ui
import login.login_ui
import login.main_login
import login.signup
import login.signup_ui
import login.user_login
import login.user_login_ui
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件

    window = login.main_login.Login()
    # window.setStyleSheet('''QWidget{background-color:CornflowerBlue;}''')  # 颜色
    window.setFixedSize(window.width(), window.height())  # 禁止拉伸窗口

    window.show()

    # 结束QApplication
    sys.exit(app.exec_())
