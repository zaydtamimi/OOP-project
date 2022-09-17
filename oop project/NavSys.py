from StockItem import StockItem
class NavSys(StockItem):
    def __init__(self,code,quantity,price,brand):
        super(NavSys,self).__init__(code,quantity,price)
        self.__brand=brand
        
    def getStockName(self):
        return "Navigation system"
    
    
    def getStockDescription(self):
        return "GeoVision Sat Nav"
    def getBrand(self):
        return self.__brand
    def setBrand(self,brand):
        self.__brand=brand
        
    
    def __str__(self):
        return super().__str__()+'Brand: '+self.getBrand()
    

# itemNav=NavSys('1234',45,67.9,'TomTom')
# print(itemNav)
        
