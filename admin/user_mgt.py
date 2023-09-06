from admin.user_mgt_ui import Ui_user_mgt
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QDate
from utils.connect import cnx
import re


class User_mgt(QWidget):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_user_mgt()
        self.ui.setupUi(self)
        self.row = []  # 搜索要用到
        self.currentrowindex = 0  # 搜索用到
        # 从数据库中获取用户信息
        self.getuserdata()
        # 点击每一行获取信息
        self.ui.tableWidget.cellClicked.connect(self.showuserdata)
        # 修改
        self.ui.change.clicked.connect(self.change)
        # 增加
        self.ui.add.clicked.connect(self.add)
        # 删除
        self.ui.delet.clicked.connect(self.delet)
        # 搜索
        self.ui.search.clicked.connect(self.search)
        self.ui.search_user.returnPressed.connect(self.search)
        # 监听搜索框是否改变
        self.ui.search_user.textChanged.connect(self.onTextChanged)

    # 将数据库中的用户放在表里
    def getuserdata(self):
        connection = cnx()
        cursor = connection.cursor()
        sql = "SELECT uname,email,passwords,entime FROM users where is_admin<1"
        cursor.execute(sql)
        results = cursor.fetchall()
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

    # 获取当前行的数据
    def showuserdata(self):
        # 获取该对象
        selected_items = self.ui.tableWidget.selectedItems()
        # 将对象转化成列表
        if selected_items:
            selected_row = selected_items[0].row()
            row_data = []
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(selected_row, col)
                row_data.append(item.text())
            self.oldname = row_data[0].lower()  # 暂存旧用户名
            # 将选中的改行填充到下边的框中
            self.ui.username.setText(row_data[0])
            self.ui.email.setText(row_data[1])
            self.ui.passwords.setText(row_data[2])
            time = str(row_data[3])
            year = int(time[0]+time[1]+time[2]+time[3])
            month = int(time[5]+time[6])
            day = int(time[8]+time[9])
            # print(time, year, month, day)
            tdate = QDate(year, month, day)  # 注意是int型
            # print(tdate)
            self.ui.date.setDate(tdate)
            # print(self.ui.date.text())

    def change(self):
        if self.ui.username.text() == "" and self.ui.passwords.text() == "" and self.ui.email.text() == "" and self.ui.date.text() == "":
            QMessageBox.critical(self, '错误', '请选择用户!')
        elif self.ui.username.text() == "" or self.ui.passwords.text() == "":
            QMessageBox.critical(self, '错误', '用户号和密码不能为空！')
        else:
            connection = cnx()
            cursor = connection.cursor()
            sql = "SELECT uname FROM users"
            cursor.execute(sql)
            results = cursor.fetchall()
            tname = self.ui.username.text().lower()
            # print(tname)
            judge = True
            for i in range(len(results)):
                if results[i][0].lower() == tname:
                    judge = False
                    break
            if judge == False and self.oldname != tname:
                QMessageBox.critical(self, '错误', '该用户名已存在,请删除或修改后继续')
            else:
                reply = QMessageBox.question(
                    None, '提示', '是否修改？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )
                if reply == QMessageBox.Yes:
                    sql = "UPDATE users SET uname=%s,email = %s,passwords=%s,entime=%s WHERE uname = %s"
                    cursor.execute(
                        sql, (self.ui.username.text(), self.ui.email.text(), self.ui.passwords.text(), self.ui.date.text(), self.oldname))
                    # self.username = newname
                    connection.commit()
                    # print("修改成功:", cursor.rowcount)
                    QMessageBox.information(
                        self, "修改成功!", "修改成功!")
                    self.getuserdata()
                    self.showuserdata()

    def add(self):
        pattern1 = r'\d{4}-\d{1,2}-\d{1,2}'
        pattern2 = r'\d{4}/\d{1,2}/\d{1,2}'
        match1 = re.match(pattern1, self.ui.date.text())
        match2 = re.match(pattern2, self.ui.date.text())
        if self.ui.username.text() == "" and self.ui.passwords.text() == "" and self.ui.email.text() == "" and self.ui.date.text() == "":
            QMessageBox.critical(self, '错误', '请填入信息!')
        elif self.ui.username.text() == "" or self.ui.passwords.text() == "" or self.ui.date.text() == "":
            QMessageBox.critical(self, '错误', '用户、密码和注册日期不能为空！')
        elif not match1 and not match2:
            QMessageBox.critical(
                self, '错误', '输入正确格式的日期(xxxx-xx-xx或xxxx/xx/xx)')
        else:
            connection = cnx()
            cursor = connection.cursor()
            sql = "SELECT uname FROM users"
            cursor.execute(sql)
            results = cursor.fetchall()
            tname = self.ui.username.text().lower()
            # print(temp)
            # print(results)
            judge = True
            for i in range(len(results)):
                if results[i][0].lower() == tname:
                    judge = False
                    break
            if judge == False:
                QMessageBox.critical(self, '错误', '该用户名已存在,请删除或修改后继续')
            else:
                sql = "INSERT INTO users(uname,email,passwords,entime,is_admin) VALUES (%s, %s, %s, %s,%s)"
                value = (self.ui.username.text(), self.ui.email.text(),
                         self.ui.passwords.text(), self.ui.date.text(), 0)
                cursor.execute(sql, value)
                # self.username = newname
                connection.commit()
                # print("修改成功:", cursor.rowcount)
                QMessageBox.information(
                    self, "添加成功!", "添加用户成功!")
                self.getuserdata()
                self.showuserdata()

    def delet(self):
        if self.ui.username.text() == "":
            QMessageBox.critical(self, '错误', '请选择用户!')
        else:
            connection = cnx()
            cursor = connection.cursor()
            sql = "SELECT uname FROM users where is_admin=0"
            cursor.execute(sql)
            results = cursor.fetchall()
            temp = (self.ui.username.text(),)
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
                        self, "删除成功!", "删除用户成功!")
                    self.getuserdata()#刷新
                    self.showuserdata()
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

        