from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem

from widgets.ClientselectionWidget import ClientselectionMainwigget
from SuperMarket.database import Customer,CustomerType

from SuperMarket import Cart
from ui.Purchase import Ui_purchase
from widgets.UIFunctions import showMessage, askQuestion


class PurchaseWidget(QWidget, Ui_purchase):
    def __init__(self,session,mainwiget, *args, **kwargs):
        self.session=session
        self.mainwiget=mainwiget
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.producket=None
        self.limited=False

        self.crt = Cart()

        self.comboBox.addItem('vent')
        self.comboBox.addItem('achat')
        self.unitnumber.setValue(1)


        # event updates
        self.pushButton_3.clicked.connect(lambda: self.clear())
        self.pushButton_2.clicked.connect(lambda: self.AddToCart())
        self.buttonRemove.clicked.connect(lambda: self.removeProduct())
        self.buttonClearAll.clicked.connect(lambda: self.clearCart())
        self.buttonPurchase.clicked.connect(lambda: self.purchase())
        self.clientbutton.clicked.connect(lambda: self.clientmenushow())
        self.productbutton.clicked.connect(lambda: self.productmenushow())
        # setup tables
        header = self.tableCart.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.setupCartTable()

    def clear(self):
        """method to clears and resets all input fields"""
        self.productbutton.setText("select")
        self.unitnumber.setValue(1)
        self.comboBox.setCurrentIndex(0)
        self.pritdachattext.setText("0")
        self.pritdeventetext.setText("0")
        self.labelSold.setText("0 DZD")
        self.producket=None


    def AddToCart(self):
        """method to add items to the cart"""
        units = self.unitnumber.text()
        produket=self.producket
        type=self.comboBox.currentText()
        price=self.pritdeventetext.text()
        if produket is None:
            showMessage(self, 'Input Error', 'Please select a product')
            return
        if units == '0':
            showMessage(self, 'Input Error', 'Please set the units required')
            return
        if self.crt.isExistingProduct(produket):
            showMessage(self, 'Input Error', 'Product already Exist in cart!')
            return
        if produket.qt < int(units) and type != "achat":
            showMessage(self, 'Input Error', units + ' units of product is not available!')
            return
        if price == "0":
            showMessage(self, 'Input Error', 'Please add the price')
            return
        
        
        units = int(units)
        price=int(price)
        self.crt.newProduct(type, units, price, produket, self.limited)
        self.clear()
        self.setupCartTable()
        self.updateTotalCost()

    def updateProductField(self):
        """method to update the items of the fieldname and fieldCode based on the update in fieldBrand fieldCategory"""
        self.fieldCode.clear()
        self.fieldName.clear()
        self.fieldName.addItem('select')
        brand = None
        category = None
        if self.fieldBrand.currentIndex() != 0:
            brand = self.fieldBrand.currentText()
        if self.fieldCategory.currentIndex() != 0:
            category = self.fieldCategory.currentText()
        self.fieldName.addItems(self.crt.getProductsData(name=True, filterBrand=brand, filterCategory=category))

    def productCodeChange(self):
        """method to update all other fields when fieldCode is changed by user"""
        code = self.fieldCode.text()
        if code != '':
            details = self.crt.getProductDetails(code)
            if details is not None:
                name = details[1]
                brand = details[2]
                category = details[3]
                self.fieldBrand.setCurrentText(brand)
                self.fieldCategory.setCurrentText(category)
                self.fieldName.clear()
                self.fieldName.addItem('select')
                self.fieldName.addItems(self.crt.getProductsData(name=True, filterBrand=brand, filterCategory=category))
                self.fieldName.setCurrentText(name)
            else:
                self.fieldCode.clear()
                showMessage(self, 'Input Error', 'No product found with product code ' + code)

    def productNameChange(self):
        """method to update all other fields when fieldName is changed by user"""
        if self.fieldName.currentText() == 'select':
            self.clear()
            return
        code = self.crt.getProductId(self.fieldName.currentText())
        details = self.crt.getProductDetails(code)
        name = details[1]
        brand = details[2]
        category = details[3]
        self.fieldBrand.setCurrentText(brand)
        self.fieldCategory.setCurrentText(category)
        self.fieldCode.setText(code)
        self.fieldName.clear()
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.crt.getProductsData(name=True, filterBrand=brand, filterCategory=category))
        self.fieldName.setCurrentText(name)

    def setupCartTable(self):
        data = self.crt.getCartTable()
        self.tableCart.setRowCount(0)
        for i, row in enumerate(data):
            self.tableCart.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableCart.setItem(i, j, newItem)

    def updateTotalCost(self):
        total = self.crt.getTotalCost()
        self.labelCost.setText(str(total))

    def clearCart(self):
        self.crt.clearCart()
        self.setupCartTable()

    def removeProduct(self):
        if not self.tableCart.selectedItems():
            showMessage(self, 'Error', 'Please select an item from cart!')
        else:
            p_id = int(self.tableCart.selectedItems()[0].text())
            self.crt.removeProduct(p_id)
            self.setupCartTable()

    def purchase(self):
        if self.tableCart.rowCount() == 0:
            showMessage(self, 'Error', 'No item in cart')
            return
        x = askQuestion(self, 'Purchase Warning', 'Confirm Purchase?')
        if x:
            self.crt.makePurchase(self.session)
            self.clearCart()
    
    def clientmenushow(self):
        print('hearee')
        self.mainwiget.hide()
        self.clientwiget=ClientselectionMainwigget(session=self.session,purchsewigget=self,mainwiget=self.mainwiget)
        self.clientwiget.showMaximized()

    def productmenushow(self):
        x=0
