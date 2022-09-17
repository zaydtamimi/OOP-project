from StockItem import StockItem
class Fenders(StockItem):
    def __init__(self,code,quantity,price,brand):
        super(Fenders,self).__init__(code,quantity,price)
        self.__brand=brand
        
    def getStockName(self):
        return "Fenders"
    def getStockDescription(self):
        return "cover wheel to prevent mud"
    def getBrand(self):
        return self.__brand
    def setBrand(self,brand):
        self.__brand=brand
        
    
    def __str__(self):
        return super().__str__()+'Brand: '+self.getBrand()
    

# itemNav=Fenders('1234',45,67.9,'fenos')
# print(itemNav)
        
