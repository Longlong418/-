# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'user_information.ui'
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


class Ui_user_information(object):
    def setupUi(self, user_information):
        if not user_information.objectName():
            user_information.setObjectName(u"user_information")
        user_information.resize(623, 584)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            user_information.sizePolicy().hasHeightForWidth())
        user_information.setSizePolicy(sizePolicy)
        user_information.setMinimumSize(QSize(483, 360))
        user_information.setMaximumSize(QSize(100000, 1000000))
        font = QFont()
        font.setFamilies([u"\u65b0\u5b8b\u4f53"])
        font.setPointSize(14)
        user_information.setFont(font)
        icon = QIcon()
        icon.addFile(u"../image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        user_information.setWindowIcon(icon)
        user_information.setStyleSheet(u"\n"
                                       "        QWidget#user_information{\n"
                                       "          background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                       "        stop:0 #BC95C6, stop:1 #3498db);\n"
                                       "\n"
                                       "        }\n"
                                       "        \n"
                                       "        QLabel#label_2 {\n"
                                       "        font-size: 24px;\n"
                                       "        font-family: \"\u6977\u4f53\";\n"
                                       "        }\n"
                                       "        QLabel#label_4,\n"
                                       "        QLabel#label_5,\n"
                                       "        QLabel#label_6,\n"
                                       "        QLabel#label_3,\n"
                                       "        QLabel#label_8,\n"
                                       "        QLabel#label_9 {\n"
                                       "        font-size: 14px;\n"
                                       "        }\n"
                                       "        QLineEdit#username,\n"
                                       "        QLineEdit#email,\n"
                                       "        QLineEdit#passwords,\n"
                                       "        QLineEdit#passwords_2,\n"
                                       "        QLineEdit#passwords_3 {\n"
                                       "        border: 1px solid #ccc;\n"
                                       "        border-radius: 5px;\n"
                                       "        padding: 5px;\n"
                                       "        }\n"
                                       "        QPushButton#save,\n"
                                       "        QPushButton#change {\n"
                                       "        background-color: #007bff;\n"
                                       "        color: #fff;\n"
                                       "        border: none;\n"
                                       "        border-radius: 5px;\n"
                                       "        padding: 10px;\n"
                                       "        transition: backgro"
                                       "und-color 0.3s ease-in-out;\n"
                                       "        }\n"
                                       "        QPushButton#save:hover,\n"
                                       "        QPushButton#change:hover {\n"
                                       "        background-color: #0056b3;\n"
                                       "        }\n"
                                       "        QLabel#label {\n"
                                       "        font-size: 10px;\n"
                                       "        font-family: \"\u9ed1\u4f53\";\n"
                                       "        animation: pulsate 1s infinite alternate;\n"
                                       "        }\n"
                                       "        QLabel#dates,\n"
                                       "        QLabel#label_7 {\n"
                                       "        font-size: 12px;\n"
                                       "        }\n"
                                       "        QLabel#change_pass {\n"
                                       "        font-size: 24px;\n"
                                       "        font-family: \"\u6977\u4f53\";\n"
                                       "        }\n"
                                       "        QLabel#label_7 {\n"
                                       "        color: #ccc;\n"
                                       "        }\n"
                                       "        @keyframes pulsate {\n"
                                       "        0% {\n"
                                       "        transform: scale(1);\n"
                                       "        }\n"
                                       "        50% {\n"
                                       "        transform: scale(1.2);\n"
                                       "        }\n"
                                       "        100% {\n"
                                       "        transform: scale(1);\n"
                                       "        }\n"
                                       "        }\n"
                                       "      ")
        self.label_2 = QLabel(user_information)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 20, 291, 51))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        self.label_2.setFont(font1)
        self.label_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_4 = QLabel(user_information)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 140, 54, 16))
        self.label_5 = QLabel(user_information)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 180, 81, 31))
        self.label_6 = QLabel(user_information)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 90, 61, 21))
        self.username = QLineEdit(user_information)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(190, 80, 271, 31))
        self.email = QLineEdit(user_information)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(190, 130, 271, 31))
        self.save = QPushButton(user_information)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(200, 220, 151, 51))
        self.label = QLabel(user_information)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 50, 151, 21))
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        self.label.setFont(font2)
        self.dates = QLabel(user_information)
        self.dates.setObjectName(u"dates")
        self.dates.setGeometry(QRect(190, 180, 181, 31))
        self.label_7 = QLabel(user_information)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 290, 621, 20))
        self.change_pass = QLabel(user_information)
        self.change_pass.setObjectName(u"change_pass")
        self.change_pass.setGeometry(QRect(200, 310, 291, 51))
        self.change_pass.setFont(font1)
        self.change_pass.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_3 = QLabel(user_information)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 360, 61, 31))
        self.passwords = QLineEdit(user_information)
        self.passwords.setObjectName(u"passwords")
        self.passwords.setGeometry(QRect(180, 360, 261, 31))
        self.passwords.setEchoMode(QLineEdit.Password)
        self.label_8 = QLabel(user_information)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 410, 101, 31))
        self.passwords_2 = QLineEdit(user_information)
        self.passwords_2.setObjectName(u"passwords_2")
        self.passwords_2.setGeometry(QRect(180, 410, 261, 31))
        self.passwords_2.setEchoMode(QLineEdit.Password)
        self.label_9 = QLabel(user_information)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 460, 141, 31))
        self.passwords_3 = QLineEdit(user_information)
        self.passwords_3.setObjectName(u"passwords_3")
        self.passwords_3.setGeometry(QRect(180, 460, 261, 31))
        self.passwords_3.setEchoMode(QLineEdit.Password)
        self.change = QPushButton(user_information)
        self.change.setObjectName(u"change")
        self.change.setGeometry(QRect(200, 510, 151, 51))

        self.retranslateUi(user_information)

        QMetaObject.connectSlotsByName(user_information)
    # setupUi

    def retranslateUi(self, user_information):
        user_information.setWindowTitle(QCoreApplication.translate(
            "user_information", u"\u4e2a\u4eba\u4fe1\u606f\u9875\u9762", None))
        self.label_2.setText(QCoreApplication.translate(
            "user_information", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate(
            "user_information", u"\u90ae\u7bb1", None))
        self.label_5.setText(QCoreApplication.translate(
            "user_information", u"\u6ce8\u518c\u65e5\u671f", None))
        self.label_6.setText(QCoreApplication.translate(
            "user_information", u"\u7528\u6237\u540d", None))
        self.username.setText(QCoreApplication.translate(
            "user_information", u"\u5982\u679c\u4f60\u662f\u6b63\u5e38\u8fd0\u884c\u7a0b\u5e8f\u770b\u5230\u7684\u8fd9\u53e5\u8bdd", None))
        self.email.setText("")
        self.save.setText(QCoreApplication.translate(
            "user_information", u"\u4fdd\u5b58", None))
        self.label.setText(QCoreApplication.translate(
            "user_information", u"\u70b9\u51fb\u5bf9\u5e94\u9879\u5373\u53ef\u7f16\u8f91\u4fe1\u606f", None))
        self.dates.setText(QCoreApplication.translate(
            "user_information", u"\u90a3\u8bf4\u660e\u9047\u5230bug\u4e86", None))
        self.label_7.setText(QCoreApplication.translate("user_information", u"\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", None))
        self.change_pass.setText(QCoreApplication.translate(
            "user_information", u"\u5bc6\u7801\u4fee\u6539", None))
        self.label_3.setText(QCoreApplication.translate(
            "user_information", u"\u539f\u5bc6\u7801", None))
        self.passwords.setText("")
        self.label_8.setText(QCoreApplication.translate(
            "user_information", u"\u8f93\u5165\u65b0\u5bc6\u7801", None))
        self.passwords_2.setText("")
        self.label_9.setText(QCoreApplication.translate(
            "user_information", u"\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801", None))
        self.passwords_3.setText("")
        self.change.setText(QCoreApplication.translate(
            "user_information", u"\u4fee\u6539", None))
    # retranslateUi
