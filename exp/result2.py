from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QPixmap
from exp.result_ui import Ui_result
import sys
from utils.connect import cnx
import random
from datetime import datetime


def random_id():
    return random.randint(10000, 99999)


class Result2(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        # 设置界面为我们生成的界面
        self.ui = Ui_result()
        self.ui.setupUi(self)
        # 将结果展示在表内
        self.getresultdata()
        self.ui.id.setText(self.model.m_id)

        self.ui.ROC.clicked.connect(self.change_page)
        self.ui.p_r.clicked.connect(self.change_page)
        self.ui.learn.clicked.connect(self.change_page)
        self.ui.stackedWidget.setCurrentIndex(0)
        roc_pic = self.model.pic_path['roc_path']
        pr_path = self.model.pic_path['pr_path']
        learn_path = self.model.pic_path['learn_path']
        # 图1
        pixmap = QPixmap(roc_pic)
        self.ui.pic_1.setPixmap(pixmap)
        self.ui.pic_1.setScaledContents(True)
        # 图2
        pixmap = QPixmap(pr_path)
        self.ui.pic_2.setPixmap(pixmap)
        self.ui.pic_2.setScaledContents(True)
        # 图3
        pixmap = QPixmap(learn_path)
        self.ui.pic_3.setPixmap(pixmap)
        self.ui.pic_3.setScaledContents(True)
    # 将数据库中的用户放在表里

    def getresultdata(self):
        # 将字典转化为列表型
        results = [(key, value) for key, value in self.model.exp.items()]
        # print(results)
        self.ui.tableWidget.setRowCount(len(results))
        for row, user_data in enumerate(results):
            for col, value in enumerate(user_data):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, col, item)
        self.adjust_table_widget_size(self.ui.tableWidget)
     # 表格自适应大小

    def adjust_table_widget_size(self, table_widget):
        table_widget.resizeColumnsToContents()
        table_widget.resizeRowsToContents()
        for row in range(table_widget.rowCount()):
            for column in range(table_widget.columnCount()):
                item = table_widget.item(row, column)
                if item:
                    item.setSizeHint(item.sizeHint())

    def change_page(self,):
        sender = self.sender()
        if sender == self.ui.ROC:
            self.ui.stackedWidget.setCurrentIndex(0)
        elif sender == self.ui.p_r:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(2)
