from SuperMarket.products import Products
from SuperMarket.sales import Sales


from SuperMarket.database import Transaction,TransactionItem



class transactionI:
    def __init__(self, type, qt, price, product,limited):
        self.type = type
        self.qt = qt  # Quantitys
        self.price = price  # Sale price
        self.product = product  # Associated product
        


class Cart():
    def __init__(self):
        super().__init__()

        self.cart = []
        self.total_cost = 0
        

    def newProduct(self,type, qt, price, product,limited):

        self.cart.append(transactionI(type, qt, price, product,limited))

    def getTotalCost(self):
        return self.total_cost

    def isExistingProduct(self, code):
        if code in self.cart.keys():
            return True

    def getCartTable(self):
        data = []
        self.total_cost = 0
        for i in range(len(self.cart)):
            item=self.cart[i]
            details = self.getProductDetails(i,item)
            self.total_cost += details[6]
            data.append(details)
        return data

    def removeProduct(self, code):
        del self.cart[code]

    def makePurchase(self):
        self.purchase(self.cart)
        self.newSale(self.total_cost)

    def clearCart(self):
        self.cart.clear()

    def getProductDetails(self,i, item):
        """
        :type code: str
        """
        details = []
        details.append(str(i))
        details.append(item.product.name)
        if(item.limited):
            details.append("")
            details.append("")
        else:
            details.append(item.product.brand.name)
            details.append(item.product.categorie.name)
        details.append(str(item.qt))
        details.append(str(item.price))
        details.append(str(item.price*item.qt))
        return details
    def makePurchase(self,session,vercement):
        transaction=Transaction(self.total_cost)
        for item in self.cart:

            item
        return
