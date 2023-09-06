# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'train.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_train(object):
    def setupUi(self, train):
        if not train.objectName():
            train.setObjectName(u"train")
        train.resize(752, 639)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(train.sizePolicy().hasHeightForWidth())
        train.setSizePolicy(sizePolicy)
        train.setMinimumSize(QSize(540, 542))
        train.setMaximumSize(QSize(1000, 1000))
        font = QFont()
        font.setPointSize(12)
        train.setFont(font)
        icon = QIcon()
        icon.addFile(u"../image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        train.setWindowIcon(icon)
        train.setStyleSheet(u"\n"
"        QWidget#train {\n"
"        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff6600,stop:1 #d3d9cb);\n"
"        }\n"
"        QLabel#label_2 {\n"
"        color: #ffffff;\n"
"        font-size: 30px;\n"
"        font-family: Impact;\n"
"        }\n"
"        QPushButton#uptest,\n"
"        QPushButton#uptrain,\n"
"        QPushButton#start_train {\n"
"        background-color: #ff6600;\n"
"        color: #ffffff;\n"
"        font-size: 16px;\n"
"        font-weight: bold;\n"
"        border-radius: 5px;\n"
"        padding: 8px 16px;\n"
"        }\n"
"        QPushButton#uptest:hover,\n"
"        QPushButton#uptrain:hover,\n"
"        QPushButton#start_train:hover {\n"
"        background-color: #ff8000;\n"
"        }\n"
"        QLabel#label,\n"
"        QLabel#label_3,\n"
"        QLabel#label_8,\n"
"        QLabel#label_9,\n"
"        QLabel#label_10,\n"
"        QLabel#label_11,\n"
"        QLabel#label_12,\n"
"        QLabel#label_13,\n"
"        QLabel#label_14 {\n"
"      "
                        "  color: #ffffff;\n"
"        }\n"
"        QComboBox#modelchoice {\n"
"        background-color: #ffffff;\n"
"        color: #333333;\n"
"        font-size: 12px;\n"
"        border-radius: 5px;\n"
"        padding: 2px 8px;\n"
"        }\n"
"        QComboBox#modelchoice::drop-down {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        width: 20px;\n"
"        border-left-width: 1px;\n"
"        border-left-color: #888888;\n"
"        border-left-style: solid;\n"
"        }\n"
"        QComboBox#modelchoice::down-arrow {\n"
"        image: url(../image/down_arrow.png);\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        }\n"
"        QLineEdit {\n"
"        background-color: #ffffff;\n"
"        color: #333333;\n"
"        font-size: 12px;\n"
"        border-radius: 5px;\n"
"        padding: 4px;\n"
"        }\n"
"        QLabel#test_data,\n"
"        QLabel#train_data {\n"
"        color: #ff6600;\n"
"        font-size: 10px;\n"
"        }\n"
"        QS"
                        "tackedWidget#stackedWidget {\n"
"        background-color: #ee934f;\n"
"        border: 1px solid #888888;\n"
"        border-radius: 20px;\n"
"        padding: 8px;\n"
"        }\n"
"        QLabel#label_6,\n"
"        QLabel#label_7,\n"
"        QLabel#label_15,\n"
"        QLabel#label_16,\n"
"        QLabel#label_17,\n"
"        QLabel#label_18,\n"
"        QLabel#label_19,\n"
"        QLabel#label_20,\n"
"        QLabel#label_21,\n"
"        QLabel#label_22,\n"
"        QLabel#label_23,\n"
"        QLabel#label_24,\n"
"        QLabel#label_25,\n"
"        QLabel#label_26,\n"
"        QLabel#label_27,\n"
"        QLabel#label_28,\n"
"        {\n"
"        color: #ffffff;\n"
"        font-size: 12px;\n"
"        font-weight: bold;\n"
"        }\n"
"        QComboBox#l_penalty,\n"
"        QComboBox#l_solver {\n"
"        background-color: #ffffff;\n"
"        color: #333333;\n"
"        font-size: 12px;\n"
"        border-radius: 5px;\n"
"        padding: 2px 8px;\n"
"        }\n"
"        QComboBox#l_penal"
                        "ty::drop-down,\n"
"        QComboBox#l_solver::drop-down {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        width: 20px;\n"
"        border-left-width: 1px;\n"
"        border-left-color: #888888;\n"
"        border-left-style: solid;\n"
"        }\n"
"        QComboBox#l_penalty::down-arrow,\n"
"        QComboBox#l_solver::down-arrow {\n"
"        image: url(image/down_arrow.png);\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        }\n"
"      ")
        self.label_2 = QLabel(train)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 10, 141, 61))
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.uptest = QPushButton(train)
        self.uptest.setObjectName(u"uptest")
        self.uptest.setGeometry(QRect(180, 100, 111, 61))
        self.label = QLabel(train)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 100, 101, 61))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(12)
        self.label.setFont(font2)
        self.label_3 = QLabel(train)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 190, 101, 61))
        self.label_3.setFont(font2)
        self.uptrain = QPushButton(train)
        self.uptrain.setObjectName(u"uptrain")
        self.uptrain.setGeometry(QRect(180, 190, 111, 61))
        self.modelchoice = QComboBox(train)
        self.modelchoice.addItem("")
        self.modelchoice.addItem("")
        self.modelchoice.addItem("")
        self.modelchoice.addItem("")
        self.modelchoice.setObjectName(u"modelchoice")
        self.modelchoice.setGeometry(QRect(180, 280, 171, 22))
        self.label_8 = QLabel(train)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(-10, 300, 761, 20))
        self.label_9 = QLabel(train)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(-10, 250, 781, 20))
        self.label_10 = QLabel(train)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 130, 131, 81))
        font3 = QFont()
        font3.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
        font3.setPointSize(16)
        self.label_10.setFont(font3)
        self.label_11 = QLabel(train)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(-10, 70, 761, 20))
        self.label_12 = QLabel(train)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 250, 131, 81))
        self.label_12.setFont(font3)
        self.label_13 = QLabel(train)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 370, 91, 81))
        self.label_13.setFont(font3)
        self.label_14 = QLabel(train)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(-20, 530, 771, 20))
        self.start_train = QPushButton(train)
        self.start_train.setObjectName(u"start_train")
        self.start_train.setGeometry(QRect(230, 570, 101, 51))
        self.test_data = QLabel(train)
        self.test_data.setObjectName(u"test_data")
        self.test_data.setGeometry(QRect(390, 120, 301, 21))
        font4 = QFont()
        self.test_data.setFont(font4)
        self.test_data.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.train_data = QLabel(train)
        self.train_data.setObjectName(u"train_data")
        self.train_data.setGeometry(QRect(390, 210, 311, 21))
        self.train_data.setFont(font4)
        self.train_data.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget = QStackedWidget(train)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(130, 330, 321, 191))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.l_c = QLineEdit(self.page)
        self.l_c.setObjectName(u"l_c")
        self.l_c.setGeometry(QRect(110, 60, 161, 21))
        self.l_c.setClearButtonEnabled(True)
        self.l_max_i = QLineEdit(self.page)
        self.l_max_i.setObjectName(u"l_max_i")
        self.l_max_i.setGeometry(QRect(110, 100, 161, 21))
        self.l_max_i.setClearButtonEnabled(True)
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 20, 71, 21))
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 60, 21, 21))
        self.label_15 = QLabel(self.page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 100, 71, 20))
        self.l_penalty = QComboBox(self.page)
        self.l_penalty.addItem("")
        self.l_penalty.addItem("")
        self.l_penalty.addItem("")
        self.l_penalty.addItem("")
        self.l_penalty.setObjectName(u"l_penalty")
        self.l_penalty.setGeometry(QRect(110, 20, 161, 21))
        self.label_16 = QLabel(self.page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 140, 54, 16))
        self.l_solver = QComboBox(self.page)
        self.l_solver.addItem("")
        self.l_solver.addItem("")
        self.l_solver.addItem("")
        self.l_solver.addItem("")
        self.l_solver.addItem("")
        self.l_solver.setObjectName(u"l_solver")
        self.l_solver.setGeometry(QRect(110, 140, 161, 31))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_17 = QLabel(self.page_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(70, 100, 31, 20))
        self.x_penalty = QComboBox(self.page_2)
        self.x_penalty.addItem("")
        self.x_penalty.addItem("")
        self.x_penalty.addItem("")
        self.x_penalty.addItem("")
        self.x_penalty.setObjectName(u"x_penalty")
        self.x_penalty.setGeometry(QRect(110, 20, 161, 21))
        self.x_tol = QLineEdit(self.page_2)
        self.x_tol.setObjectName(u"x_tol")
        self.x_tol.setGeometry(QRect(110, 100, 161, 21))
        self.x_tol.setClearButtonEnabled(True)
        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(80, 60, 21, 21))
        self.label_19 = QLabel(self.page_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(63, 140, 41, 20))
        self.label_20 = QLabel(self.page_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 20, 71, 21))
        self.x_loss = QComboBox(self.page_2)
        self.x_loss.addItem("")
        self.x_loss.addItem("")
        self.x_loss.setObjectName(u"x_loss")
        self.x_loss.setGeometry(QRect(110, 140, 161, 31))
        self.x_c = QLineEdit(self.page_2)
        self.x_c.setObjectName(u"x_c")
        self.x_c.setGeometry(QRect(110, 60, 161, 21))
        self.x_c.setClearButtonEnabled(True)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_21 = QLabel(self.page_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 60, 91, 21))
        self.dt_max_f = QComboBox(self.page_3)
        self.dt_max_f.addItem("")
        self.dt_max_f.addItem("")
        self.dt_max_f.addItem("")
        self.dt_max_f.addItem("")
        self.dt_max_f.setObjectName(u"dt_max_f")
        self.dt_max_f.setGeometry(QRect(150, 140, 181, 31))
        self.label_22 = QLabel(self.page_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 140, 101, 20))
        self.label_23 = QLabel(self.page_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 100, 141, 20))
        self.dt_max_d = QLineEdit(self.page_3)
        self.dt_max_d.setObjectName(u"dt_max_d")
        self.dt_max_d.setGeometry(QRect(150, 60, 181, 21))
        self.dt_max_d.setClearButtonEnabled(True)
        self.dt_min_s = QLineEdit(self.page_3)
        self.dt_min_s.setObjectName(u"dt_min_s")
        self.dt_min_s.setGeometry(QRect(150, 100, 181, 21))
        self.dt_min_s.setClearButtonEnabled(True)
        self.dt_criterion = QComboBox(self.page_3)
        self.dt_criterion.addItem("")
        self.dt_criterion.addItem("")
        self.dt_criterion.setObjectName(u"dt_criterion")
        self.dt_criterion.setGeometry(QRect(150, 20, 181, 31))
        self.label_24 = QLabel(self.page_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(10, 20, 71, 21))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_25 = QLabel(self.page_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 100, 141, 20))
        self.max_iter = QLineEdit(self.page_4)
        self.max_iter.setObjectName(u"max_iter")
        self.max_iter.setGeometry(QRect(100, 60, 181, 21))
        self.label_26 = QLabel(self.page_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 60, 91, 21))
        self.label_27 = QLabel(self.page_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 140, 101, 20))
        self.label_28 = QLabel(self.page_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 20, 71, 21))
        self.active = QComboBox(self.page_4)
        self.active.addItem("")
        self.active.addItem("")
        self.active.addItem("")
        self.active.addItem("")
        self.active.setObjectName(u"active")
        self.active.setGeometry(QRect(100, 100, 181, 21))
        self.batch_size = QLineEdit(self.page_4)
        self.batch_size.setObjectName(u"batch_size")
        self.batch_size.setGeometry(QRect(100, 20, 151, 20))
        self.learrate = QLineEdit(self.page_4)
        self.learrate.setObjectName(u"learrate")
        self.learrate.setGeometry(QRect(100, 140, 181, 20))
        self.stackedWidget.addWidget(self.page_4)
        self.parm = QLineEdit(train)
        self.parm.setObjectName(u"parm")
        self.parm.setGeometry(QRect(460, 350, 261, 131))
        self.label_4 = QLabel(train)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 320, 271, 21))
        font5 = QFont()
        font5.setPointSize(9)
        self.label_4.setFont(font5)
        self.label_5 = QLabel(train)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(460, 500, 311, 16))

        self.retranslateUi(train)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(train)
    # setupUi

    def retranslateUi(self, train):
        train.setWindowTitle(QCoreApplication.translate("train", u"\u6a21\u578b\u8bad\u7ec3", None))
        self.label_2.setText(QCoreApplication.translate("train", u"\u6a21\u578b\u8bad\u7ec3", None))
        self.uptest.setText(QCoreApplication.translate("train", u"\u4e0a\u4f20\u6d4b\u8bd5\u96c6", None))
        self.label.setText(QCoreApplication.translate("train", u"\u5df2\u9009\u6d4b\u8bd5\u96c6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("train", u"\u5df2\u9009\u8bad\u7ec3\u96c6\uff1a", None))
        self.uptrain.setText(QCoreApplication.translate("train", u"\u4e0a\u4f20\u8bad\u7ec3\u96c6", None))
        self.modelchoice.setItemText(0, QCoreApplication.translate("train", u"Logistic\u56de\u5f52\u5206\u7c7b\u5668", None))
        self.modelchoice.setItemText(1, QCoreApplication.translate("train", u"\u7ebf\u6027\u652f\u6301\u5411\u91cf\u5206\u7c7b", None))
        self.modelchoice.setItemText(2, QCoreApplication.translate("train", u"\u51b3\u7b56\u6811\u5206\u7c7b\u5668", None))
        self.modelchoice.setItemText(3, QCoreApplication.translate("train", u"MLPClassifier", None))

        self.label_8.setText(QCoreApplication.translate("train", u"---------------------------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.label_9.setText(QCoreApplication.translate("train", u"---------------------------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.label_10.setText(QCoreApplication.translate("train", u"\u6570\u636e\u96c6\u4e0a\u4f20", None))
        self.label_11.setText(QCoreApplication.translate("train", u"---------------------------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.label_12.setText(QCoreApplication.translate("train", u"\u6a21\u578b\u9009\u62e9", None))
        self.label_13.setText(QCoreApplication.translate("train", u"\u53c2\u6570\u9009\u62e9", None))
        self.label_14.setText(QCoreApplication.translate("train", u"---------------------------------------------------------------------------------------------------------------------------------------------------------------", None))
        self.start_train.setText(QCoreApplication.translate("train", u"\u8bad\u7ec3", None))
        self.test_data.setText(QCoreApplication.translate("train", u"\u6682\u65e0", None))
        self.train_data.setText(QCoreApplication.translate("train", u"\u6682\u65e0", None))
        self.l_c.setText(QCoreApplication.translate("train", u"1.0", None))
        self.l_c.setPlaceholderText(QCoreApplication.translate("train", u"\u6b63\u5219\u5316\u53c2\u6570,float>0", None))
        self.l_max_i.setText(QCoreApplication.translate("train", u"100", None))
        self.l_max_i.setPlaceholderText(QCoreApplication.translate("train", u"\u6536\u655b\u7684\u6700\u5927\u8fed\u4ee3\u6b21\u6570", None))
        self.label_6.setText(QCoreApplication.translate("train", u"penalty", None))
        self.label_7.setText(QCoreApplication.translate("train", u"C", None))
        self.label_15.setText(QCoreApplication.translate("train", u"max_iter", None))
        self.l_penalty.setItemText(0, QCoreApplication.translate("train", u"l2", None))
        self.l_penalty.setItemText(1, QCoreApplication.translate("train", u"l1", None))
        self.l_penalty.setItemText(2, QCoreApplication.translate("train", u"elasticnet", None))
        self.l_penalty.setItemText(3, QCoreApplication.translate("train", u"none", None))

        self.l_penalty.setCurrentText(QCoreApplication.translate("train", u"l2", None))
        self.label_16.setText(QCoreApplication.translate("train", u"solver", None))
        self.l_solver.setItemText(0, QCoreApplication.translate("train", u"newton-cg", None))
        self.l_solver.setItemText(1, QCoreApplication.translate("train", u"lbfgs", None))
        self.l_solver.setItemText(2, QCoreApplication.translate("train", u"liblinear", None))
        self.l_solver.setItemText(3, QCoreApplication.translate("train", u"sag", None))
        self.l_solver.setItemText(4, QCoreApplication.translate("train", u"saga", None))

        self.l_solver.setCurrentText(QCoreApplication.translate("train", u"newton-cg", None))
        self.label_17.setText(QCoreApplication.translate("train", u"tol", None))
        self.x_penalty.setItemText(0, QCoreApplication.translate("train", u"l2", None))
        self.x_penalty.setItemText(1, QCoreApplication.translate("train", u"l1", None))
        self.x_penalty.setItemText(2, QCoreApplication.translate("train", u"elasticnet", None))
        self.x_penalty.setItemText(3, QCoreApplication.translate("train", u"none", None))

        self.x_penalty.setCurrentText(QCoreApplication.translate("train", u"l2", None))
        self.x_tol.setText(QCoreApplication.translate("train", u"0.0001", None))
        self.x_tol.setPlaceholderText(QCoreApplication.translate("train", u"\u5bb9\u5dee\u503c,float>0", None))
        self.label_18.setText(QCoreApplication.translate("train", u"C", None))
        self.label_19.setText(QCoreApplication.translate("train", u"loss", None))
        self.label_20.setText(QCoreApplication.translate("train", u"penalty", None))
        self.x_loss.setItemText(0, QCoreApplication.translate("train", u"hinge", None))
        self.x_loss.setItemText(1, QCoreApplication.translate("train", u"squared_hinge", None))

        self.x_loss.setCurrentText(QCoreApplication.translate("train", u"hinge", None))
        self.x_c.setText(QCoreApplication.translate("train", u"1.0", None))
        self.x_c.setPlaceholderText(QCoreApplication.translate("train", u"\u6b63\u5219\u5316\u53c2\u6570,float>0", None))
        self.label_21.setText(QCoreApplication.translate("train", u"max_depth", None))
        self.dt_max_f.setItemText(0, QCoreApplication.translate("train", u"auto", None))
        self.dt_max_f.setItemText(1, QCoreApplication.translate("train", u"sqrt", None))
        self.dt_max_f.setItemText(2, QCoreApplication.translate("train", u"log2", None))
        self.dt_max_f.setItemText(3, QCoreApplication.translate("train", u"None", None))

        self.dt_max_f.setCurrentText(QCoreApplication.translate("train", u"auto", None))
        self.label_22.setText(QCoreApplication.translate("train", u"max_features", None))
        self.label_23.setText(QCoreApplication.translate("train", u"min_samples_split", None))
        self.dt_max_d.setText(QCoreApplication.translate("train", u"1", None))
        self.dt_max_d.setPlaceholderText(QCoreApplication.translate("train", u"int>0", None))
        self.dt_min_s.setText(QCoreApplication.translate("train", u"2", None))
        self.dt_min_s.setPlaceholderText(QCoreApplication.translate("train", u"\u5bb9\u5dee\u503c,float>0", None))
        self.dt_criterion.setItemText(0, QCoreApplication.translate("train", u"gini", None))
        self.dt_criterion.setItemText(1, QCoreApplication.translate("train", u"entropy", None))

        self.dt_criterion.setCurrentText(QCoreApplication.translate("train", u"gini", None))
        self.label_24.setText(QCoreApplication.translate("train", u"criterion", None))
        self.label_25.setText(QCoreApplication.translate("train", u"\u6fc0\u6d3b\u51fd\u6570", None))
        self.max_iter.setText(QCoreApplication.translate("train", u"200", None))
        self.max_iter.setPlaceholderText(QCoreApplication.translate("train", u"int>0 ,\u6700\u5927\u8fed\u4ee3\u6b21\u6570", None))
        self.label_26.setText(QCoreApplication.translate("train", u"max_iter", None))
        self.label_27.setText(QCoreApplication.translate("train", u"learning_rate", None))
        self.label_28.setText(QCoreApplication.translate("train", u"batch_size", None))
        self.active.setItemText(0, QCoreApplication.translate("train", u"relu", None))
        self.active.setItemText(1, QCoreApplication.translate("train", u"logistic", None))
        self.active.setItemText(2, QCoreApplication.translate("train", u"tanh", None))
        self.active.setItemText(3, QCoreApplication.translate("train", u"identity", None))

        self.active.setCurrentText(QCoreApplication.translate("train", u"relu", None))
        self.batch_size.setInputMask("")
        self.batch_size.setText(QCoreApplication.translate("train", u"200", None))
        self.batch_size.setPlaceholderText(QCoreApplication.translate("train", u"int>0", None))
        self.learrate.setText(QCoreApplication.translate("train", u"0.0001", None))
        self.learrate.setPlaceholderText(QCoreApplication.translate("train", u"float,\u521d\u59cb\u5b66\u4e60\u7387", None))
        self.parm.setPlaceholderText(QCoreApplication.translate("train", u"{\"penalty\":\"l2\",\"C\":1.0}", None))
        self.label_4.setText(QCoreApplication.translate("train", u"\u81ea\u5b9a\u4e49\u4f20\u53c2\uff1a\u6309\u7167\u4e0b\u9762\u7684\u5f62\u5f0f\u4f20\u53c2\uff0c\u5426\u5219\u4f1a\u51fa\u9519", None))
        self.label_5.setText(QCoreApplication.translate("train", u"\u8f93\u5165\u7684\u53c2\u6570\u9519\u8bef\u4e5f\u4f1a\u51fa\u9519,\uff08\u522b\u5fd8\u4e86\u5927\u62ec\u53f7\uff09", None))
    # retranslateUi

