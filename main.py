"""
This is the runner file of the application
Mainwindow is created and other widgets are added in this file
"""
import sys

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QStackedWidget, QWidget, QMessageBox, QTableWidgetItem, \
    QHeaderView

from superMarket import Cart, Inventory
from ui.products import Ui_products
from ui.purchase import Ui_purchase
from ui.stock import Ui_stock


class UIProducts(Ui_products):
    def __init__(self, widget, inv):
        self.widget = widget
        self.inv = inv
        self.setupUi(widget)
        self.fieldPrize.setValidator(QDoubleValidator(0, 10000, 2))
        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.inv.getAllBrandNames())
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.inv.getAllCategoryNames())
        # event updates
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonAddProduct.clicked.connect(lambda: self.addProduct())
        self.buttonAddBrand.clicked.connect(lambda: self.addBrand())
        self.buttonAddCategory.clicked.connect(lambda: self.addCategory())

        # setup tables
        header = self.tableBrands.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.setBrandTableData()

        header = self.tableCategories.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.setCategoryTableData()

        header = self.tableProducts.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.setProductsTableData()

    def setBrandTableData(self):
        self.tableBrands.setRowCount(0)
        data = self.inv.getAllBrandsData()
        for i, row in enumerate(data):
            self.tableBrands.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableBrands.setItem(i, j, newItem)

    def setCategoryTableData(self):
        self.tableCategories.setRowCount(0)
        data = self.inv.getAllCategoryData()
        for i, row in enumerate(data):
            self.tableCategories.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableCategories.setItem(i, j, newItem)

    def setProductsTableData(self):
        self.tableProducts.setRowCount(0)
        data = self.inv.getIdNameProductsData()
        for i, row in enumerate(data):
            self.tableProducts.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableProducts.setItem(i, j, newItem)

    def clear(self):
        self.fieldPrize.clear()
        self.fieldStock.setValue(0)
        self.fieldName.clear()

        self.fieldCategory.clear()
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.inv.getAllCategoryNames())

        self.fieldBrand.clear()
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.inv.getAllBrandNames())

    def addProduct(self):
        name = self.fieldName.text()
        brand = self.fieldBrand.currentText()
        category = self.fieldCategory.currentText()
        stock = self.fieldStock.text()
        prize = self.fieldPrize.text()
        # some validations for the inputs
        if name == '' or len(name) <= 5:
            self.showMessage('Input Error', 'Please enter valid name')
            return
        if name in self.inv.getAllProductNames():
            self.showMessage('Input Error', 'Product already exists!')
            return
        if brand == 'select':
            self.showMessage('Input Error', 'Please select a brand')
            return
        if category == 'select':
            self.showMessage('Input Error', 'Please select a category')
            return
        if prize == '' or prize == 0:
            self.showMessage('Input Error', 'Please enter valid prize')
            return
        if stock == '':
            self.showMessage('Input Error', 'Please enter valid stock')
            return

        stock = int(stock)
        prize = float(prize)
        category = self.inv.getCategoryId(category)
        brand = self.inv.getBrandId(brand)
        self.inv.addProduct(name, brand, category, stock, prize)
        self.showMessage('Product added', name + ' added to products successfully')
        self.setProductsTableData()
        self.clear()

    def addBrand(self):
        brand = self.fieldNewBrand.text()
        # some validations for the input
        if brand == '':
            self.showMessage('Input Error', 'Please enter valid brand name')
            return
        if brand in self.inv.getAllBrandNames():
            self.showMessage('Input Error', 'Brand already exists!')
            return
        self.inv.addBrand(brand)
        self.showMessage('Brand added', brand + ' added to brands successfully')
        self.fieldNewBrand.clear()
        self.setBrandTableData()
        self.clear()

    def addCategory(self):
        category = self.fieldNewCategory.text()
        # some validations for the input
        if category == '':
            self.showMessage('Input Error', 'Please enter valid category name')
            return
        if category in self.inv.getAllCategoryNames():
            self.showMessage('Input Error', 'Category already exists!')
            return
        self.inv.addCategory(category)
        self.showMessage('Category added', category + ' added to categories successfully')
        self.fieldNewCategory.clear()
        self.setCategoryTableData()
        self.clear()

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.about(self.widget, title, message)


