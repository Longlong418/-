# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'admin_login.ui'
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


class Ui_admin_login(object):
    def setupUi(self, admin_login):
        if not admin_login.objectName():
            admin_login.setObjectName(u"admin_login")
        admin_login.resize(391, 281)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            admin_login.sizePolicy().hasHeightForWidth())
        admin_login.setSizePolicy(sizePolicy)
        admin_login.setMinimumSize(QSize(391, 281))
        admin_login.setMaximumSize(QSize(391, 281))
        icon = QIcon()
        icon.addFile(u"../image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        admin_login.setWindowIcon(icon)
        self.label = QLabel(admin_login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 161, 101))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.login = QPushButton(admin_login)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(160, 200, 75, 24))
        self.adname = QLineEdit(admin_login)
        self.adname.setObjectName(u"adname")
        self.adname.setGeometry(QRect(110, 120, 171, 20))
        self.adname.setStyleSheet(u"\n"
                                  "          QLineEdit#adname {\n"
                                  "          border: 2px solid #ffffff;\n"
                                  "          border-radius: 5px;\n"
                                  "          padding: 2px 4px;\n"
                                  "          background-color: #f2f2f2;\n"
                                  "          \n"
                                  "          }\n"
                                  "        ")
        self.passwords = QLineEdit(admin_login)
        self.passwords.setObjectName(u"passwords")
        self.passwords.setGeometry(QRect(110, 160, 171, 20))
        self.passwords.setContextMenuPolicy(Qt.NoContextMenu)
        self.passwords.setStyleSheet(u"\n"
                                     "          QLineEdit#passwords {\n"
                                     "          border: 2px solid #ffffff;\n"
                                     "          border-radius: 5px;\n"
                                     "          padding: 2px 4px;\n"
                                     "          background-color: #f2f2f2;\n"
                                     "          \n"
                                     "          }\n"
                                     "        ")
        self.passwords.setEchoMode(QLineEdit.Password)

        self.retranslateUi(admin_login)

        QMetaObject.connectSlotsByName(admin_login)
    # setupUi

    def retranslateUi(self, admin_login):
        admin_login.setWindowTitle(QCoreApplication.translate(
            "admin_login", u"\u7ba1\u7406\u5458\u767b\u9646", None))
        admin_login.setStyleSheet(QCoreApplication.translate("admin_login", u"\n"
                                                             "        QWidget#admin_login {\n"
                                                             "        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                                             "        stop:0 #2c3e50, stop:1 #3498db);\n"
                                                             "        }\n"
                                                             "      ", None))
        self.label.setStyleSheet(QCoreApplication.translate("admin_login", u"\n"
                                                            "          QLabel#label {\n"
                                                            "          color: #ffffff;\n"
                                                            "          }\n"
                                                            "        ", None))
        self.label.setText(QCoreApplication.translate(
            "admin_login", u"\u7ba1\u7406\u5458\u767b\u5f55", None))
        self.login.setStyleSheet(QCoreApplication.translate("admin_login", u"\n"
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
        self.login.setText(QCoreApplication.translate(
            "admin_login", u"\u767b\u5f55", None))
        self.adname.setText("")
        self.adname.setPlaceholderText(QCoreApplication.translate(
            "admin_login", u"\u8f93\u5165\u60a8\u7684\u7ba1\u7406\u5458\u540d", None))
        self.passwords.setText("")
        self.passwords.setPlaceholderText(QCoreApplication.translate(
            "admin_login", u"\u8f93\u5165\u60a8\u7684\u5bc6\u7801", None))
    # retranslateUi
