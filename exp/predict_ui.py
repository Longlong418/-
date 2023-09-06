# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'predict.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QTextEdit, QWidget)


class Ui_predict(object):
    def setupUi(self, predict):
        if not predict.objectName():
            predict.setObjectName(u"predict")
        predict.resize(731, 502)
        predict.setStyleSheet(
            u" #predict{background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4DA2CB, stop:1 #67B26F);}")
        self.pre = QPushButton(predict)
        self.pre.setObjectName(u"pre")
        self.pre.setGeometry(QRect(250, 410, 121, 41))
        self.pre.setMaximumSize(QSize(1000, 400))
        self.pre.setStyleSheet(u" QPushButton {\n"
                               "        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0#67B26F,stop:1 #4DA2CB);\n"
                               "        color: #FFFFFF;\n"
                               "        border: none; \n"
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
                               "        background-color: #4299FF;\n"
                               "        color: #FFFFFF;\n"
                               "        padding: 10px 20px;\n"
                               "        font-size: 16px;\n"
                               "        text-transform: uppercase;\n"
                               "        letter-spacing: 2px;\n"
                               "        outline: none;\n"
                               ""
                               "        }\n"
                               "        QPushButton:focus {\n"
                               "        outline: none;\n"
                               "        border: 2px solid #4299FF;\n"
                               "        }")
        self.label_6 = QLabel(predict)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(500, 30, 54, 16))
        self.label_2 = QLabel(predict)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 20, 221, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.name = QLabel(predict)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(150, 150, 421, 16))
        self.label_3 = QLabel(predict)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 100, 91, 31))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(16)
        self.label_3.setFont(font1)
        self.path = QLabel(predict)
        self.path.setObjectName(u"path")
        self.path.setGeometry(QRect(150, 110, 451, 16))
        self.label_8 = QLabel(predict)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 146, 91, 20))
        self.label_8.setFont(font1)
        self.input_x = QLineEdit(predict)
        self.input_x.setObjectName(u"input_x")
        self.input_x.setGeometry(QRect(130, 210, 581, 81))
        self.label = QLabel(predict)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 230, 81, 41))
        font2 = QFont()
        font2.setFamilies([u"\u6977\u4f53"])
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label_4 = QLabel(predict)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 180, 231, 16))
        self.label_5 = QLabel(predict)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 360, 54, 16))
        self.label_5.setFont(font1)
        self.result = QLabel(predict)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(130, 360, 231, 20))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(12)
        self.result.setFont(font3)
        self.label_7 = QLabel(predict)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 310, 54, 31))
        self.label_7.setFont(font1)
        self.X = QTextEdit(predict)
        self.X.setObjectName(u"X")
        self.X.setGeometry(QRect(130, 300, 581, 51))
        self.X.setReadOnly(True)

        self.retranslateUi(predict)

        QMetaObject.connectSlotsByName(predict)
    # setupUi

    def retranslateUi(self, predict):
        predict.setWindowTitle(QCoreApplication.translate(
            "predict", u"\u6a21\u578b\u9884\u6d4b", None))
        self.pre.setText(QCoreApplication.translate(
            "predict", u"\u9884\u6d4b", None))
        self.label_6.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "predict", u"\u6a21\u578b\u9884\u6d4b", None))
        self.name.setText(QCoreApplication.translate(
            "predict", u"\u7a7a", None))
        self.label_3.setText(QCoreApplication.translate(
            "predict", u"\u6a21\u578b\u8def\u5f84:", None))
        self.path.setText(QCoreApplication.translate(
            "predict", u"\u7a7a", None))
        self.label_8.setText(QCoreApplication.translate(
            "predict", u"\u6a21\u578b\u540d\u5b57\uff1a", None))
        self.input_x.setPlaceholderText(QCoreApplication.translate(
            "predict", u"\u4ee5\u5217\u8868\u5f62\u5f0f\u8f93\u5165\uff0c\u5982[6.1, 2.8, 4.7, 1.2]", None))
        self.label.setText(QCoreApplication.translate(
            "predict", u"\u8f93\u5165X:", None))
        self.label_4.setText(QCoreApplication.translate(
            "predict", u"\u6ce8\u610f\uff1a\u8f93\u5165X\u7684\u6570\u91cf\u5bf9\u5e94\u4e0b\u9762\u7684\u7279\u5f81", None))
        self.label_5.setText(QCoreApplication.translate(
            "predict", u"\u7ed3\u679c\uff1a", None))
        self.result.setText(
            QCoreApplication.translate("predict", u"none", None))
        self.label_7.setText(QCoreApplication.translate(
            "predict", u"\u7279\u5f81\uff1a", None))
        self.X.setHtml(QCoreApplication.translate("predict", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "hr { height: 1px; border-width: 0; }\n"
                                                  "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                  "li.checked::marker { content: \"\\2612\"; }\n"
                                                  "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5982\u679c\u4f60\u770b\u5230\u8fd9\u53e5\u8bdd\u8bf4\u660e\u9047\u5230bug\u4e86</p></body></html>", None))
    # retranslateUi
