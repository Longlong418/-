# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Signup(object):
    def setupUi(self, Signup):
        if not Signup.objectName():
            Signup.setObjectName(u"Signup")
        Signup.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"../image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Signup.setWindowIcon(icon)
        self.label = QLabel(Signup)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 161, 101))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.sign = QPushButton(Signup)
        self.sign.setObjectName(u"sign")
        self.sign.setGeometry(QRect(150, 210, 75, 24))
        self.username = QLineEdit(Signup)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(110, 100, 171, 31))
        self.username.setStyleSheet(u"\n"
"          QLineEdit#username {\n"
"          border: 2px solid #ffffff;\n"
"          border-radius: 5px;\n"
"          padding: 2px 4px;\n"
"          background-color: #f2f2f2;\n"
"          }\n"
"        ")
        self.passwords1 = QLineEdit(Signup)
        self.passwords1.setObjectName(u"passwords1")
        self.passwords1.setGeometry(QRect(110, 150, 171, 20))
        self.passwords1.setStyleSheet(u"\n"
"          QLineEdit#passwords1 {\n"
"          border: 2px solid #ffffff;\n"
"          border-radius: 5px;\n"
"          padding: 2px 4px;\n"
"          background-color: #f2f2f2;\n"
"          }\n"
"        ")
        self.passwords1.setEchoMode(QLineEdit.Password)
        self.passwords2 = QLineEdit(Signup)
        self.passwords2.setObjectName(u"passwords2")
        self.passwords2.setGeometry(QRect(110, 180, 171, 20))
        self.passwords2.setStyleSheet(u"\n"
"          QLineEdit#passwords2 {\n"
"          border: 2px solid #ffffff;\n"
"          border-radius: 5px;\n"
"          padding: 2px 4px;\n"
"          background-color: #f2f2f2;\n"
"          }\n"
"        ")
        self.passwords2.setEchoMode(QLineEdit.Password)
        self.label_2 = QLabel(Signup)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 80, 241, 20))

        self.retranslateUi(Signup)

        QMetaObject.connectSlotsByName(Signup)
    # setupUi

    def retranslateUi(self, Signup):
        Signup.setWindowTitle(QCoreApplication.translate("Signup", u"\u7528\u6237\u6ce8\u518c", None))
        Signup.setStyleSheet(QCoreApplication.translate("Signup", u"\n"
"        QWidget#Signup {\n"
"        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #2c3e50, stop:1 #3498db);\n"
"        }\n"
"      ", None))
        self.label.setStyleSheet(QCoreApplication.translate("Signup", u"\n"
"          QLabel#label {\n"
"          color: #ffffff;\n"
"          }\n"
"        ", None))
        self.label.setText(QCoreApplication.translate("Signup", u"\u7528\u6237\u6ce8\u518c", None))
        self.sign.setStyleSheet(QCoreApplication.translate("Signup", u"\n"
"          QPushButton#sign {\n"
"          background-color: #3498db;\n"
"          color: #ffffff;\n"
"          border: none;\n"
"          border-radius: 5px;\n"
"          padding: 5px 10px;\n"
"          }\n"
"          QPushButton#sign:hover {\n"
"          background-color: #45aaf2;\n"
"          }\n"
"          QPushButton#sign:pressed {\n"
"          background-color: #2980b9;\n"
"          }\n"
"        ", None))
        self.sign.setText(QCoreApplication.translate("Signup", u"\u6ce8\u518c", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Signup", u"\u8f93\u5165\u7528\u6237\u540d", None))
        self.passwords1.setPlaceholderText(QCoreApplication.translate("Signup", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.passwords2.setText("")
        self.passwords2.setPlaceholderText(QCoreApplication.translate("Signup", u"\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801", None))
        self.label_2.setStyleSheet(QCoreApplication.translate("Signup", u"\n"
"          QLabel#label_2 {\n"
"          color: #ffffff;\n"
"          }\n"
"        ", None))
        self.label_2.setText(QCoreApplication.translate("Signup", u"\u8bf7\u8bbe\u7f6e6\u4f4d\u4ee5\u4e0a\u7684\u5bc6\u7801~", None))
    # retranslateUi

