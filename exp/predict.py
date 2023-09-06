from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from exp.predict_ui import Ui_predict

import sys
import pickle
import numpy as np
import ast


def is_list(string):
    try:
        ast.literal_eval(string)
        return True
    except (SyntaxError, ValueError):
        return False


# 创建假model用来传参


class Predict(QWidget):
    def __init__(self, parm):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_predict()
        self.ui.setupUi(self)
        self.parm = parm
        self.ui.pre.clicked.connect(self.predict)
        self.ui.path.setText(parm['path'])
        self.ui.name.setText(parm['name'])
        self.ui.X.setText(parm['x'])

    def predict(self):
        if not is_list(self.ui.input_x.text()):
            QMessageBox.critical(self, '错误', '请输入正确的格式')
        else:
            try:
                x = ast.literal_eval(self.ui.input_x.text())
                x = np.array(x)
                x = x.reshape(1, -1)
                with open(self.parm['path'], 'rb') as file:
                    clf = pickle.load(file)
                y_pred = clf.predict(x)
                self.ui.result.setText(str(y_pred))
            except:
                QMessageBox.critical(self, '错误', "输入的x有误")
