from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QProgressBar, QVBoxLayout, QDialog
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtCore import Qt, QThread, QBasicTimer, QTimer, QThread, Signal
from PySide6 import QtCore, QtGui, QtWidgets
from user.train_ui import Ui_train
import sys
from utils.draw_pic import draw_ROC
from utils.draw_pic import draw_pre_rec
from utils.draw_pic import draw_learning_curve
from ml_model.Logistic_model import logistic_model
from ml_model.LinearSVC_model import LinearSVC_model
from ml_model.DecisionTreecf_model import decision_tree_model
from ml_model.MLP_model import MLPClassifier_model
from user.result import Result
import ast
import time


def is_dict_string(string):
    try:
        # 使用 ast.literal_eval 评估字符串，并将其转换为字典对象
        dictionary = ast.literal_eval(string)

        # 检查评估后的对象是否为字典类型
        if isinstance(dictionary, dict):
            return True
        else:
            return False
    except (ValueError, SyntaxError):
        return False


class Train(QWidget):
    def __init__(self, username):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_train()
        self.ui.setupUi(self)
        self.username = username
        self.ui.modelchoice.currentIndexChanged.connect(self.switch_page)
        self.ui.uptest.clicked.connect(self.open_file_dialog)
        self.ui.uptrain.clicked.connect(self.open_file_dialog)
        self.ui.start_train.clicked.connect(self.start_train1)
        self.test_data = ""
        self.train_data = ""
        # 进度条
        self.progress_bar = QProgressBar(self)
        self.progress_timer = QTimer(self)
        self.progress_timer.timeout.connect(self.hide_progress_bar)

        # 设置只能输入浮点数的组件
        validator = QDoubleValidator()
        validator.setBottom(0)  # 设置最小值为0
        self.ui.l_c.setValidator(validator)
        self.ui.x_c.setValidator(validator)
        self.ui.x_tol.setValidator(validator)
        # 设置只能输入正整数的组件
        validator = QIntValidator()
        validator.setBottom(1)  # 设置最小值为1
        self.ui.l_max_i.setValidator(validator)
        self.ui.dt_max_d.setValidator(validator)
        self.ui.dt_min_s.setValidator(validator)
    # 进度条

    def hide_progress_bar(self):
        # 停止定时器
        self.progress_timer.stop()

        # 隐藏进度条
        self.progress_bar.hide()

    # 选择文件
    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)  # 选择已存在的文件
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            # print(selected_files)
            if selected_files[0][-3:] != 'csv' and selected_files[0][-4:] != 'xlsx' and selected_files[0][-3:] != 'xls':
                QMessageBox.critical(self, "错误", "选择csv、xls或xlsx文件!")
            else:
                sender = self.sender()
                if sender == self.ui.uptest:
                    self.ui.test_data.setText(selected_files[0])
                    self.test_data = selected_files[0]
                else:
                    self.ui.train_data.setText(selected_files[0])
                    self.train_data = selected_files[0]
    # 切换页面

    def switch_page(self):
        self.ui.stackedWidget.setCurrentIndex(
            self.ui.modelchoice.currentIndex())
    # 开始训练

    def start_train1(self):
        parms = {}
        if self.ui.parm.text() != "":
            if is_dict_string(self.ui.parm.text()):
                parms = eval(self.ui.parm.text())
            else:
                QMessageBox.critical(self, "错误", "参数格式错误,将以默认参数训练")
        try:
            if self.ui.modelchoice.currentText() == 'Logistic回归分类器':
                self.model = logistic_model()
                if len(parms) == 0:
                    parms['penalty'] = self.ui.l_penalty.currentText()
                    parms['solver'] = self.ui.l_solver.currentText()
                    parms['C'] = float(self.ui.l_c.text())
                    parms['max_iter'] = int(self.ui.l_max_i.text())

            elif self.ui.modelchoice.currentText() == '线性支持向量分类':
                self.model = LinearSVC_model()
                if len(parms) == 0:
                    parms['penalty'] = self.ui.x_penalty.currentText()
                    parms['loss'] = self.ui.x_loss.currentText()
                    parms['C'] = float(self.ui.x_c.text())
                    parms['tol'] = float(self.ui.x_tol.text())
                # {"penalty":'l2',"dual":False,"tol":0.0001,"C":1.0,"fit_intercept":True,"intercept_scaling":1,"class_weight":None,"random_state":None,"solver":'lbfgs',"max_iter":100,"multi_class":'auto',"verbose":0,"warm_start":False,"n_jobs":None,"l1_ratio":None}

            elif self.ui.modelchoice.currentText() == '决策树分类器':
                self.model = decision_tree_model()  # 实例化模型
                if len(parms) == 0:
                    parms['criterion'] = self.ui.dt_criterion.currentText()

                    parms['max_depth'] = int(self.ui.dt_max_d.text())

                    parms['min_samples_split'] = int(self.ui.dt_min_s.text())
                    if self.ui.dt_max_f.currentText() == "None":
                        parms['max_features'] = None
                    else:
                        parms['max_features'] = self.ui.dt_max_f.currentText()
            elif self.ui.modelchoice.currentText() == 'MLPClassifier':
                self.model = MLPClassifier_model()  # 实例化模型
                if len(parms) == 0:  # 传参
                    parms['batch_size'] = int(self.ui.batch_size.text())

                    parms['activation'] = str(self.ui.active.currentText())

                    parms['max_iter'] = int(self.ui.max_iter.text())

                    parms['learning_rate_init'] = float(
                        self.ui.learrate.text())
            self.model.params = parms
            # print(parms.values())
            if "" in parms.values():
                QMessageBox.critical(self, "错误", "参数不能为空!")
            elif self.test_data == "" or self.train_data == "":
                QMessageBox.critical(self, "错误", "请选择数据集!")
            else:
                self.model.test_file = self.test_data
                self.model.train_file = self.train_data

                self.model.start_train()

                # 展示结果
                self.result = Result(self.model, self.username)
                self.result.show()

        except:
            QMessageBox.critical(self, "错误", "参数冲突或数据集错误,请检查!")
