from admin.admin_mgt_ui import Ui_admin_mgt
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QDate
from utils.connect import cnx
import re


class Admin_mgt(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_admin_mgt()
        self.ui.setupUi(self)
        self.getadmindata()
        self.ui.tableWidget.cellClicked.connect(self.showadmindata)
        # 增
        self.ui.add.clicked.connect(self.add)
        # 删
        self.ui.delet.clicked.connect(self.delet)
        # 改
        self.ui.change.clicked.connect(self.change)
        # 查
        self.ui.search.clicked.connect(self.search)
        self.ui.search_admin.returnPressed.connect(self.search)
        self.ui.search_admin.textChanged.connect(self.onTextChanged)
        self.row = []
        self.currentrowindex = 1
    # 将管理员放在表里

    def getadmindata(self):
        connection = cnx()
        cursor = connection.cursor()
        sql = "SELECT uname,passwords FROM users where is_admin=1"
        cursor.execute(sql)
        results = cursor.fetchall()
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
    # 展示当前行

    def showadmindata(self):
        # 获取该对象
        selected_items = self.ui.tableWidget.selectedItems()
        # 将对象转化成列表
        if selected_items:
            selected_row = selected_items[0].row()
            row_data = []
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(selected_row, col)
                row_data.append(item.text())
            self.oldname = row_data[0]  # 暂存旧用户名
            # 将选中的改行填充到下边的框中
            self.ui.adminname.setText(row_data[0])
            self.ui.passwords.setText(row_data[1])
    # 修改

    def change(self):
        if self.ui.adminname.text() == "" and self.ui.passwords.text() == "":
            QMessageBox.critical(self, '错误', '请选择用户!')
        elif self.ui.adminname.text() == "" or self.ui.passwords.text() == "":
            QMessageBox.critical(self, '错误', '用户号和密码不能为空！')
        else:
            connection = cnx()
            cursor = connection.cursor()
            sql = "SELECT uname FROM users"
            cursor.execute(sql)
            results = cursor.fetchall()
            temp = (self.ui.adminname.text(),)

            if temp in results and self.oldname != self.ui.adminname.text():
                QMessageBox.critical(self, '错误', '该用户名已存在,请删除或修改后继续')
            else:
                reply = QMessageBox.question(
                    None, '提示', '是否修改？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )
                if reply == QMessageBox.Yes:
                    sql = "UPDATE users SET uname=%s,passwords=%s WHERE uname = %s"
                    cursor.execute(
                        sql, (self.ui.adminname.text(),  self.ui.passwords.text(), self.oldname))
                    connection.commit()
                    # print("修改成功:", cursor.rowcount)
                    QMessageBox.information(
                        self, "修改成功!", "修改成功!")
                    self.getadmindata()
                    self.showadmindata()
    # 增加

    def add(self):
        if self.ui.adminname.text() == "" and self.ui.passwords.text() == "":
            QMessageBox.critical(self, '错误', '请填入信息!')
        elif self.ui.adminname.text() == "" or self.ui.passwords.text() == "":
            QMessageBox.critical(self, '错误', '管理员名和密码不能为空！')
        else:
            connection = cnx()
            cursor = connection.cursor()
            sql = "SELECT uname FROM users"
            cursor.execute(sql)
            results = cursor.fetchall()
            temp = (self.ui.adminname.text(),)
            if temp in results:
                QMessageBox.critical(self, '错误', '该用户名已存在,请删除或修改后继续')
            else:
                sql = "INSERT INTO users(uname,email,passwords,entime,is_admin) VALUES (%s, %s, %s, %s,%s)"
                value = (self.ui.adminname.text(), "",
                         self.ui.passwords.text(), "2023/04/04", 1)
                cursor.execute(sql, value)
                # self.username = newname
                connection.commit()
                # print("修改成功:", cursor.rowcount)
                QMessageBox.information(
                    self, "添加成功!", "添加管理员成功!")
                self.getadmindata()
                self.showadmindata()
    # 删除

    def delet(self):
        if self.ui.adminname.text() == "":
            QMessageBox.critical(self, '错误', '请选择管理员!')
        else:
            connection = cnx()
            cursor = connection.cursor()
            sql = "SELECT uname FROM users where is_admin=1"
            cursor.execute(sql)
            results = cursor.fetchall()
            temp = (self.ui.adminname.text(),)
            # print(temp)
            # print(results)
            if temp not in results:
                QMessageBox.critical(self, '错误', '该用户不存在！')
            else:
                reply = QMessageBox.question(
                    None, '提示', '是否删除？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )
                if reply == QMessageBox.Yes:
                    sql = "DELETE FROM users WHERE uname = %s"
                    cursor.execute(sql, temp)
                    connection.commit()
                    QMessageBox.information(
                        self, "删除成功!", "删除管理员成功!")
                    self.getadmindata()
                    self.showadmindata()
    # 搜索

    # 搜索
    def onTextChanged(self, text):
        # 在文本发生改变时执行的逻辑
        self.currentrowindex = 1
        self.row.clear()
        table = self.ui.tableWidget
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
            table = self.ui.tableWidget
            if self.currentrowindex >= len(self.row):  # 翻到底后重翻
                self.currentrowindex = 0

            item = table.item(
                self.row[self.currentrowindex], 0)
            table.scrollToItem(item)  # 翻滚到当前项
            table.selectRow(self.row[self.currentrowindex])  # 选中当前行
            self.currentrowindex += 1

        else:
            QMessageBox.critical(self, '错误', '无结果')
