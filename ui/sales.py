# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sales.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sales(object):
    def setupUi(self, sales):
        sales.setObjectName("sales")
        sales.resize(847, 565)
        sales.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(sales)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainframe_1 = QtWidgets.QFrame(sales)
        self.mainframe_1.setStyleSheet("")
        self.mainframe_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_1.setObjectName("mainframe_1")
        self.gridLayout = QtWidgets.QGridLayout(self.mainframe_1)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.mainframe_1)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.fieldMonth = QtWidgets.QComboBox(self.groupBox_2)
        self.fieldMonth.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldMonth.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldMonth.setObjectName("fieldMonth")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.verticalLayout_4.addWidget(self.fieldMonth)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Centular")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.fieldYear = QtWidgets.QComboBox(self.groupBox_2)
        self.fieldYear.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldYear.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldYear.setObjectName("fieldYear")
        self.verticalLayout_4.addWidget(self.fieldYear)
        self.frame_6 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTotal_2 = QtWidgets.QLabel(self.frame_6)
        self.labelTotal_2.setObjectName("labelTotal_2")
        self.horizontalLayout_3.addWidget(self.labelTotal_2)
        self.labelMonthlyAmount = QtWidgets.QLabel(self.frame_6)
        self.labelMonthlyAmount.setObjectName("labelMonthlyAmount")
        self.horizontalLayout_3.addWidget(self.labelMonthlyAmount)
        self.labelRs_2 = QtWidgets.QLabel(self.frame_6)
        self.labelRs_2.setObjectName("labelRs_2")
        self.horizontalLayout_3.addWidget(self.labelRs_2)
        self.verticalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft)
        self.buttonCheck = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonCheck.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Centular")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonCheck.setFont(font)
        self.buttonCheck.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonCheck.setObjectName("buttonCheck")
        self.verticalLayout_4.addWidget(self.buttonCheck)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.mainframe_1)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tableSales = QtWidgets.QTableWidget(self.frame_2)
        self.tableSales.setMaximumSize(QtCore.QSize(500, 16777215))
        self.tableSales.setObjectName("tableSales")
        self.tableSales.setColumnCount(4)
        self.tableSales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(3, item)
        self.tableSales.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableSales, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTotal = QtWidgets.QLabel(self.frame_5)
        self.labelTotal.setObjectName("labelTotal")
        self.horizontalLayout_2.addWidget(self.labelTotal)
        self.labeldailyAmount = QtWidgets.QLabel(self.frame_5)
        self.labeldailyAmount.setObjectName("labeldailyAmount")
        self.horizontalLayout_2.addWidget(self.labeldailyAmount)
        self.labelRs = QtWidgets.QLabel(self.frame_5)
        self.labelRs.setObjectName("labelRs")
        self.horizontalLayout_2.addWidget(self.labelRs)
        self.horizontalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 2, 2)
        self.frame = QtWidgets.QFrame(self.mainframe_1)
        self.frame.setMaximumSize(QtCore.QSize(340, 280))
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.calendar = QtWidgets.QCalendarWidget(self.frame)
        self.calendar.setObjectName("calendar")
        self.verticalLayout_2.addWidget(self.calendar)
        self.buttonLoad = QtWidgets.QPushButton(self.frame)
        self.buttonLoad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonLoad.setObjectName("buttonLoad")
        self.verticalLayout_2.addWidget(self.buttonLoad, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.mainframe_1)

        self.retranslateUi(sales)
        QtCore.QMetaObject.connectSlotsByName(sales)

    def retranslateUi(self, sales):
        _translate = QtCore.QCoreApplication.translate
        sales.setWindowTitle(_translate("sales", "Form"))
        sales.setProperty("type", _translate("sales", "main"))
        self.mainframe_1.setProperty("type", _translate("sales", "mainframe"))
        self.groupBox_2.setTitle(_translate("sales", "Monthly sale"))
        self.label_3.setText(_translate("sales", "Month"))
        self.fieldMonth.setItemText(0, _translate("sales", "January"))
        self.fieldMonth.setItemText(1, _translate("sales", "February"))
        self.fieldMonth.setItemText(2, _translate("sales", "March"))
        self.fieldMonth.setItemText(3, _translate("sales", "April"))
        self.fieldMonth.setItemText(4, _translate("sales", "May"))
        self.fieldMonth.setItemText(5, _translate("sales", "June"))
        self.fieldMonth.setItemText(6, _translate("sales", "July"))
        self.fieldMonth.setItemText(7, _translate("sales", "August"))
        self.fieldMonth.setItemText(8, _translate("sales", "September"))
        self.fieldMonth.setItemText(9, _translate("sales", "October"))
        self.fieldMonth.setItemText(10, _translate("sales", "November"))
        self.fieldMonth.setItemText(11, _translate("sales", "December"))
        self.label_4.setText(_translate("sales", "Year"))
        self.labelTotal_2.setText(_translate("sales", "Sale Amount"))
        self.labelMonthlyAmount.setText(_translate("sales", "0.0"))
        self.labelMonthlyAmount.setProperty("type", _translate("sales", "bold"))
        self.labelRs_2.setText(_translate("sales", "Rs."))
        self.buttonCheck.setText(_translate("sales", "Check"))
        self.label.setText(_translate("sales", "Sales"))
        self.label.setProperty("type", _translate("sales", "heading"))
        item = self.tableSales.horizontalHeaderItem(0)
        item.setText(_translate("sales", "Sale Id"))
        item = self.tableSales.horizontalHeaderItem(1)
        item.setText(_translate("sales", "Date"))
        item = self.tableSales.horizontalHeaderItem(2)
        item.setText(_translate("sales", "Time"))
        item = self.tableSales.horizontalHeaderItem(3)
        item.setText(_translate("sales", "Amount"))
        self.labelTotal.setText(_translate("sales", "Total Amount :"))
        self.labeldailyAmount.setText(_translate("sales", "0.0"))
        self.labeldailyAmount.setProperty("type", _translate("sales", "bold"))
        self.labelRs.setText(_translate("sales", "Rs."))
        self.label_5.setText(_translate("sales", "View Sales"))
        self.label_5.setProperty("type", _translate("sales", "heading"))
        self.buttonLoad.setText(_translate("sales", "Load"))
