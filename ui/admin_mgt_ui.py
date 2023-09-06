# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_mgt.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_admin_mgt(object):
    def setupUi(self, admin_mgt):
        if not admin_mgt.objectName():
            admin_mgt.setObjectName(u"admin_mgt")
        admin_mgt.resize(728, 561)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(admin_mgt.sizePolicy().hasHeightForWidth())
        admin_mgt.setSizePolicy(sizePolicy)
        admin_mgt.setMinimumSize(QSize(630, 558))
        admin_mgt.setMaximumSize(QSize(1000, 1000))
        admin_mgt.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u"../image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        admin_mgt.setWindowIcon(icon)
        self.label_2 = QLabel(admin_mgt)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 0, 221, 51))
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.delet = QPushButton(admin_mgt)
        self.delet.setObjectName(u"delet")
        self.delet.setGeometry(QRect(130, 490, 121, 61))
        self.tableWidget = QTableWidget(admin_mgt)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 14):
            self.tableWidget.setRowCount(14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(220, 80, 301, 341))
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
        self.change = QPushButton(admin_mgt)
        self.change.setObjectName(u"change")
        self.change.setGeometry(QRect(300, 490, 121, 61))
        self.change.setMaximumSize(QSize(1000, 400))
        self.adminname = QLineEdit(admin_mgt)
        self.adminname.setObjectName(u"adminname")
        self.adminname.setGeometry(QRect(270, 440, 111, 31))
        self.label = QLabel(admin_mgt)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(203, 440, 71, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setCursor(QCursor(Qt.IBeamCursor))
        self.passwords = QLineEdit(admin_mgt)
        self.passwords.setObjectName(u"passwords")
        self.passwords.setGeometry(QRect(430, 440, 121, 31))
        self.label_4 = QLabel(admin_mgt)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 440, 54, 31))
        self.label_4.setFont(font1)
        self.add = QPushButton(admin_mgt)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(470, 490, 121, 61))
        self.add.setMaximumSize(QSize(1000, 400))
        self.label_6 = QLabel(admin_mgt)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(520, 20, 54, 16))
        self.search_admin = QLineEdit(admin_mgt)
        self.search_admin.setObjectName(u"search_admin")
        self.search_admin.setGeometry(QRect(450, 30, 171, 41))
        self.search_admin.setFont(font1)
        self.search_admin.setTabletTracking(False)
        self.search_admin.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.search = QPushButton(admin_mgt)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(570, 40, 75, 24))
        self.search.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u"../image/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon1)

        self.retranslateUi(admin_mgt)

        QMetaObject.connectSlotsByName(admin_mgt)
    # setupUi

    def retranslateUi(self, admin_mgt):
        admin_mgt.setWindowTitle(QCoreApplication.translate("admin_mgt", u"\u4fe1\u606f\u7ba1\u7406", None))
        admin_mgt.setStyleSheet(QCoreApplication.translate("admin_mgt", u"\n"
"        #admin_mgt {\n"
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
"        QHeaderView::section:h"
                        "over {\n"
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
"        background-color: #4299F"
                        "F;\n"
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
        self.label_2.setText(QCoreApplication.translate("admin_mgt", u"\u7ba1\u7406\u5458\u4fe1\u606f\u7ba1\u7406", None))
        self.delet.setText(QCoreApplication.translate("admin_mgt", u"\u5220\u9664", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("admin_mgt", u"\u7ba1\u7406\u5458\u540d", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("admin_mgt", u"\u5bc6\u7801", None));
        self.change.setText(QCoreApplication.translate("admin_mgt", u"\u4fee\u6539", None))
        self.label.setText(QCoreApplication.translate("admin_mgt", u"\u7ba1\u7406\u5458\u540d", None))
        self.label_4.setText(QCoreApplication.translate("admin_mgt", u"\u5bc6\u7801", None))
        self.add.setText(QCoreApplication.translate("admin_mgt", u"\u6dfb\u52a0", None))
        self.label_6.setText("")
        self.search_admin.setPlaceholderText(QCoreApplication.translate("admin_mgt", u"\u641c\u7d22", None))
        self.search.setText("")
    # retranslateUi

