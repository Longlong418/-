from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QPixmap
from exp.result_ui import Ui_result
import sys
from utils.connect import cnx
import random
from datetime import datetime


def random_id():
    return random.randint(10000, 99999)


class Result(QWidget):
    def __init__(self, model, username):
        super().__init__()
        self.model = model
        self.username = username

        # 设置界面为我们生成的界面
        self.ui = Ui_result()
        self.ui.setupUi(self)
        # 存数据库：
        self.up_sql()
        # 将结果展示在表内
        self.getresultdata()

        self.ui.ROC.clicked.connect(self.change_page)
        self.ui.p_r.clicked.connect(self.change_page)
        self.ui.learn.clicked.connect(self.change_page)
        self.ui.stackedWidget.setCurrentIndex(0)
        roc_pic = self.model.roc_path
        pr_path = self.model.pr_path
        learn_path = self.model.learn_path
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

    def up_sql(self):
        connection = cnx()
        cursor = connection.cursor()
        cursor.execute("SELECT r_id FROM record")
        results = cursor.fetchall()
        m_id = random_id()
        temp = (m_id,)
        # 生成不重复的实验id
        while True:
            if temp not in results:
                break
            m_id = random_id()
            temp = (m_id,)
        # 插入model数据库
        cursor.execute("INSERT INTO model (m_id, mname,mparm,model_path,x) VALUES (%s,%s,%s,%s,%s)", (
            m_id, self.model.name, str(self.model.params), self.model.model_path, str(self.model.headers)))
        # 插入test数据库
        test_id = m_id
        cursor.execute("INSERT INTO test(test_id, test_path,test_sum,test_dim,users_uname) VALUES (%s,%s,%s,%s,%s)", (
            test_id, self.model.test_file, self.model.test_sum, self.model.test_dim, self.username))
        # 插入train数据库
        train_id = m_id
        cursor.execute("INSERT INTO train(t_id, train_path,train_sum,train_dim,users_uname) VALUES (%s,%s,%s,%s,%s)", (
            train_id, self.model.train_file, self.model.train_sum, self.model.train_dim, self.username))
        # 插入record数据库
        r_id = m_id
        current_time = datetime.now()
        current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        exp1 = str(self.model.exp)
        # print(exp1)
        cursor.execute("INSERT INTO record (r_id, result,record_date,pic_path,users_uname,test_test_id,train_t_id,model_m_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (
            r_id,  exp1, current_time, str(self.model.exp_pic), self.username, test_id, train_id, m_id))
        self.ui.id.setText(str(m_id))

        connection.commit()

    def change_page(self,):
        sender = self.sender()
        if sender == self.ui.ROC:
            self.ui.stackedWidget.setCurrentIndex(0)
        elif sender == self.ui.p_r:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(2)
