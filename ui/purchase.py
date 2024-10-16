# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Purchcemodifided.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_purchase(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(1453, 1033)
        Form.setMouseTracking(True)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainfraim = QFrame(Form)
        self.mainfraim.setObjectName(u"mainfraim")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainfraim.sizePolicy().hasHeightForWidth())
        self.mainfraim.setSizePolicy(sizePolicy)
        self.mainfraim.setFrameShape(QFrame.NoFrame)
        self.mainfraim.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.mainfraim)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.mainfraim)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 10))
        self.label.setLineWidth(200)
        self.label.setMidLineWidth(200)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.frame = QFrame(self.mainfraim)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)

        self.pritdeventetext = QLineEdit(self.frame)
        self.pritdeventetext.setObjectName(u"pritdeventetext")
        sizePolicy1.setHeightForWidth(self.pritdeventetext.sizePolicy().hasHeightForWidth())
        self.pritdeventetext.setSizePolicy(sizePolicy1)
        self.pritdeventetext.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.pritdeventetext, 1, 4, 1, 1)

        self.pritdachattext = QLabel(self.frame)
        self.pritdachattext.setObjectName(u"pritdachattext")
        self.pritdachattext.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.pritdachattext, 1, 3, 1, 1)

        self.unitnumber = QSpinBox(self.frame)
        self.unitnumber.setObjectName(u"unitnumber")
        font = QFont()
        font.setKerning(True)
        self.unitnumber.setFont(font)
        self.unitnumber.setFrame(False)
        self.unitnumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.unitnumber.setKeyboardTracking(True)

        self.gridLayout_3.addWidget(self.unitnumber, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 4, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)

        self.productbutton = QPushButton(self.frame)
        self.productbutton.setObjectName(u"productbutton")

        self.gridLayout_3.addWidget(self.productbutton, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 1, 2, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.mainfraim)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(600, -1, -1, -1)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.gridLayout_4.addWidget(self.frame_2, 3, 0, 1, 1)

        self.selctclientframe = QFrame(self.mainfraim)
        self.selctclientframe.setObjectName(u"selctclientframe")
        self.selctclientframe.setMinimumSize(QSize(0, 0))
        self.selctclientframe.setFrameShape(QFrame.StyledPanel)
        self.selctclientframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.selctclientframe)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(300, -1, 300, -1)
        self.clientbutton = QPushButton(self.selctclientframe)
        self.clientbutton.setObjectName(u"clientbutton")
        self.clientbutton.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.clientbutton, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.selctclientframe, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.mainfraim)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(1300, 135))
        self.frame_3.setMaximumSize(QSize(16777215, 135))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frameSold = QFrame(self.frame_3)
        self.frameSold.setObjectName(u"frameSold")
        sizePolicy.setHeightForWidth(self.frameSold.sizePolicy().hasHeightForWidth())
        self.frameSold.setSizePolicy(sizePolicy)
        self.frameSold.setMinimumSize(QSize(637, 40))
        self.frameSold.setMaximumSize(QSize(637, 900))
        self.gridLayout_9 = QGridLayout(self.frameSold)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.labelDZD = QLabel(self.frameSold)
        self.labelDZD.setObjectName(u"labelDZD")
        self.labelDZD.setMinimumSize(QSize(200, 0))
        self.labelDZD.setMaximumSize(QSize(200, 16777215))
        self.labelDZD.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.labelDZD, 0, 2, 1, 1)

        self.labelSold = QLabel(self.frameSold)
        self.labelSold.setObjectName(u"labelSold")
        sizePolicy.setHeightForWidth(self.labelSold.sizePolicy().hasHeightForWidth())
        self.labelSold.setSizePolicy(sizePolicy)
        self.labelSold.setMinimumSize(QSize(350, 0))
        self.labelSold.setMaximumSize(QSize(350, 16777215))
        self.labelSold.setStyleSheet(u"")
        self.labelSold.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.labelSold, 0, 1, 1, 1)

        self.labelTotal1 = QLabel(self.frameSold)
        self.labelTotal1.setObjectName(u"labelTotal1")
        self.labelTotal1.setMinimumSize(QSize(100, 0))
        self.labelTotal1.setMaximumSize(QSize(100, 16777215))
        self.labelTotal1.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.labelTotal1, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frameSold, 2, 0, 1, 1)

        self.frameCartButtons = QFrame(self.frame_3)
        self.frameCartButtons.setObjectName(u"frameCartButtons")
        self.frameCartButtons.setMinimumSize(QSize(0, 50))
        self.frameCartButtons.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_6 = QGridLayout(self.frameCartButtons)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.buttonClearAll = QPushButton(self.frameCartButtons)
        self.buttonClearAll.setObjectName(u"buttonClearAll")
        self.buttonClearAll.setMinimumSize(QSize(125, 30))
        self.buttonClearAll.setMaximumSize(QSize(400, 16777215))
        self.buttonClearAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.buttonClearAll, 0, 0, 1, 1)

        self.buttonRemove = QPushButton(self.frameCartButtons)
        self.buttonRemove.setObjectName(u"buttonRemove")
        self.buttonRemove.setMinimumSize(QSize(125, 30))
        self.buttonRemove.setMaximumSize(QSize(400, 16777215))
        self.buttonRemove.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.buttonRemove, 0, 1, 1, 1)

        self.buttonPurchase = QPushButton(self.frameCartButtons)
        self.buttonPurchase.setObjectName(u"buttonPurchase")
        self.buttonPurchase.setMinimumSize(QSize(125, 30))
        self.buttonPurchase.setMaximumSize(QSize(400, 16777215))
        self.buttonPurchase.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.buttonPurchase, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frameCartButtons, 2, 1, 1, 1)

        self.frameCost = QFrame(self.frame_3)
        self.frameCost.setObjectName(u"frameCost")
        sizePolicy.setHeightForWidth(self.frameCost.sizePolicy().hasHeightForWidth())
        self.frameCost.setSizePolicy(sizePolicy)
        self.frameCost.setMinimumSize(QSize(637, 40))
        self.frameCost.setMaximumSize(QSize(637, 200))
        self.gridLayout_8 = QGridLayout(self.frameCost)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.labelTotal = QLabel(self.frameCost)
        self.labelTotal.setObjectName(u"labelTotal")
        self.labelTotal.setMinimumSize(QSize(100, 0))
        self.labelTotal.setMaximumSize(QSize(100, 16777215))
        self.labelTotal.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.labelTotal, 0, 0, 1, 1)

        self.labelCost = QLabel(self.frameCost)
        self.labelCost.setObjectName(u"labelCost")
        sizePolicy.setHeightForWidth(self.labelCost.sizePolicy().hasHeightForWidth())
        self.labelCost.setSizePolicy(sizePolicy)
        self.labelCost.setMinimumSize(QSize(350, 0))
        self.labelCost.setMaximumSize(QSize(350, 16777215))
        self.labelCost.setStyleSheet(u"")
        self.labelCost.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.labelCost, 0, 1, 1, 1)

        self.labelRs = QLabel(self.frameCost)
        self.labelRs.setObjectName(u"labelRs")
        self.labelRs.setMinimumSize(QSize(200, 0))
        self.labelRs.setMaximumSize(QSize(200, 16777215))
        self.labelRs.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.labelRs, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frameCost, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_7.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.lineEdit.setFont(font2)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.gridLayout_5.addWidget(self.frame_4, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 5, 0, 1, 1)

        self.tableCart = QTableWidget(self.mainfraim)
        if (self.tableCart.columnCount() < 7):
            self.tableCart.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableCart.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableCart.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCart.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCart.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableCart.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableCart.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableCart.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableCart.setObjectName(u"tableCart")
        sizePolicy.setHeightForWidth(self.tableCart.sizePolicy().hasHeightForWidth())
        self.tableCart.setSizePolicy(sizePolicy)
        self.tableCart.setMinimumSize(QSize(0, 500))
        self.tableCart.setLayoutDirection(Qt.LeftToRight)
        self.tableCart.setAutoFillBackground(False)
        self.tableCart.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableCart.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableCart.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCart.setTabKeyNavigation(True)
        self.tableCart.setProperty(u"showDropIndicator", True)
        self.tableCart.setDragDropOverwriteMode(True)
        self.tableCart.setAlternatingRowColors(True)
        self.tableCart.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableCart.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCart.setTextElideMode(Qt.ElideMiddle)
        self.tableCart.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableCart.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableCart.setShowGrid(True)
        self.tableCart.setGridStyle(Qt.SolidLine)
        self.tableCart.setSortingEnabled(True)
        self.tableCart.horizontalHeader().setCascadingSectionResizes(False)
        self.tableCart.horizontalHeader().setDefaultSectionSize(150)
        self.tableCart.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableCart, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.mainfraim, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Bon d'achat ou de vente", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"unit", None))
        self.pritdeventetext.setText(QCoreApplication.translate("Form", u"0", None))
        self.pritdachattext.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"prit", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"select prodact:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"type", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"prit d'achat", None))
        self.productbutton.setText(QCoreApplication.translate("Form", u"select", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Add", None))
        self.clientbutton.setText(QCoreApplication.translate("Form", u"selectionner le client", None))
        self.labelDZD.setText("")
        self.labelSold.setText(QCoreApplication.translate("Form", u"  0 DZD", None))
        self.labelTotal1.setText(QCoreApplication.translate("Form", u"encien sold:", None))
        self.buttonClearAll.setText(QCoreApplication.translate("Form", u"Clear All", None))
        self.buttonRemove.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.buttonPurchase.setText(QCoreApplication.translate("Form", u"acheter", None))
        self.labelTotal.setText(QCoreApplication.translate("Form", u"Total Cost :", None))
        self.labelCost.setText(QCoreApplication.translate("Form", u"0 DZD", None))
        self.labelRs.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Vercement:", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        ___qtablewidgetitem = self.tableCart.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"n\u00b0", None));
        ___qtablewidgetitem1 = self.tableCart.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nom du produit", None));
        ___qtablewidgetitem2 = self.tableCart.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Brand", None));
        ___qtablewidgetitem3 = self.tableCart.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Category", None));
        ___qtablewidgetitem4 = self.tableCart.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Units", None));
        ___qtablewidgetitem5 = self.tableCart.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Unit/Cost", None));
        ___qtablewidgetitem6 = self.tableCart.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Cost", None));
    # retranslateUi

