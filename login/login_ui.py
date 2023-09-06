# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'login.ui'
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


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(547, 269)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QSize(547, 269))
        login.setMaximumSize(QSize(547, 269))
        icon = QIcon()
        icon.addFile(u"image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        login.setWindowIcon(icon)
        self.background_label = QLabel(login)
        self.background_label.setObjectName(u"background_label")
        self.background_label.setGeometry(QRect(0, 0, 547, 269))
        self.background_label.setPixmap(QPixmap(u"image/background.png"))
        self.background_label.setScaledContents(True)
        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 30, 51, 51))
        self.label.setPixmap(QPixmap(u"image/logo.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(4)
        self.label_2 = QLabel(login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 30, 351, 51))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.user_signup = QPushButton(login)
        self.user_signup.setObjectName(u"user_signup")
        self.user_signup.setGeometry(QRect(220, 140, 111, 71))
        self.label_3 = QLabel(login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 70, 111, 20))
        self.label_3.setStyleSheet(u"\n"
                                   "          QLabel#label_3 {\n"
                                   "          color: #808080;\n"
                                   "          font-size: 10px;\n"
                                   "          }\n"
                                   "\n"
                                   "        ")
        self.admin_login = QPushButton(login)
        self.admin_login.setObjectName(u"admin_login")
        self.admin_login.setGeometry(QRect(390, 140, 111, 71))
        self.user_login = QPushButton(login)
        self.user_login.setObjectName(u"user_login")
        self.user_login.setGeometry(QRect(50, 140, 111, 71))

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate(
            "login", u"\u767b\u5f55\u754c\u9762", None))
        self.background_label.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "login", u"\u673a\u5668\u5b66\u4e60\u5b9e\u9a8c\u7ba1\u7406\u5e73\u53f0", None))
        self.user_signup.setStyleSheet(QCoreApplication.translate("login", u"\n"
                                                                  "          QPushButton#user_signup {\n"
                                                                  "          background-color: #3498db;\n"
                                                                  "          color: #ffffff;\n"
                                                                  "          border-radius: 10px;\n"
                                                                  "          }\n"
                                                                  "          QPushButton#user_signup:hover {\n"
                                                                  "          background-color: #45aaf2;\n"
                                                                  "          }\n"
                                                                  "          QPushButton#user_signup:pressed {\n"
                                                                  "          background-color: #2980b9;\n"
                                                                  "          }\n"
                                                                  "        ", None))
        self.user_signup.setText(QCoreApplication.translate(
            "login", u"\u7528\u6237\u6ce8\u518c", None))
        self.label_3.setText(QCoreApplication.translate(
            "login", u"Made by Longlong", None))
        self.admin_login.setStyleSheet(QCoreApplication.translate("login", u"\n"
                                                                  "          QPushButton#admin_login {\n"
                                                                  "          background-color: #e74c3c;\n"
                                                                  "          color: #ffffff;\n"
                                                                  "          border-radius: 10px;\n"
                                                                  "          }\n"
                                                                  "          QPushButton#admin_login:hover {\n"
                                                                  "          background-color: #f05a4d;\n"
                                                                  "          }\n"
                                                                  "          QPushButton#admin_login:pressed {\n"
                                                                  "          background-color: #c0392b;\n"
                                                                  "          }\n"
                                                                  "        ", None))
        self.admin_login.setText(QCoreApplication.translate(
            "login", u"\u7ba1\u7406\u5458\u767b\u5f55", None))
        self.user_login.setStyleSheet(QCoreApplication.translate("login", u"\n"
                                                                 "          QPushButton#user_login {\n"
                                                                 "          background-color: #27ae60;\n"
                                                                 "          color: #ffffff;\n"
                                                                 "          border-radius: 10px;\n"
                                                                 "          }\n"
                                                                 "          QPushButton#user_login:hover {\n"
                                                                 "          background-color: #2ecc71;\n"
                                                                 "          }\n"
                                                                 "          QPushButton#user_login:pressed {\n"
                                                                 "          background-color: #1f8b4c;\n"
                                                                 "          }\n"
                                                                 "        ", None))
        self.user_login.setText(QCoreApplication.translate(
            "login", u"\u7528\u6237\u767b\u5f55", None))
    # retranslateUi
