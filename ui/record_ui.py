# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_record(object):
    def setupUi(self, record):
        if not record.objectName():
            record.setObjectName(u"record")
        record.resize(912, 612)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(record.sizePolicy().hasHeightForWidth())
        record.setSizePolicy(sizePolicy)
        record.setMinimumSize(QSize(912, 612))
        record.setMaximumSize(QSize(912, 612))
        font = QFont()
        font.setPointSize(10)
        record.setFont(font)
        icon = QIcon()
        icon.addFile(u"../image/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        record.setWindowIcon(icon)
        self.label_2 = QLabel(record)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 0, 141, 51))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(24)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.table = QTableWidget(record)
        if (self.table.columnCount() < 8):
            self.table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.table.rowCount() < 2):
            self.table.setRowCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setItem(0, 1, __qtablewidgetitem9)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 60, 891, 471))
        self.table.setLineWidth(1)
        self.table.setMidLineWidth(1)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.table.setAutoScroll(True)
        self.table.setAutoScrollMargin(19)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setTextElideMode(Qt.ElideRight)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setSortingEnabled(True)
        self.table.setWordWrap(True)
        self.table.setCornerButtonEnabled(True)
        self.table.horizontalHeader().setDefaultSectionSize(125)
        self.remove = QPushButton(record)
        self.remove.setObjectName(u"remove")
        self.remove.setGeometry(QRect(670, 540, 141, 71))
        self.data = QPushButton(record)
        self.data.setObjectName(u"data")
        self.data.setGeometry(QRect(320, 540, 141, 71))
        self.results = QPushButton(record)
        self.results.setObjectName(u"results")
        self.results.setGeometry(QRect(120, 540, 161, 71))
        self.search_user = QLineEdit(record)
        self.search_user.setObjectName(u"search_user")
        self.search_user.setGeometry(QRect(570, 10, 171, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.search_user.setFont(font2)
        self.search_user.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.search = QPushButton(record)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(690, 20, 75, 24))
        self.search.setStyleSheet(u"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u"../image/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon1)
        self.predict = QPushButton(record)
        self.predict.setObjectName(u"predict")
        self.predict.setGeometry(QRect(490, 540, 141, 71))

        self.retranslateUi(record)

        QMetaObject.connectSlotsByName(record)
    # setupUi

    def retranslateUi(self, record):
        record.setWindowTitle(QCoreApplication.translate("record", u"\u5b9e\u9a8c\u8bb0\u5f55", None))
        record.setStyleSheet(QCoreApplication.translate("record", u"\n"
"        #record {\n"
"        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6190E8,stop:1 #A7BFE8);\n"
"        }\n"
"        QTableWidget {\n"
"        background-color: #FFFFFF;\n"
"        alternate-background-color: #F2F2F2;\n"
"        border: none;\n"
"        }\n"
"        QTableWidget::item {\n"
"        padding: 5px;\n"
"        background-color: #FFFFFF;\n"
"        color: #333333;\n"
"        border-bottom: 1px solid #E5E5E5;\n"
"        }\n"
"        QTableWidget::item:hover {\n"
"        background-color: #E6F2FF;\n"
"        }\n"
"        QTableWidget::item:selected {\n"
"        background-color: #4299FF;\n"
"        color: #FFFFFF;\n"
"        }\n"
"        QHeaderView {\n"
"        background-color: #6190E8;\n"
"        border: none;\n"
"        }\n"
"        QHeaderView::section {\n"
"        padding: 5px;\n"
"        background-color: #6190E8;\n"
"        color: #FFFFFF;\n"
"        border-bottom: 1px solid #4786D1;\n"
"        }\n"
"        QHeaderView::section:hove"
                        "r {\n"
"        background-color: #4786D1;\n"
"        }\n"
"        QHeaderView::section:checked {\n"
"        background-color: #4299FF;\n"
"        color: #FFFFFF;\n"
"        }\n"
"        QPushButton {\n"
"        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6190E8,stop:1 #A7BFE8);\n"
"        color: #FFFFFF;\n"
"        border: none;\n"
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
""
                        "        color: #FFFFFF;\n"
"        padding: 10px 20px;\n"
"        font-size: 16px;\n"
"        text-transform: uppercase;\n"
"        letter-spacing: 2px;\n"
"        outline: none;\n"
"        }\n"
"        QPushButton:focus {\n"
"        outline: none;\n"
"        border: 2px solid #4299FF;\n"
"        }\n"
"      ", None))
        self.label_2.setText(QCoreApplication.translate("record", u"\u5b9e\u9a8c\u8bb0\u5f55", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("record", u"\u5b9e\u9a8c_id", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("record", u"\u7528\u6237", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("record", u"\u8bad\u7ec3\u96c6", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("record", u"\u6d4b\u8bd5\u96c6", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("record", u"\u6a21\u578b", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("record", u"\u53c2\u6570", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("record", u"\u8bad\u7ec3\u7ed3\u679c", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("record", u"\u5b9e\u9a8c\u65f6\u95f4", None));

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)

        self.remove.setText(QCoreApplication.translate("record", u"\u5220\u9664", None))
        self.data.setText(QCoreApplication.translate("record", u"\u67e5\u770b\u6570\u636e\u96c6", None))
        self.results.setText(QCoreApplication.translate("record", u"\u67e5\u770b\u5b9e\u9a8c\u7ed3\u679c", None))
        self.search_user.setPlaceholderText(QCoreApplication.translate("record", u"\u641c\u7d22", None))
        self.search.setText("")
        self.predict.setText(QCoreApplication.translate("record", u"\u6a21\u578b\u9884\u6d4b", None))
    # retranslateUi

