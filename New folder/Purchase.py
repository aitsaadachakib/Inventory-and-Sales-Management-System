# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Purchase.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_purchase(object):
    def setupUi(self, purchase):
        if not purchase.objectName():
            purchase.setObjectName(u"purchase")
        purchase.resize(783, 511)
        self.gridLayout = QGridLayout(purchase)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mainframe_2 = QFrame(purchase)
        self.mainframe_2.setObjectName(u"mainframe_2")
        self.mainframe_2.setEnabled(True)
        self.mainframe_2.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.mainframe_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableCart = QTableWidget(self.mainframe_2)
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
        self.tableCart.setEnabled(True)
        self.tableCart.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableCart.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCart.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableCart.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCart.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.tableCart, 2, 0, 1, 2, Qt.AlignHCenter)

        self.h_2 = QLabel(self.mainframe_2)
        self.h_2.setObjectName(u"h_2")
        self.h_2.setMinimumSize(QSize(0, 30))
        self.h_2.setMaximumSize(QSize(16777215, 30))
        self.h_2.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.h_2, 0, 0, 1, 2)

        self.frameCartButtons = QFrame(self.mainframe_2)
        self.frameCartButtons.setObjectName(u"frameCartButtons")
        self.frameCartButtons.setMinimumSize(QSize(0, 50))
        self.frameCartButtons.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.frameCartButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonClearAll = QPushButton(self.frameCartButtons)
        self.buttonClearAll.setObjectName(u"buttonClearAll")
        self.buttonClearAll.setMinimumSize(QSize(125, 0))
        self.buttonClearAll.setMaximumSize(QSize(125, 16777215))
        self.buttonClearAll.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.buttonClearAll)

        self.buttonRemove = QPushButton(self.frameCartButtons)
        self.buttonRemove.setObjectName(u"buttonRemove")
        self.buttonRemove.setMinimumSize(QSize(125, 0))
        self.buttonRemove.setMaximumSize(QSize(125, 16777215))
        self.buttonRemove.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.buttonRemove)

        self.buttonPurchase = QPushButton(self.frameCartButtons)
        self.buttonPurchase.setObjectName(u"buttonPurchase")
        self.buttonPurchase.setMinimumSize(QSize(125, 0))
        self.buttonPurchase.setMaximumSize(QSize(125, 16777215))
        self.buttonPurchase.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.buttonPurchase)


        self.gridLayout_4.addWidget(self.frameCartButtons, 3, 1, 1, 1, Qt.AlignRight)

        self.frameCost = QFrame(self.mainframe_2)
        self.frameCost.setObjectName(u"frameCost")
        self.frameCost.setMinimumSize(QSize(0, 30))
        self.frameCost.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.frameCost)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelTotal = QLabel(self.frameCost)
        self.labelTotal.setObjectName(u"labelTotal")
        self.labelTotal.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.labelTotal)

        self.labelCost = QLabel(self.frameCost)
        self.labelCost.setObjectName(u"labelCost")
        self.labelCost.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.labelCost)

        self.labelRs = QLabel(self.frameCost)
        self.labelRs.setObjectName(u"labelRs")
        self.labelRs.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.labelRs)


        self.gridLayout_4.addWidget(self.frameCost, 3, 0, 1, 1, Qt.AlignLeft)


        self.gridLayout.addWidget(self.mainframe_2, 1, 0, 1, 1)

        self.mainframe_1 = QFrame(purchase)
        self.mainframe_1.setObjectName(u"mainframe_1")
        self.mainframe_1.setMinimumSize(QSize(0, 170))
        self.mainframe_1.setMaximumSize(QSize(16777215, 170))
        self.mainframe_1.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.mainframe_1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frameSearchButtons = QFrame(self.mainframe_1)
        self.frameSearchButtons.setObjectName(u"frameSearchButtons")
        self.frameSearchButtons.setMaximumSize(QSize(16777215, 50))
        self.frameSearchButtons.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.frameSearchButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonClear = QPushButton(self.frameSearchButtons)
        self.buttonClear.setObjectName(u"buttonClear")
        self.buttonClear.setMinimumSize(QSize(125, 0))
        self.buttonClear.setMaximumSize(QSize(125, 16777215))
        self.buttonClear.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.buttonClear.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.buttonClear)

        self.buttonAdd = QPushButton(self.frameSearchButtons)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setMinimumSize(QSize(125, 0))
        self.buttonAdd.setMaximumSize(QSize(125, 16777215))
        self.buttonAdd.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout.addWidget(self.buttonAdd)


        self.gridLayout_2.addWidget(self.frameSearchButtons, 19, 3, 1, 2, Qt.AlignRight)

        self.h_1 = QLabel(self.mainframe_1)
        self.h_1.setObjectName(u"h_1")
        self.h_1.setEnabled(True)
        self.h_1.setMinimumSize(QSize(0, 30))
        self.h_1.setMaximumSize(QSize(16777215, 30))
        self.h_1.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.h_1, 0, 0, 1, 5)

        self.fieldpricev = QLineEdit(self.mainframe_1)
        self.fieldpricev.setObjectName(u"fieldpricev")
        self.fieldpricev.setMinimumSize(QSize(125, 25))
        self.fieldpricev.setMaximumSize(QSize(300, 25))

        self.gridLayout_2.addWidget(self.fieldpricev, 19, 0, 1, 1)

        self.labelCode = QLabel(self.mainframe_1)
        self.labelCode.setObjectName(u"labelCode")
        self.labelCode.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelCode, 18, 0, 1, 1)

        self.fieldName = QComboBox(self.mainframe_1)
        self.fieldName.setObjectName(u"fieldName")
        self.fieldName.setMinimumSize(QSize(125, 25))
        self.fieldName.setStyleSheet(u"")
        self.fieldName.setEditable(True)

        self.gridLayout_2.addWidget(self.fieldName, 17, 0, 1, 1)

        self.labelName = QLabel(self.mainframe_1)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setMaximumSize(QSize(16777215, 25))
        self.labelName.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelName, 6, 0, 1, 1)

        self.fieldCategory = QComboBox(self.mainframe_1)
        self.fieldCategory.setObjectName(u"fieldCategory")
        self.fieldCategory.setMinimumSize(QSize(125, 25))
        self.fieldCategory.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.fieldCategory, 17, 1, 1, 1)

        self.labelCategory = QLabel(self.mainframe_1)
        self.labelCategory.setObjectName(u"labelCategory")
        self.labelCategory.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelCategory, 6, 1, 1, 1)

        self.fieldBrand = QComboBox(self.mainframe_1)
        self.fieldBrand.setObjectName(u"fieldBrand")
        self.fieldBrand.setEnabled(True)
        self.fieldBrand.setMinimumSize(QSize(125, 25))
        self.fieldBrand.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.fieldBrand, 17, 2, 1, 1)

        self.labelBrand = QLabel(self.mainframe_1)
        self.labelBrand.setObjectName(u"labelBrand")
        self.labelBrand.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelBrand, 6, 2, 1, 1)

        self.fieldUnits = QSpinBox(self.mainframe_1)
        self.fieldUnits.setObjectName(u"fieldUnits")
        self.fieldUnits.setMinimumSize(QSize(100, 25))
        self.fieldUnits.setMaximumSize(QSize(100, 25))
        self.fieldUnits.setStyleSheet(u"")
        self.fieldUnits.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.gridLayout_2.addWidget(self.fieldUnits, 17, 3, 1, 1)

        self.labelUnits = QLabel(self.mainframe_1)
        self.labelUnits.setObjectName(u"labelUnits")
        self.labelUnits.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelUnits, 6, 3, 1, 1)

        self.label = QLabel(self.mainframe_1)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 6, 4, 1, 1)

        self.filedpriceachat = QLabel(self.mainframe_1)
        self.filedpriceachat.setObjectName(u"filedpriceachat")

        self.gridLayout_2.addWidget(self.filedpriceachat, 17, 4, 1, 1)


        self.gridLayout.addWidget(self.mainframe_1, 0, 0, 1, 1)


        self.retranslateUi(purchase)

        QMetaObject.connectSlotsByName(purchase)
    # setupUi

    def retranslateUi(self, purchase):
        purchase.setWindowTitle(QCoreApplication.translate("purchase", u"Form", None))
        purchase.setProperty(u"type", QCoreApplication.translate("purchase", u"main", None))
        self.mainframe_2.setProperty(u"type", QCoreApplication.translate("purchase", u"mainframe", None))
        ___qtablewidgetitem = self.tableCart.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("purchase", u"n\u00b0", None));
        ___qtablewidgetitem1 = self.tableCart.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("purchase", u"Product Name", None));
        ___qtablewidgetitem2 = self.tableCart.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("purchase", u"Brand", None));
        ___qtablewidgetitem3 = self.tableCart.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("purchase", u"category", None));
        ___qtablewidgetitem4 = self.tableCart.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("purchase", u"Units", None));
        ___qtablewidgetitem5 = self.tableCart.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("purchase", u"Cost/Unit", None));
        ___qtablewidgetitem6 = self.tableCart.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("purchase", u"Cost", None));
        self.h_2.setText(QCoreApplication.translate("purchase", u"Cart", None))
        self.h_2.setProperty(u"type", QCoreApplication.translate("purchase", u"heading", None))
        self.buttonClearAll.setText(QCoreApplication.translate("purchase", u"Clear All", None))
        self.buttonRemove.setText(QCoreApplication.translate("purchase", u"Remove", None))
        self.buttonPurchase.setText(QCoreApplication.translate("purchase", u"Purchase", None))
        self.labelTotal.setText(QCoreApplication.translate("purchase", u"Total Cost :", None))
        self.labelCost.setText(QCoreApplication.translate("purchase", u"0.0", None))
        self.labelRs.setText(QCoreApplication.translate("purchase", u"Rs.", None))
        self.mainframe_1.setProperty(u"type", QCoreApplication.translate("purchase", u"mainframe", None))
        self.buttonClear.setText(QCoreApplication.translate("purchase", u"Clear", None))
        self.buttonAdd.setText(QCoreApplication.translate("purchase", u"Add to cart", None))
        self.h_1.setText(QCoreApplication.translate("purchase", u"Select Product", None))
        self.h_1.setProperty(u"type", QCoreApplication.translate("purchase", u"heading", None))
        self.fieldpricev.setText(QCoreApplication.translate("purchase", u"0", None))
        self.labelCode.setText(QCoreApplication.translate("purchase", u"price vent", None))
        self.labelName.setText(QCoreApplication.translate("purchase", u"Product Name", None))
        self.labelCategory.setText(QCoreApplication.translate("purchase", u"Category", None))
        self.labelBrand.setText(QCoreApplication.translate("purchase", u"Brand", None))
        self.labelUnits.setText(QCoreApplication.translate("purchase", u"Units", None))
        self.label.setText(QCoreApplication.translate("purchase", u"price achat", None))
        self.filedpriceachat.setText(QCoreApplication.translate("purchase", u"0", None))
    # retranslateUi

