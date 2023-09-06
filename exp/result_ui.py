# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'result.ui'
##
# Created by: Qt User Interface Compiler version 6.5.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
                               QRadioButton, QSizePolicy, QStackedWidget, QTableWidget,
                               QTableWidgetItem, QWidget)


class Ui_result(object):
    def setupUi(self, result):
        if not result.objectName():
            result.setObjectName(u"result")
        result.resize(676, 641)
        self.label_2 = QLabel(result)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 0, 131, 51))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.stackedWidget = QStackedWidget(result)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 270, 561, 361))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pic_1 = QLabel(self.page)
        self.pic_1.setObjectName(u"pic_1")
        self.pic_1.setGeometry(QRect(23, 15, 501, 341))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pic_2 = QLabel(self.page_2)
        self.pic_2.setObjectName(u"pic_2")
        self.pic_2.setGeometry(QRect(13, 15, 511, 321))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.pic_3 = QLabel(self.page_3)
        self.pic_3.setObjectName(u"pic_3")
        self.pic_3.setGeometry(QRect(23, 15, 511, 321))
        self.stackedWidget.addWidget(self.page_3)
        self.ROC = QRadioButton(result)
        self.ROC.setObjectName(u"ROC")
        self.ROC.setGeometry(QRect(590, 340, 95, 20))
        self.ROC.setChecked(True)
        self.p_r = QRadioButton(result)
        self.p_r.setObjectName(u"p_r")
        self.p_r.setGeometry(QRect(590, 420, 95, 20))
        self.learn = QRadioButton(result)
        self.learn.setObjectName(u"learn")
        self.learn.setGeometry(QRect(590, 490, 95, 20))
        self.tableWidget = QTableWidget(result)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 50, 661, 211))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label = QLabel(result)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 51, 16))
        self.id = QLabel(result)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(70, 20, 111, 16))

        self.retranslateUi(result)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(result)
    # setupUi

    def retranslateUi(self, result):
        result.setWindowTitle(QCoreApplication.translate(
            "result", u"\u8bad\u7ec3\u7ed3\u679c", None))
        result.setStyleSheet(QCoreApplication.translate("result", u"\n"
                                                        "        #result{background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4DA2CB, stop:1 #67B26F);}\n"
                                                        "        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);\n"
                                                        "        QPushButton {\n"
                                                        "        border-radius: 5px;\n"
                                                        "        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 0, 255));\n"
                                                        "        color: white;\n"
                                                        "        padding: 5px 10px;\n"
                                                        "        }\n"
                                                        "        QPushButton:hover {\n"
                                                        "        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
                                                        "        }\n"
                                                        "        QLabel {\n"
                                                        "        font-family: \"Arial\";\n"
                                                        "        font-size: 14px;\n"
                                                        "        color: #FF00FF;\n"
                                                        "        text-align: center;\n"
                                                        "        }\n"
                                                        "        QTableWidget {\n"
                                                        "        background-color: #222222; /* \u80cc\u666f\u989c\u8272 */\n"
                                                        "        alternate-background-color: #333333; /* \u4ea4\u66ff\u884c\u80cc\u666f\u989c\u8272 */\n"
                                                        "        border: none; /* \u53bb\u9664\u8fb9"
                                                        "\u6846 */\n"
                                                        "        /* \u6eda\u52a8\u6761\u6837\u5f0f */\n"
                                                        "        QScrollBar:vertical {\n"
                                                        "        background-color: #111111;\n"
                                                        "        width: 12px;\n"
                                                        "        margin: 0px 0px 0px 0px;\n"
                                                        "        }\n"
                                                        "        QScrollBar::handle:vertical {\n"
                                                        "        background-color: #888888;\n"
                                                        "        min-height: 20px;\n"
                                                        "        }\n"
                                                        "        QScrollBar::handle:vertical:hover {\n"
                                                        "        background-color: #999999;\n"
                                                        "        }\n"
                                                        "        QScrollBar::add-line:vertical,\n"
                                                        "        QScrollBar::sub-line:vertical {\n"
                                                        "        background: none;\n"
                                                        "        height: 0px;\n"
                                                        "        width: 0px;\n"
                                                        "        }\n"
                                                        "        QScrollBar::add-page:vertical,\n"
                                                        "        QScrollBar::sub-page:vertical {\n"
                                                        "        background: none;\n"
                                                        "        }\n"
                                                        "        }\n"
                                                        "        QTableWidget::item {\n"
                                                        "        padding: 5px; /* \u5355\u5143\u683c\u5185\u8fb9\u8ddd */\n"
                                                        "        background-color: #222222; /* \u5355\u5143\u683c\u80cc\u666f\u989c\u8272 */\n"
                                                        "        color: #FFFFFF; /* \u6587\u5b57\u989c\u8272 */\n"
                                                        "        borde"
                                                        "r-bottom: 1px solid #333333; /* \u5355\u5143\u683c\u5e95\u90e8\u8fb9\u6846 */\n"
                                                        "        }\n"
                                                        "        QTableWidget::item:hover {\n"
                                                        "        background-color: #555555; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
                                                        "        }\n"
                                                        "        QTableWidget::item:selected {\n"
                                                        "        background-color: #FF6600; /* \u9009\u4e2d\u5355\u5143\u683c\u7684\u80cc\u666f\u989c\u8272 */\n"
                                                        "        color: #FFFFFF; /* \u9009\u4e2d\u5355\u5143\u683c\u7684\u6587\u5b57\u989c\u8272 */\n"
                                                        "        }\n"
                                                        "        QHeaderView {\n"
                                                        "        background-color: #222222; /* \u8868\u5934\u80cc\u666f\u989c\u8272 */\n"
                                                        "        border: none; /* \u53bb\u9664\u8fb9\u6846 */\n"
                                                        "        }\n"
                                                        "        QHeaderView::section {\n"
                                                        "        padding: 5px; /* \u8868\u5934\u5185\u8fb9\u8ddd */\n"
                                                        "        background-color: #222222; /* \u8868\u5934\u80cc\u666f\u989c\u8272 */\n"
                                                        "        color: #FFFFFF; /* \u8868\u5934\u6587\u5b57\u989c\u8272 */\n"
                                                        "        border-bottom: 1px solid #333333; /* \u8868\u5934\u5e95\u90e8\u8fb9\u6846 */\n"
                                                        "      "
                                                        "  }\n"
                                                        "        QHeaderView::section:hover {\n"
                                                        "        background-color: #555555; /* \u60ac\u505c\u65f6\u7684\u8868\u5934\u80cc\u666f\u989c\u8272 */\n"
                                                        "        }\n"
                                                        "        QHeaderView::section:checked {\n"
                                                        "        background-color: #FF6600; /* \u9009\u4e2d\u7684\u8868\u5934\u80cc\u666f\u989c\u8272 */\n"
                                                        "        color: #FFFFFF; /* \u9009\u4e2d\u7684\u8868\u5934\u6587\u5b57\u989c\u8272 */\n"
                                                        "        }\n"
                                                        "      ", None))
        self.label_2.setText(QCoreApplication.translate(
            "result", u"\u8bad\u7ec3\u7ed3\u679c", None))
        self.pic_1.setText("")
        self.pic_2.setText("")
        self.pic_3.setText("")
        self.ROC.setText(QCoreApplication.translate(
            "result", u"\u56fe1", None))
        self.p_r.setText(QCoreApplication.translate(
            "result", u"\u56fe2", None))
        self.learn.setText(QCoreApplication.translate(
            "result", u"\u56fe3", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate(
            "result", u"\u8bc4\u4ef7\u6307\u6807", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("result", u"\u6570\u636e", None))
        self.label.setText(QCoreApplication.translate(
            "result", u"\u5b9e\u9a8cID\uff1a", None))
        self.id.setText(QCoreApplication.translate("result", u"11111", None))
    # retranslateUi
