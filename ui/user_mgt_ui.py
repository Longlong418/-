# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_mgt.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_user_mgt(object):
    def setupUi(self, user_mgt):
        if not user_mgt.objectName():
            user_mgt.setObjectName(u"user_mgt")
        user_mgt.resize(728, 561)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(user_mgt.sizePolicy().hasHeightForWidth())
        user_mgt.setSizePolicy(sizePolicy)
        user_mgt.setMinimumSize(QSize(630, 558))
        user_mgt.setMaximumSize(QSize(1000, 1000))
        icon = QIcon()
        icon.addFile(u"../image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        user_mgt.setWindowIcon(icon)
        self.label_2 = QLabel(user_mgt)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 0, 201, 51))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.delet = QPushButton(user_mgt)
        self.delet.setObjectName(u"delet")
        self.delet.setGeometry(QRect(130, 490, 121, 61))
        self.tableWidget = QTableWidget(user_mgt)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 14):
            self.tableWidget.setRowCount(14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 80, 571, 341))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(14)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.change = QPushButton(user_mgt)
        self.change.setObjectName(u"change")
        self.change.setGeometry(QRect(300, 490, 121, 61))
        self.change.setMaximumSize(QSize(1000, 400))
        self.username = QLineEdit(user_mgt)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(50, 440, 111, 31))
        self.label = QLabel(user_mgt)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 440, 54, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label_3 = QLabel(user_mgt)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 440, 54, 31))
        self.label_3.setFont(font1)
        self.email = QLineEdit(user_mgt)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(210, 440, 121, 31))
        self.label_5 = QLabel(user_mgt)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 440, 71, 31))
        self.label_5.setFont(font1)
        self.passwords = QLineEdit(user_mgt)
        self.passwords.setObjectName(u"passwords")
        self.passwords.setGeometry(QRect(380, 440, 121, 31))
        self.label_4 = QLabel(user_mgt)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 440, 54, 31))
        self.label_4.setFont(font1)
        self.add = QPushButton(user_mgt)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(470, 490, 121, 61))
        self.add.setMaximumSize(QSize(1000, 400))
        self.label_6 = QLabel(user_mgt)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(520, 20, 54, 16))
        self.search_user = QLineEdit(user_mgt)
        self.search_user.setObjectName(u"search_user")
        self.search_user.setGeometry(QRect(450, 30, 171, 41))
        self.search_user.setFont(font1)
        self.search_user.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.search = QPushButton(user_mgt)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(570, 40, 75, 24))
        self.search.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u"../image/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon1)
        self.date = QDateEdit(user_mgt)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(580, 440, 111, 31))
        self.date.setMinimumDate(QDate(1946, 2, 14))
        self.date.setDate(QDate(2023, 1, 1))

        self.retranslateUi(user_mgt)

        QMetaObject.connectSlotsByName(user_mgt)
    # setupUi

    def retranslateUi(self, user_mgt):
        user_mgt.setWindowTitle(QCoreApplication.translate("user_mgt", u"\u4fe1\u606f\u7ba1\u7406", None))
        user_mgt.setStyleSheet(QCoreApplication.translate("user_mgt", u"\n"
"        #user_mgt {\n"
"        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6190E8,stop:1 #A7BFE8);\n"
"        }\n"
"        QTableWidget {\n"
"        background-color: #FFFFFF;\n"
"        alternate-background-color: #F2F2F2;\n"
"        border: none;\n"
"        }\n"
"        QTableWidget::item {\n"
"        padding: 5px;\n"
"        background-color: #FFFFFF;\n"
"        color: #333333;\n"
"        border-bottom: 1px solid #E5E5E5;\n"
"        }\n"
"        QTableWidget::item:hover {\n"
"        background-color: #E6F2FF;\n"
"        }\n"
"        QTableWidget::item:selected {\n"
"        background-color: #4299FF;\n"
"        color: #FFFFFF;\n"
"        }\n"
"        QHeaderView {\n"
"        background-color: #6190E8;\n"
"        border: none;\n"
"        }\n"
"        QHeaderView::section {\n"
"        padding: 5px;\n"
"        background-color: #6190E8;\n"
"        color: #FFFFFF;\n"
"        border-bottom: 1px solid #4786D1;\n"
"        }\n"
"        QHeaderView::section:ho"
                        "ver {\n"
"        background-color: #4786D1;\n"
"        }\n"
"        QHeaderView::section:checked {\n"
"        background-color: #4299FF;\n"
"        color: #FFFFFF;\n"
"        }\n"
"        QPushButton {\n"
"        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6190E8,stop:1 #A7BFE8);\n"
"        color: #FFFFFF;\n"
"        border: none;\n"
"        padding: 10px 20px;\n"
"        font-size: 16px;\n"
"        border-radius: 10px;\n"
"        text-transform: uppercase;\n"
"        letter-spacing: 2px;\n"
"        }\n"
"        QPushButton:hover {\n"
"        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #A7BFE8,stop:1 #6190E8);\n"
"        }\n"
"        QPushButton:pressed {\n"
"        background-color: #366BA4;\n"
"        }\n"
"        QPushButton:disabled {\n"
"        background-color: #999999;\n"
"        color: #CCCCCC;\n"
"        }\n"
"        QPushButton:default {\n"
"        border: none;\n"
"        border-radius: 5px;\n"
"        background-color: #4299FF"
                        ";\n"
"        color: #FFFFFF;\n"
"        padding: 10px 20px;\n"
"        font-size: 16px;\n"
"        text-transform: uppercase;\n"
"        letter-spacing: 2px;\n"
"        outline: none;\n"
"        }\n"
"        QPushButton:focus {\n"
"        outline: none;\n"
"        border: 2px solid #4299FF;\n"
"        }\n"
"      ", None))
        self.label_2.setText(QCoreApplication.translate("user_mgt", u"\u7528\u6237\u4fe1\u606f\u7ba1\u7406", None))
        self.delet.setText(QCoreApplication.translate("user_mgt", u"\u5220\u9664", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("user_mgt", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("user_mgt", u"\u90ae\u7bb1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("user_mgt", u"\u5bc6\u7801", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("user_mgt", u"\u6ce8\u518c\u65e5\u671f", None));
        self.change.setText(QCoreApplication.translate("user_mgt", u"\u4fee\u6539", None))
        self.label.setText(QCoreApplication.translate("user_mgt", u"\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("user_mgt", u"\u90ae\u7bb1", None))
        self.label_5.setText(QCoreApplication.translate("user_mgt", u"\u6ce8\u518c\u65e5\u671f", None))
        self.label_4.setText(QCoreApplication.translate("user_mgt", u"\u5bc6\u7801", None))
        self.add.setText(QCoreApplication.translate("user_mgt", u"\u6dfb\u52a0", None))
        self.label_6.setText("")
        self.search_user.setPlaceholderText(QCoreApplication.translate("user_mgt", u"\u641c\u7d22", None))
        self.search.setText("")
    # retranslateUi

