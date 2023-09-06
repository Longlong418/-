# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'data_info.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)


class Ui_data_info(object):
    def setupUi(self, data_info):
        if not data_info.objectName():
            data_info.setObjectName(u"data_info")
        data_info.resize(528, 379)
        data_info.setStyleSheet(
            u" #data_info{background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4DA2CB, stop:1 #67B26F);}")
        self.label_2 = QLabel(data_info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 0, 181, 51))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label = QLabel(data_info)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 81, 41))
        font1 = QFont()
        font1.setFamilies([u"\u4eff\u5b8b"])
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label_3 = QLabel(data_info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 80, 71, 16))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(11)
        self.label_3.setFont(font2)
        self.label_10 = QLabel(data_info)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(-10, 160, 541, 20))
        self.label_4 = QLabel(data_info)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 81, 41))
        self.label_4.setFont(font1)
        self.test_path = QLabel(data_info)
        self.test_path.setObjectName(u"test_path")
        self.test_path.setGeometry(QRect(120, 80, 451, 16))
        self.label_6 = QLabel(data_info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 110, 71, 16))
        self.label_6.setFont(font2)
        self.label_7 = QLabel(data_info)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 140, 71, 16))
        self.label_7.setFont(font2)
        self.test_sum = QLabel(data_info)
        self.test_sum.setObjectName(u"test_sum")
        self.test_sum.setGeometry(QRect(120, 110, 421, 16))
        self.test_dim = QLabel(data_info)
        self.test_dim.setObjectName(u"test_dim")
        self.test_dim.setGeometry(QRect(120, 140, 281, 16))
        self.label_8 = QLabel(data_info)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 250, 71, 16))
        self.label_8.setFont(font2)
        self.train_dim = QLabel(data_info)
        self.train_dim.setObjectName(u"train_dim")
        self.train_dim.setGeometry(QRect(120, 280, 411, 16))
        self.label_5 = QLabel(data_info)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 220, 71, 16))
        self.label_5.setFont(font2)
        self.train_path = QLabel(data_info)
        self.train_path.setObjectName(u"train_path")
        self.train_path.setGeometry(QRect(120, 220, 421, 16))
        self.label_9 = QLabel(data_info)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 280, 51, 16))
        self.label_9.setFont(font2)
        self.train_sum = QLabel(data_info)
        self.train_sum.setObjectName(u"train_sum")
        self.train_sum.setGeometry(QRect(120, 250, 451, 16))
        self.username = QLabel(data_info)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(100, 330, 181, 31))
        font3 = QFont()
        font3.setFamilies([u"\u6977\u4f53"])
        font3.setPointSize(12)
        self.username.setFont(font3)

        self.retranslateUi(data_info)

        QMetaObject.connectSlotsByName(data_info)
    # setupUi

    def retranslateUi(self, data_info):
        data_info.setWindowTitle(QCoreApplication.translate(
            "data_info", u"\u6570\u636e\u96c6\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate(
            "data_info", u"\u6570\u636e\u96c6\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate(
            "data_info", u"\u6d4b\u8bd5\u96c6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate(
            "data_info", u"\u8def\u5f84:", None))
        self.label_10.setText(QCoreApplication.translate("data_info", u"\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", None))
        self.label_4.setText(QCoreApplication.translate(
            "data_info", u"\u8bad\u7ec3\u96c6\uff1a", None))
        self.test_path.setText(QCoreApplication.translate(
            "data_info", u"\u7a7a", None))
        self.label_6.setText(QCoreApplication.translate(
            "data_info", u"\u6837\u672c\u603b\u6570\uff1a", None))
        self.label_7.setText(QCoreApplication.translate(
            "data_info", u"\u7ef4\u5ea6:", None))
        self.test_sum.setText(QCoreApplication.translate(
            "data_info", u"\u7a7a", None))
        self.test_dim.setText(QCoreApplication.translate(
            "data_info", u"\u7a7a", None))
        self.label_8.setText(QCoreApplication.translate(
            "data_info", u"\u6837\u672c\u603b\u6570\uff1a", None))
        self.train_dim.setText(QCoreApplication.translate(
            "data_info", u"\u7a7a", None))
        self.label_5.setText(QCoreApplication.translate(
            "data_info", u"\u8def\u5f84:", None))
        self.train_path.setText(
            QCoreApplication.translate("data_info", u"\u7a7a", None))
        self.label_9.setText(QCoreApplication.translate(
            "data_info", u"\u7ef4\u5ea6:", None))
        self.train_sum.setText(QCoreApplication.translate(
            "data_info", u"\u7a7a", None))
        self.username.setText(QCoreApplication.translate(
            "data_info", u"\u7531\"\u7528\u6237\u540d\"\u4e0a\u4f20", None))
    # retranslateUi
