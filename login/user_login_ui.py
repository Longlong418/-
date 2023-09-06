# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'user_login.ui'
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
                               QSizePolicy, QWidget)


class Ui_user_login(object):
    def setupUi(self, user_login):
        if not user_login.objectName():
            user_login.setObjectName(u"user_login")
        user_login.resize(391, 281)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            user_login.sizePolicy().hasHeightForWidth())
        user_login.setSizePolicy(sizePolicy)
        user_login.setMinimumSize(QSize(391, 281))
        user_login.setMaximumSize(QSize(391, 281))
        icon = QIcon()
        icon.addFile(u"../image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        user_login.setWindowIcon(icon)
        self.label = QLabel(user_login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 151, 101))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.username = QLineEdit(user_login)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(110, 110, 171, 20))
        self.passwords = QLineEdit(user_login)
        self.passwords.setObjectName(u"passwords")
        self.passwords.setGeometry(QRect(110, 150, 171, 20))
        self.passwords.setEchoMode(QLineEdit.Password)
        self.login = QPushButton(user_login)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(160, 190, 75, 24))

        self.retranslateUi(user_login)

        QMetaObject.connectSlotsByName(user_login)
    # setupUi

    def retranslateUi(self, user_login):
        user_login.setWindowTitle(QCoreApplication.translate(
            "user_login", u"\u7528\u6237\u767b\u5f55", None))
        user_login.setStyleSheet(QCoreApplication.translate("user_login", u"\n"
                                                            "        QWidget#user_login {\n"
                                                            "        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                                            "        stop:0 #2c3e50, stop:1 #3498db);\n"
                                                            "        }\n"
                                                            "      ", None))
        self.label.setText(QCoreApplication.translate(
            "user_login", u"\u7528\u6237\u767b\u5f55", None))
        self.label.setStyleSheet(QCoreApplication.translate("user_login", u"\n"
                                                            "          QLabel#label {\n"
                                                            "          color: #ffffff;\n"
                                                            "          }\n"
                                                            "        ", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate(
            "user_login", u"\u8f93\u5165\u60a8\u7684\u7528\u6237\u540d", None))
        self.username.setStyleSheet(QCoreApplication.translate("user_login", u"\n"
                                                               "          QLineEdit#username {\n"
                                                               "          border: 2px solid #3498db;\n"
                                                               "          border-radius: 5px;\n"
                                                               "          padding: 2px 4px;\n"
                                                               "          background-color: #f2f2f2;\n"
                                                               "          }\n"
                                                               "        ", None))
        self.passwords.setText("")
        self.passwords.setPlaceholderText(QCoreApplication.translate(
            "user_login", u"\u8f93\u5165\u60a8\u7684\u5bc6\u7801", None))
        self.passwords.setStyleSheet(QCoreApplication.translate("user_login", u"\n"
                                                                "          QLineEdit#passwords {\n"
                                                                "          border: 2px solid #3498db;\n"
                                                                "          border-radius: 5px;\n"
                                                                "          padding: 2px 4px;\n"
                                                                "          background-color: #f2f2f2;\n"
                                                                "          }\n"
                                                                "        ", None))
        self.login.setText(QCoreApplication.translate(
            "user_login", u"\u767b\u5f55", None))
        self.login.setStyleSheet(QCoreApplication.translate("user_login", u"\n"
                                                            "          QPushButton#login {\n"
                                                            "          background-color: #3498db;\n"
                                                            "          color: #ffffff;\n"
                                                            "          border: none;\n"
                                                            "          border-radius: 5px;\n"
                                                            "          padding: 5px 10px;\n"
                                                            "          }\n"
                                                            "          QPushButton#login:hover {\n"
                                                            "          background-color: #45aaf2;\n"
                                                            "          }\n"
                                                            "          QPushButton#login:pressed {\n"
                                                            "          background-color: #2980b9;\n"
                                                            "          }\n"
                                                            "        ", None))
    # retranslateUi
