from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from exp.data_info_ui import Ui_data_info
import sys
from utils.connect import cnx
import ast


class Data_info(QWidget):
    def __init__(self, parm):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_data_info()
        self.ui.setupUi(self)
        self.ui.test_path.setText(str(parm['test_path']))
        self.ui.test_sum.setText(str(parm['test_sum']))
        self.ui.test_dim.setText(str(parm['test_dim']))
        self.ui.train_path.setText(str(parm['train_path']))
        self.ui.train_sum.setText(str(parm['train_sum']))
        self.ui.train_dim.setText(str(parm['train_dim']))
        self.ui.username.setText("由{}上传".format(str(parm['username'])))
