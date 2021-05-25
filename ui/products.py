# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'products.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_products(object):
    def setupUi(self, products):
        products.setObjectName("products")
        products.resize(717, 419)
        products.setStyleSheet("QWidget#products{\n"
"    background-color:rgb(0, 124, 124);\n"
"}\n"
"QLabel{\n"
"    font: 15px  \"Centular\";\n"
"}\n"
"QPushButton{\n"
"    font: 15px  \"Centular\";\n"
"    background-color:rgb(0, 124, 124);\n"
"}\n"
"\n"
"QLabel#h_1 ,QLabel#h_2, QLabel#h_3{\n"
"    font: bold 16px  \"Centular\";\n"
"}\n"
"\n"
"QFrame#mainframe_1, QFrame#mainframe_2,  QFrame#mainframe_3{\n"
"    background-color:rgb(51, 152, 152);\n"
"    border-radius:6px;\n"
"}\n"
"\n"
"QComboBox,QSpinBox,QLineEdit{\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:#000;\n"
"    border-radius:3px;\n"
"}\n"
"QMessageBox{\n"
"    background-color: rgb(51, 152, 152);\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"    gridline-color: #ffffff;\n"
"    background-color: transparent;\n"
"    border:1px solid rgb(255, 255, 255);\n"
"    font: 13px  \"Centular\";\n"
"}\n"
"QHeaderView {\n"
"    background-color: transparent;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(0, 124, 124);\n"
"    font: bold 13px  \"Centular\" ;\n"
"    border-bottom: 1px solid #fff;\n"
"    border-right: 1px solid #fff;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fff;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fff;\n"
"}\n"
"QTableWidget::item::selected \n"
"{\n"
" Color:#000; \n"
" Background: #fff;\n"
"}\n"
"QGroupBox {\n"
"     border: 1px solid #fff;\n"
"     border-radius: 5px;\n"
"     margin-top:12px; \n"
"font: bold 12px  \"Centular\";\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     \n"
"    font: 8pt \"MS Sans Serif\";\n"
" }")
        self.gridLayout = QtWidgets.QGridLayout(products)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.mainframe_2 = QtWidgets.QFrame(products)
        self.mainframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_2.setObjectName("mainframe_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.mainframe_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.mainframe_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.fieldNewBrand = QtWidgets.QLineEdit(self.groupBox_5)
        self.fieldNewBrand.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldNewBrand.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldNewBrand.setObjectName("fieldNewBrand")
        self.gridLayout_6.addWidget(self.fieldNewBrand, 1, 0, 1, 1)
        self.buttonAddBrand = QtWidgets.QPushButton(self.groupBox_5)
        self.buttonAddBrand.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonAddBrand.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonAddBrand.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonAddBrand.setObjectName("buttonAddBrand")
        self.gridLayout_6.addWidget(self.buttonAddBrand, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 1, 1, 1, QtCore.Qt.AlignTop)
        self.tableBrands = QtWidgets.QTableWidget(self.mainframe_2)
        self.tableBrands.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableBrands.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableBrands.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableBrands.setObjectName("tableBrands")
        self.tableBrands.setColumnCount(2)
        self.tableBrands.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableBrands.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBrands.setHorizontalHeaderItem(1, item)
        self.tableBrands.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tableBrands, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalFrame = QtWidgets.QFrame(self.mainframe_2)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonDeleteBrand = QtWidgets.QPushButton(self.horizontalFrame)
        self.buttonDeleteBrand.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonDeleteBrand.setObjectName("buttonDeleteBrand")
        self.horizontalLayout.addWidget(self.buttonDeleteBrand)
        self.buttonUpdateBrand = QtWidgets.QPushButton(self.horizontalFrame)
        self.buttonUpdateBrand.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonUpdateBrand.setObjectName("buttonUpdateBrand")
        self.horizontalLayout.addWidget(self.buttonUpdateBrand)
        self.gridLayout_5.addWidget(self.horizontalFrame, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.mainframe_2, 1, 0, 1, 1)
        self.mainframe_3 = QtWidgets.QFrame(products)
        self.mainframe_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_3.setObjectName("mainframe_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.mainframe_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.mainframe_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.fieldNewCategory = QtWidgets.QLineEdit(self.groupBox_6)
        self.fieldNewCategory.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldNewCategory.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldNewCategory.setObjectName("fieldNewCategory")
        self.gridLayout_8.addWidget(self.fieldNewCategory, 1, 0, 1, 1)
        self.buttonAddCategory = QtWidgets.QPushButton(self.groupBox_6)
        self.buttonAddCategory.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonAddCategory.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonAddCategory.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonAddCategory.setObjectName("buttonAddCategory")
        self.gridLayout_8.addWidget(self.buttonAddCategory, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_7.addWidget(self.groupBox_6, 0, 1, 1, 1, QtCore.Qt.AlignTop)
        self.tableCategories = QtWidgets.QTableWidget(self.mainframe_3)
        self.tableCategories.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableCategories.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableCategories.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableCategories.setObjectName("tableCategories")
        self.tableCategories.setColumnCount(2)
        self.tableCategories.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableCategories.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCategories.setHorizontalHeaderItem(1, item)
        self.tableCategories.verticalHeader().setVisible(False)
        self.gridLayout_7.addWidget(self.tableCategories, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalFrame1 = QtWidgets.QFrame(self.mainframe_3)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonDeleteCategory = QtWidgets.QPushButton(self.horizontalFrame1)
        self.buttonDeleteCategory.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonDeleteCategory.setObjectName("buttonDeleteCategory")
        self.horizontalLayout_2.addWidget(self.buttonDeleteCategory)
        self.buttonUpdateCategory = QtWidgets.QPushButton(self.horizontalFrame1)
        self.buttonUpdateCategory.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonUpdateCategory.setObjectName("buttonUpdateCategory")
        self.horizontalLayout_2.addWidget(self.buttonUpdateCategory)
        self.gridLayout_7.addWidget(self.horizontalFrame1, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.mainframe_3, 1, 1, 1, 1)
        self.mainframe_1 = QtWidgets.QFrame(products)
        self.mainframe_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_1.setObjectName("mainframe_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainframe_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.mainframe_1)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.fieldName = QtWidgets.QLineEdit(self.groupBox_4)
        self.fieldName.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldName.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldName.setObjectName("fieldName")
        self.gridLayout_3.addWidget(self.fieldName, 1, 0, 1, 1)
        self.fieldStock = QtWidgets.QSpinBox(self.groupBox_4)
        self.fieldStock.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldStock.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldStock.setObjectName("fieldStock")
        self.gridLayout_3.addWidget(self.fieldStock, 1, 1, 1, 1)
        self.fieldCategory = QtWidgets.QComboBox(self.groupBox_4)
        self.fieldCategory.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldCategory.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldCategory.setObjectName("fieldCategory")
        self.gridLayout_3.addWidget(self.fieldCategory, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.fieldBrand = QtWidgets.QComboBox(self.groupBox_4)
        self.fieldBrand.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldBrand.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldBrand.setObjectName("fieldBrand")
        self.gridLayout_3.addWidget(self.fieldBrand, 3, 0, 1, 1)
        self.fieldPrize = QtWidgets.QLineEdit(self.groupBox_4)
        self.fieldPrize.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldPrize.setMaximumSize(QtCore.QSize(300, 25))
        self.fieldPrize.setObjectName("fieldPrize")
        self.gridLayout_3.addWidget(self.fieldPrize, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttonAddProduct = QtWidgets.QPushButton(self.frame_7)
        self.buttonAddProduct.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonAddProduct.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonAddProduct.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonAddProduct.setObjectName("buttonAddProduct")
        self.gridLayout_4.addWidget(self.buttonAddProduct, 0, 0, 1, 1)
        self.buttonClear = QtWidgets.QPushButton(self.frame_7)
        self.buttonClear.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonClear.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonClear.setObjectName("buttonClear")
        self.gridLayout_4.addWidget(self.buttonClear, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_7, 0, 2, 6, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 2, 4, 1, 1)
        self.tableProducts = QtWidgets.QTableWidget(self.mainframe_1)
        self.tableProducts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableProducts.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableProducts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableProducts.setWordWrap(False)
        self.tableProducts.setObjectName("tableProducts")
        self.tableProducts.setColumnCount(2)
        self.tableProducts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(1, item)
        self.tableProducts.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableProducts, 2, 0, 1, 1)
        self.horizontalFrame2 = QtWidgets.QFrame(self.mainframe_1)
        self.horizontalFrame2.setObjectName("horizontalFrame2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttoDeleteProduct = QtWidgets.QPushButton(self.horizontalFrame2)
        self.buttoDeleteProduct.setMinimumSize(QtCore.QSize(125, 0))
        self.buttoDeleteProduct.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttoDeleteProduct.setObjectName("buttoDeleteProduct")
        self.horizontalLayout_4.addWidget(self.buttoDeleteProduct)
        self.buttonUpdateProduct = QtWidgets.QPushButton(self.horizontalFrame2)
        self.buttonUpdateProduct.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonUpdateProduct.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonUpdateProduct.setObjectName("buttonUpdateProduct")
        self.horizontalLayout_4.addWidget(self.buttonUpdateProduct)
        self.gridLayout_2.addWidget(self.horizontalFrame2, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout.addWidget(self.mainframe_1, 0, 0, 1, 2)

        self.retranslateUi(products)
        QtCore.QMetaObject.connectSlotsByName(products)

    def retranslateUi(self, products):
        _translate = QtCore.QCoreApplication.translate
        products.setWindowTitle(_translate("products", "Form"))
        self.groupBox_5.setTitle(_translate("products", "Add New Brand"))
        self.label.setText(_translate("products", "Brand Name"))
        self.buttonAddBrand.setText(_translate("products", "Add"))
        item = self.tableBrands.horizontalHeaderItem(0)
        item.setText(_translate("products", "Brand Id"))
        item = self.tableBrands.horizontalHeaderItem(1)
        item.setText(_translate("products", "Brand Name"))
        self.buttonDeleteBrand.setText(_translate("products", "Delete"))
        self.buttonUpdateBrand.setText(_translate("products", "Update"))
        self.groupBox_6.setTitle(_translate("products", "Add New Category"))
        self.label_7.setText(_translate("products", "Category Name"))
        self.buttonAddCategory.setText(_translate("products", "Add"))
        item = self.tableCategories.horizontalHeaderItem(0)
        item.setText(_translate("products", "New Column"))
        item = self.tableCategories.horizontalHeaderItem(1)
        item.setText(_translate("products", "Category Name"))
        self.buttonDeleteCategory.setText(_translate("products", "Delete"))
        self.buttonUpdateCategory.setText(_translate("products", "Update"))
        self.groupBox_4.setTitle(_translate("products", "Add New Product"))
        self.label_5.setText(_translate("products", "Current Stock"))
        self.label_2.setText(_translate("products", "Product Name"))
        self.label_3.setText(_translate("products", "Brand"))
        self.label_4.setText(_translate("products", "Category"))
        self.label_6.setText(_translate("products", "Prize/Unit"))
        self.buttonAddProduct.setText(_translate("products", "Add"))
        self.buttonClear.setText(_translate("products", "Clear"))
        item = self.tableProducts.horizontalHeaderItem(0)
        item.setText(_translate("products", "Product Id"))
        item = self.tableProducts.horizontalHeaderItem(1)
        item.setText(_translate("products", "Product Name"))
        self.buttoDeleteProduct.setText(_translate("products", "Delete"))
        self.buttonUpdateProduct.setText(_translate("products", "Update"))
