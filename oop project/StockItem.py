class StockItem(object):
    stock_category="car accessories"
    def __init__(self,code,quantity,price):
        self.__code=code
        self.__quantity=quantity
        self.__price=price
    
    def getStockName(self):
        return 'Unknown Stock Name'
    def getStockDescription(args):
        return 'Unknown Stock Description'
    def getCode(self):
        return self.__code
    def setCode(self,code):
        self.__code=code
    def getQuantity(self):
        return self.__quantity
    def setQuantity(self,quantity):
        self.__quantity=quantity
    def getPrice(self):
        return self.__price
    def setPrice(self,price):
        self.__price=price
    
    # increase stock level
    def increaseStock(self,increament):
        self.__quantity+=increament
    # sell stock
    def sellStock(self,decreamnt):
        if decreamnt<1 or decreamnt>100:
            print('Please enter the suitable amount')
            return False
        else:
            print('reduction successful')
            self.__quantity-=decreamnt
            return True
    # get vat
    def getVat(self):
        return 17.5
    # get price with Vat
    def getPriceWithVat(self):
        return self.getPrice()+((self.getPrice()*17.5)/100)
    def __str__(self):
        return f' Item code: {self.getCode()}\n Item Name: {self.getStockName()}\n Item description: {self.getStockDescription()} \n Item stock: {self.getQuantity()}\n Item price before VAT: {self.getPrice()}\n Item price after VAT: {self.getPriceWithVat()}\n '
    
    
        
item=StockItem('1234',45,67.9)
print(type(item)==StockItem)
# item.getCode()
# item.getPrice()
# item.getPriceWithVat()
# item.getQuantity()
# item.getVat()
# item.sellStock(20)
# item.increaseStock(30)
# print(item)

        
        
        
        
