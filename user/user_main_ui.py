# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'user_main.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
                               QWidget)


class Ui_user_main(object):
    def setupUi(self, user_main):
        if not user_main.objectName():
            user_main.setObjectName(u"user_main")
        user_main.resize(832, 539)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            user_main.sizePolicy().hasHeightForWidth())
        user_main.setSizePolicy(sizePolicy)
        user_main.setMinimumSize(QSize(832, 539))
        user_main.setMaximumSize(QSize(832, 539))
        icon = QIcon()
        icon.addFile(u"image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        user_main.setWindowIcon(icon)
        user_main.setStyleSheet(u"\n"
                                "        QWidget#user_main{\n"
                                "        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                "        stop:0 #FF5F6D, stop:1 #3498db);\n"
                                "        }\n"
                                "      ")
        self.background_label = QLabel(user_main)
        self.background_label.setObjectName(u"background_label")
        self.background_label.setGeometry(QRect(0, 0, 832, 539))
        self.background_label.setPixmap(QPixmap(u"image/bg_.jpg"))
        self.background_label.setScaledContents(True)
        self.label_2 = QLabel(user_main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 20, 351, 51))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(207, 205, 193);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.information = QPushButton(user_main)
        self.information.setObjectName(u"information")
        self.information.setGeometry(QRect(270, 300, 291, 151))
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(24)
        self.information.setFont(font1)
        self.information.setStyleSheet(u"\n"
                                       "          QPushButton#information {\n"
                                       "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #cfc9bd, stop:1 #3498db);\n"
                                       "          border-radius: 10px;\n"
                                       "          color: white;\n"
                                       "          }\n"
                                       "          QPushButton#information:hover {\n"
                                       "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #3498db, stop:1 #FF5F6D);\n"
                                       "          }\n"
                                       "          QPushButton#information:pressed {\n"
                                       "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFC371, stop:1 #FF5F6D);\n"
                                       "          padding-left: 5px;\n"
                                       "          padding-top: 5px;\n"
                                       "          }\n"
                                       "        ")
        self.label_3 = QLabel(user_main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(720, 520, 111, 20))
        self.train = QPushButton(user_main)
        self.train.setObjectName(u"train")
        self.train.setGeometry(QRect(80, 110, 291, 151))
        self.train.setFont(font1)
        self.train.setStyleSheet(u"\n"
                                 "          QPushButton#train {\n"
                                 "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #133374,stop:1  #d3d9cb);\n"
                                 "          border-radius: 10px;\n"
                                 "          color: white;\n"
                                 " 	\n"
                                 "          }\n"
                                 "          QPushButton#train:hover {\n"
                                 "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #173776, stop:1 #6B73FF);\n"
                                 "          }\n"
                                 "          QPushButton#train:pressed {\n"
                                 "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #000DFF, stop:1 #6B73FF);\n"
                                 "          padding-left: 5px;\n"
                                 "          padding-top: 5px;\n"
                                 "          }\n"
                                 "        ")
        self.logout = QPushButton(user_main)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(370, 480, 91, 51))
        self.logout.setFont(font1)
        self.logout.setStyleSheet(u"\n"
                                  "          QPushButton#logout {\n"
                                  "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #365d39, stop:1 #53788f);\n"
                                  "          border-radius: 10px;\n"
                                  "          color: white;\n"
                                  "          }\n"
                                  "          QPushButton#logout:hover {\n"
                                  "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFC371, stop:1 #FF5F6D);\n"
                                  "          }\n"
                                  "          QPushButton#logout:pressed {\n"
                                  "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFC371, stop:1 #FF5F6D);\n"
                                  "          padding-left: 5px;\n"
                                  "          padding-top: 5px;\n"
                                  "          }\n"
                                  "        ")
        self.record = QPushButton(user_main)
        self.record.setObjectName(u"record")
        self.record.setGeometry(QRect(460, 110, 291, 151))
        self.record.setFont(font1)
        self.record.setStyleSheet(u"\n"
                                  "          QPushButton#record {\n"
                                  "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #8a8da2, stop:1 #3498db);\n"
                                  "          border-radius: 10px;\n"
                                  "          color: white;\n"
                                  "          }\n"
                                  "          QPushButton#record:hover {\n"
                                  "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #173776, stop:1 #6B73FF);\n"
                                  "          }\n"
                                  "          QPushButton#record:pressed {\n"
                                  "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #000DFF, stop:1 #6B73FF);\n"
                                  "          padding-left: 5px;\n"
                                  "          padding-top: 5px;\n"
                                  "          }\n"
                                  "        ")
        self.username = QLabel(user_main)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(620, 40, 131, 16))
        font2 = QFont()
        font2.setFamilies([u"\u6977\u4f53"])
        font2.setPointSize(12)
        self.username.setFont(font2)
        self.username.setStyleSheet(u"color: rgb(207, 197, 188);")

        self.retranslateUi(user_main)

        QMetaObject.connectSlotsByName(user_main)
    # setupUi

    def retranslateUi(self, user_main):
        user_main.setWindowTitle(QCoreApplication.translate(
            "user_main", u"\u673a\u5668\u5b66\u4e60\u5b9e\u9a8c\u7ba1\u7406\u5e73\u53f0", None))
        self.background_label.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "user_main", u"\u673a\u5668\u5b66\u4e60\u5b9e\u9a8c\u7ba1\u7406\u5e73\u53f0", None))
        self.information.setText(QCoreApplication.translate(
            "user_main", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate(
            "user_main", u"Made by Longlong", None))
        self.train.setText(QCoreApplication.translate(
            "user_main", u"\u6a21\u578b\u8bad\u7ec3", None))
        self.logout.setText(QCoreApplication.translate(
            "user_main", u"\u6ce8\u9500", None))
        self.record.setText(QCoreApplication.translate(
            "user_main", u"\u5b9e\u9a8c\u8bb0\u5f55", None))
        self.username.setText(QCoreApplication.translate(
            "user_main", u"\u6b22\u8fce\u60a8\uff0c", None))
    # retranslateUi