class UIPurchase(Ui_purchase):
    def __init__(self, widget, crt, inv):
        self.widget = widget
        self.crt = crt
        self.inv = inv
        self.setupUi(widget)
        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.inv.getAllBrandNames())
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.inv.getAllCategoryNames())
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.inv.getAllProductNames())
        # event updates
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonAdd.clicked.connect(lambda: self.AddToCart())
        self.fieldCategory.activated.connect(lambda: self.updateProductField())
        self.fieldBrand.activated.connect(lambda: self.updateProductField())
        self.fieldCode.returnPressed.connect(lambda: self.productCodeChange())
        self.fieldName.activated.connect(lambda: self.productNameChange())

    def clear(self):
        """method to clears and resets all input fields"""
        self.fieldCode.clear()
        self.fieldUnits.setValue(0)

        self.fieldBrand.clear()
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.inv.getAllBrandNames())

        self.fieldCategory.clear()
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.inv.getAllCategoryNames())

        self.fieldName.clear()
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.inv.getAllProductNames())

    def AddToCart(self):
        """method to add items to the cart"""
        units = self.fieldUnits.text()
        productCode = self.fieldCode.text()
        if productCode == '' or productCode == '0':
            self.showMessage('Input Error', 'Please select a product')
            return
        if units == '0':
            self.showMessage('Input Error', 'Please set the units required')
            return
        units = int(units)
        productCode = int(productCode)
        self.crt.newProduct(productCode, units)

    def updateProductField(self):
        """method to update the items of the fieldname and fieldCode based on the update in fieldBrand fieldCategory"""
        self.fieldCode.clear()
        self.fieldName.clear()
        self.fieldName.addItem('select')
        if self.fieldBrand.currentText() == 'select' and self.fieldCategory.currentText() == 'select':
            self.fieldName.addItems(self.inv.getAllProductNames())
        elif self.fieldBrand.currentText() == 'select':
            self.fieldName.addItems(self.inv.getAllProductNames(brand=None, category=self.fieldCategory.currentText()))
        elif self.fieldCategory.currentText() == 'select':
            self.fieldName.addItems(self.inv.getAllProductNames(brand=self.fieldBrand.currentText(), category=None))
        else:
            self.fieldName.addItems(self.inv.getAllProductNames(brand=self.fieldBrand.currentText(),
                                                                category=self.fieldCategory.currentText()))

    def productCodeChange(self):
        """method to update all other fields when fieldCode is changed by user"""
        code = self.fieldCode.text()
        if code != '':
            details = self.inv.getProductDetails(code)
            if details is not None:
                name = details[1]
                brand = details[2]
                category = details[3]
                self.fieldBrand.setCurrentText(brand)
                self.fieldCategory.setCurrentText(category)
                self.fieldName.clear()
                self.fieldName.addItem('select')
                self.fieldName.addItems(self.inv.getAllProductNames(brand, category))
                self.fieldName.setCurrentText(name)
            else:
                self.fieldCode.clear()
                self.showMessage('Input Error', 'No product found with product code ' + code)

    def productNameChange(self):
        """method to update all other fields when fieldName is changed by user"""
        if self.fieldName.currentText() == 'select':
            self.clear()
            return
        code = self.inv.getProductId(self.fieldName.currentText())
        details = self.inv.getProductDetails(code)
        name = details[1]
        brand = details[2]
        category = details[3]
        self.fieldBrand.setCurrentText(brand)
        self.fieldCategory.setCurrentText(category)
        self.fieldCode.setText(code)
        self.fieldName.clear()
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.inv.getAllProductNames(brand, category))
        self.fieldName.setCurrentText(name)

    def showMessage(self, title, message):
        """method to show any message to the user with a title and description"""
        msg = QMessageBox()
        msg.about(self.widget, title, message)


class UIStock(Ui_stock):
    def __init__(self, widget, inv):
        self.widget = widget
        self.inv = inv
        self.setupUi(widget)


class UISuperMarket(QMainWindow):
    def __init__(self):
        super().__init__()
        # setup the mainwindow
        self.resize(800, 600)
        self.setWindowTitle('MASS Supermarket')
        self.setWindowIcon(QIcon('res/images/icon.png'))
        self.centralwidget = QStackedWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setContentsMargins(0, 20, 0, 0)

        self.crt = Cart()
        self.inv = Inventory()

        # setup contents of stacked widget
        self.purchaseWidget = QWidget()
        UIPurchase(self.purchaseWidget, self.crt, self.inv)
        self.centralwidget.addWidget(self.purchaseWidget)
        self.addWidget = QWidget()
        UIProducts(self.addWidget, self.inv)
        self.centralwidget.addWidget(self.addWidget)
        self.stockWidget = QWidget()
        UIStock(self.stockWidget, self.inv)
        self.centralwidget.addWidget(self.stockWidget)

        # set the widget that should be shown at first
        self.setWidget(self.purchaseWidget)
        self.setupMenuBar()
        self.show()

    def setWidget(self, widget):
        """method to set the active widget in the stacked widget"""
        self.centralwidget.setCurrentWidget(widget)

    def setupMenuBar(self):
        """method to setup the menubar"""
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 5000, 20))
        purchase = menubar.addAction('Purchase')
        products = menubar.addAction('Products')
        viewStock = menubar.addAction('Stock')
        updateStock = menubar.addAction('Update Stock')

        purchase.triggered.connect(lambda: self.setWidget(self.purchaseWidget))
        products.triggered.connect(lambda: self.setWidget(self.addWidget))
        viewStock.triggered.connect(lambda: self.setWidget(self.stockWidget))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UISuperMarket()
    sys.exit(app.exec_())
