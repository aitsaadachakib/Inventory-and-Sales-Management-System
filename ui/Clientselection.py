# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientselection.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Clientselection(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1237, 1042)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(500, 0))
        self.frame_2.setMaximumSize(QSize(750, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.nameinput = QLineEdit(self.frame_2)
        self.nameinput.setObjectName(u"nameinput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nameinput.sizePolicy().hasHeightForWidth())
        self.nameinput.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.nameinput, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)

        self.typecombo = QComboBox(self.frame_2)
        self.typecombo.setObjectName(u"typecombo")

        self.gridLayout_4.addWidget(self.typecombo, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)

        self.clienttable = QTableWidget(self.frame)
        if (self.clienttable.columnCount() < 4):
            self.clienttable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.clienttable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.clienttable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.clienttable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.clienttable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.clienttable.setObjectName(u"clienttable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.clienttable.sizePolicy().hasHeightForWidth())
        self.clienttable.setSizePolicy(sizePolicy3)
        self.clienttable.setMinimumSize(QSize(650, 0))
        self.clienttable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.clienttable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.clienttable.setTextElideMode(Qt.ElideMiddle)
        self.clienttable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.clienttable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.clienttable.horizontalHeader().setDefaultSectionSize(150)
        self.clienttable.verticalHeader().setProperty(u"showSortIndicator", False)

        self.gridLayout_2.addWidget(self.clienttable, 2, 0, 1, 2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.selectbutto = QPushButton(self.frame_3)
        self.selectbutto.setObjectName(u"selectbutto")
        self.selectbutto.setMinimumSize(QSize(0, 30))
        self.selectbutto.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.selectbutto, 0, 2, 1, 1)

        self.selectbutton = QPushButton(self.frame_3)
        self.selectbutton.setObjectName(u"selectbutton")
        self.selectbutton.setMinimumSize(QSize(0, 30))
        self.selectbutton.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.selectbutton, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Client:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"name:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"type:", None))
        ___qtablewidgetitem = self.clienttable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.clienttable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"name", None));
        ___qtablewidgetitem2 = self.clienttable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"type", None));
        ___qtablewidgetitem3 = self.clienttable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"sold", None));
        self.selectbutto.setText(QCoreApplication.translate("Form", u"select", None))
        self.selectbutton.setText(QCoreApplication.translate("Form", u"modify", None))
    # retranslateUi

