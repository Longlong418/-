# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'admin_main.ui'
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


class Ui_admin_main(object):
    def setupUi(self, admin_main):
        if not admin_main.objectName():
            admin_main.setObjectName(u"admin_main")
        admin_main.resize(827, 532)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            admin_main.sizePolicy().hasHeightForWidth())
        admin_main.setSizePolicy(sizePolicy)
        admin_main.setMinimumSize(QSize(827, 532))
        admin_main.setMaximumSize(QSize(827, 532))
        icon = QIcon()
        icon.addFile(u"image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        admin_main.setWindowIcon(icon)
        self.background_label = QLabel(admin_main)
        self.background_label.setObjectName(u"background_label")
        self.background_label.setGeometry(QRect(0, 0, 832, 539))
        self.background_label.setPixmap(QPixmap(u"image/bg_.jpg"))
        self.background_label.setScaledContents(True)
        self.logout = QPushButton(admin_main)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(370, 440, 91, 51))
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(24)
        self.logout.setFont(font)
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
        self.label_2 = QLabel(admin_main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 50, 351, 51))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(24)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"\n"
                                   "          color: rgb(207, 205, 193);\n"
                                   "          color: rgb(255, 255, 255);\n"
                                   "        ")
        self.label_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.record = QPushButton(admin_main)
        self.record.setObjectName(u"record")
        self.record.setGeometry(QRect(460, 140, 291, 151))
        self.record.setFont(font)
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
        self.label_3 = QLabel(admin_main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(710, 510, 111, 20))
        self.user = QPushButton(admin_main)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(80, 140, 291, 151))
        self.user.setFont(font)
        self.user.setStyleSheet(u"\n"
                                "          QPushButton#user {\n"
                                "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #133374,stop:1 #d3d9cb);\n"
                                "          border-radius: 10px;\n"
                                "          color: white;\n"
                                "          }\n"
                                "          QPushButton#user:hover {\n"
                                "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #173776, stop:1 #6B73FF);\n"
                                "          }\n"
                                "          QPushButton#user:pressed {\n"
                                "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #000DFF, stop:1 #6B73FF);\n"
                                "          padding-left: 5px;\n"
                                "          padding-top: 5px;\n"
                                "          }\n"
                                "        ")
        self.admin = QPushButton(admin_main)
        self.admin.setObjectName(u"admin")
        self.admin.setGeometry(QRect(320, 320, 191, 101))
        self.admin.setFont(font)
        self.admin.setStyleSheet(u"\n"
                                 "          QPushButton#admin{\n"
                                 "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #cfc9bd, stop:1 #3498db);\n"
                                 "          border-radius: 10px;\n"
                                 "          color: white;\n"
                                 "          }\n"
                                 "          QPushButton#admin:hover {\n"
                                 "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #3498db, stop:1 #FF5F6D);\n"
                                 "          }\n"
                                 "          QPushButton#admin:pressed {\n"
                                 "          background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFC371, stop:1 #FF5F6D);\n"
                                 "          padding-left: 5px;\n"
                                 "          padding-top: 5px;\n"
                                 "          }\n"
                                 "        ")
        self.label = QLabel(admin_main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(610, 70, 151, 21))
        font2 = QFont()
        font2.setFamilies([u"\u534e\u6587\u6977\u4f53"])
        font2.setPointSize(11)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(207, 197, 188);")

        self.retranslateUi(admin_main)

        QMetaObject.connectSlotsByName(admin_main)
    # setupUi

    def retranslateUi(self, admin_main):
        admin_main.setWindowTitle(QCoreApplication.translate(
            "admin_main", u"\u673a\u5668\u5b66\u4e60\u5b9e\u9a8c\u7ba1\u7406\u5e73\u53f0", None))
        self.background_label.setText("")
        self.logout.setText(QCoreApplication.translate(
            "admin_main", u"\u6ce8\u9500", None))
        self.label_2.setText(QCoreApplication.translate(
            "admin_main", u"\u673a\u5668\u5b66\u4e60\u5b9e\u9a8c\u7ba1\u7406\u5e73\u53f0", None))
        self.record.setText(QCoreApplication.translate(
            "admin_main", u"\u5b9e\u9a8c\u8bb0\u5f55\u7ba1\u7406", None))
        self.label_3.setText(QCoreApplication.translate(
            "admin_main", u"Made by Longlong", None))
        self.user.setText(QCoreApplication.translate(
            "admin_main", u"\u7528\u6237\u7ba1\u7406", None))
        self.admin.setText(QCoreApplication.translate(
            "admin_main", u"\u7ba1\u7406\u5458\u7ba1\u7406", None))
        self.label.setText(QCoreApplication.translate(
            "admin_main", u"\u6b22\u8fce\u60a8\uff0c\u7ba1\u7406\u5458", None))
    # retranslateUi
