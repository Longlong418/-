from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from exp.record_ui import Ui_record
from exp.result2 import Result2
from exp.data_info import Data_info
import sys
from utils.connect import cnx
import ast
from exp.predict import Predict

# 创建假model用来传参


class Fakemodel:
    def __init__(self):
        self.pic_path = {}
        self.exp = {}
        self.m_id = ""


class Record(QWidget):
    def __init__(self):
        super().__init__()
        # 实例化假model
        self.fakemodel = Fakemodel()
        # 设置界面为我们生成的界面
        self.ui = Ui_record()
        self.ui.setupUi(self)

        # 从数据库中获取实验信息
        self.getrecorddata()
        # 获取当前行
        self.ui.table.cellClicked.connect(self.showrecorddata)
        self.ui.results.clicked.connect(self.showresult)
        self.ui.data.clicked.connect(self.showdata)
        self.ui.remove.clicked.connect(self.delet)
        self.ui.predict.clicked.connect(self.pre)

        # 搜索
        self.row = []
        self.currentrowindex = 1
        self.ui.search.clicked.connect(self.search)
        self.ui.search_user.returnPressed.connect(self.search)
        # 监听搜索框是否改变
        self.ui.search_user.textChanged.connect(self.onTextChanged)

    # 从数据库中获取实验信息

    def getrecorddata(self):
        connection = cnx()
        cursor = connection.cursor()
        sql = """
        SELECT r.r_id,u.uname,tr.train_path, t.test_path, m.mname, m.mparm, r.result, r.record_date
        FROM record r
        JOIN users u ON r.users_uname = u.uname
        JOIN test t ON r.test_test_id = t.test_id
        JOIN train tr ON r.train_t_id = tr.t_id
        JOIN model m ON r.model_m_id = m.m_id
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        # print(results)
        self.ui.table.setRowCount(len(results))
        for row, user_data in enumerate(results):
            for col, value in enumerate(user_data):
                item = QTableWidgetItem(str(value))
                self.ui.table.setItem(row, col, item)
        self.adjust_table_widget_size(self.ui.table)
    # 表格自适应大小

    def adjust_table_widget_size(self, table_widget):
        table_widget.resizeColumnsToContents()
        table_widget.resizeRowsToContents()
        for row in range(table_widget.rowCount()):
            for column in range(table_widget.columnCount()):
                item = table_widget.item(row, column)
                if item:
                    item.setSizeHint(item.sizeHint())

    # 获取当前行
    def showrecorddata(self):
        # 获取该对象
        selected_items = self.ui.table.selectedItems()
        # 将对象转化成列表
        if selected_items:
            selected_row = selected_items[0].row()
            row_data = []
            for col in range(self.ui.table.columnCount()):
                item = self.ui.table.item(selected_row, col)
                row_data.append(item.text())
        if len(row_data) == 0:
            QMessageBox.critical(self, "错误", "请选择表中一项数据进行操作")
        return row_data

    # 查看实验结果
    def showresult(self):
        currentrow = self.showrecorddata()
        r_id = currentrow[0]
        connection = cnx()
        cursor = connection.cursor()
        sql = "SELECT result,pic_path FROM record WHERE r_id = %s"
        cursor.execute(sql, (r_id,))
        results = cursor.fetchall()
        # print(results[0][0])
        # 实验参数
        self.fakemodel.exp = ast.literal_eval(results[0][0])  # 将字典字符串eval一下
        self.fakemodel.pic_path = ast.literal_eval(results[0][1])
        self.fakemodel.m_id = r_id
        self.result = Result2(self.fakemodel)
        self.result.show()
    # 模型预测

    def pre(self):
        currentrow = self.showrecorddata()
        parm = {}
        m_id = currentrow[0]
        connection = cnx()
        cursor = connection.cursor()
        sql = "SELECT mname,model_path,x FROM model WHERE m_id = %s"
        cursor.execute(sql, (m_id,))
        results = cursor.fetchall()
        parm['name'] = results[0][0]
        parm['path'] = results[0][1]
        parm['x'] = results[0][2]
        self.pre2 = Predict(parm)
        self.pre2.show()

    # 查看数据集
    def showdata(self):
        parm = {}

        currentrow = self.showrecorddata()
        test_id = currentrow[0]  # 因为m_id和r_id以及测试集训练集id都一样哈哈哈哈
        parm['username'] = currentrow[1]
        connection = cnx()
        cursor = connection.cursor()
        sql = "SELECT test_path,test_sum,test_dim FROM test WHERE test_id = %s"
        cursor.execute(sql, (test_id,))
        results = cursor.fetchall()
        parm['test_path'] = results[0][0]
        parm['test_sum'] = results[0][1]
        parm['test_dim'] = results[0][2]
        sql = "SELECT train_path,train_sum,train_dim FROM train WHERE t_id = %s"
        cursor.execute(sql, (test_id,))
        results = cursor.fetchall()
        parm['train_path'] = results[0][0]
        parm['train_sum'] = results[0][1]
        parm['train_dim'] = results[0][2]
        self.data_info = Data_info(parm)
        self.data_info.show()
    # 删除

    def delet(self):
        currentrow = self.showrecorddata()
        test_id = currentrow[0]
        reply = QMessageBox.question(
            None, '提示', '是否删除？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            connection = cnx()
            cursor = connection.cursor()
            # 根据test直接级联删除record表，可以少写两行代码 嘻嘻嘻
            sql = "DELETE FROM test WHERE test_id = %s"
            cursor.execute(sql, (test_id,))
            sql = "DELETE FROM train WHERE t_id = %s"
            cursor.execute(sql, (test_id,))
            sql = "DELETE FROM model WHERE m_id = %s"
            cursor.execute(sql, (test_id,))
            results = cursor.fetchall()
            connection.commit()
            QMessageBox.information(self, "已删除!", "已删除")
            self.getrecorddata()
    # 搜索

    def onTextChanged(self, text):
        # 在文本发生改变时执行的逻辑
        self.currentrowindex = 1
        self.row.clear()
        table = self.ui.table
        table.clearSelection()
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item is not None and item.text() == text and row not in self.row:
                    self.row.append(row)
        if len(self.row) != 0:
            item = table.item(self.row[0], 0)
            table.scrollToItem(item)  # 翻滚到当前项
            table.selectRow(self.row[0])  # 选中当前行

    def search(self):
        if len(self.row) != 0:
            table = self.ui.table
            if self.currentrowindex >= len(self.row):  # 翻到底后重翻
                self.currentrowindex = 0

            item = table.item(
                self.row[self.currentrowindex], 0)
            table.scrollToItem(item)  # 翻滚到当前项
            table.selectRow(self.row[self.currentrowindex])  # 选中当前行
            self.currentrowindex += 1

        else:
            QMessageBox.critical(self, '错误', '无结果')
