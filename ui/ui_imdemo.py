# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imdemo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(989, 861)
        self.horizontalLayout_10 = QHBoxLayout(Form)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(17, 117, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(100, 44))

        self.verticalLayout.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.frame)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(100, 44))

        self.verticalLayout.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.frame)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(100, 44))

        self.verticalLayout.addWidget(self.toolButton_3)

        self.toolButton_4 = QToolButton(self.frame)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(100, 44))

        self.verticalLayout.addWidget(self.toolButton_4)

        self.verticalSpacer = QSpacerItem(17, 494, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_10.addWidget(self.frame)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.toolButton_17 = QToolButton(self.frame_4)
        self.toolButton_17.setObjectName(u"toolButton_17")
        self.toolButton_17.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_12.addWidget(self.toolButton_17)

        self.toolButton_18 = QToolButton(self.frame_4)
        self.toolButton_18.setObjectName(u"toolButton_18")
        self.toolButton_18.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_12.addWidget(self.toolButton_18)

        self.toolButton_19 = QToolButton(self.frame_4)
        self.toolButton_19.setObjectName(u"toolButton_19")
        self.toolButton_19.setMinimumSize(QSize(60, 30))

        self.horizontalLayout_12.addWidget(self.toolButton_19)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_12)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_5 = QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.page_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_11.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_11.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_11.addWidget(self.pushButton_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget_11 = QTableWidget(self.frame_3)
        if (self.tableWidget_11.columnCount() < 6):
            self.tableWidget_11.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_11.setObjectName(u"tableWidget_11")

        self.horizontalLayout_8.addWidget(self.tableWidget_11)

        self.tableWidget_12 = QTableWidget(self.frame_3)
        self.tableWidget_12.setObjectName(u"tableWidget_12")

        self.horizontalLayout_8.addWidget(self.tableWidget_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_9 = QHBoxLayout(self.page_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_2 = QFrame(self.page_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_13.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_13.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_13.addWidget(self.pushButton_12)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tableWidget_13 = QTableWidget(self.frame_2)
        if (self.tableWidget_13.columnCount() < 6):
            self.tableWidget_13.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget_13.setObjectName(u"tableWidget_13")

        self.horizontalLayout_15.addWidget(self.tableWidget_13)

        self.tableWidget_14 = QTableWidget(self.frame_2)
        self.tableWidget_14.setObjectName(u"tableWidget_14")

        self.horizontalLayout_15.addWidget(self.tableWidget_14)


        self.verticalLayout_3.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_9.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"\u5546\u54c1", None))
        self.toolButton_2.setText(QCoreApplication.translate("Form", u"\u9500\u552e", None))
        self.toolButton_3.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237", None))
        self.toolButton_4.setText(QCoreApplication.translate("Form", u"\u4f9b\u5e94\u5546", None))
        self.toolButton_17.setText(QCoreApplication.translate("Form", u"\u6240\u6709\u5546\u54c1", None))
        self.toolButton_18.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u7ba1\u7406", None))
        self.toolButton_19.setText(QCoreApplication.translate("Form", u"\ud83d\udd3a\u9884\u8b66", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"+\u65b0\u5efa\u5546\u54c1", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"+\u5165\u5e93", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"-\u51fa\u5e93", None))
        ___qtablewidgetitem = self.tableWidget_11.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u5546\u54c1ID", None));
        ___qtablewidgetitem1 = self.tableWidget_11.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget_11.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u6570\u91cf", None));
        ___qtablewidgetitem3 = self.tableWidget_11.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u4ef7\u503c", None));
        ___qtablewidgetitem4 = self.tableWidget_11.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u5df2\u552e\u6570\u91cf", None));
        ___qtablewidgetitem5 = self.tableWidget_11.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u5df2\u552e\u91d1\u989d", None));
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"PushButton", None))
        ___qtablewidgetitem6 = self.tableWidget_13.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"\u5546\u54c1ID", None));
        ___qtablewidgetitem7 = self.tableWidget_13.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        ___qtablewidgetitem8 = self.tableWidget_13.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u6570\u91cf", None));
        ___qtablewidgetitem9 = self.tableWidget_13.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u4ef7\u503c", None));
        ___qtablewidgetitem10 = self.tableWidget_13.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"\u5df2\u552e\u6570\u91cf", None));
        ___qtablewidgetitem11 = self.tableWidget_13.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"\u5df2\u552e\u91d1\u989d", None));
    # retranslateUi

