from StockItem import StockItem
class Bumpers(StockItem):
    def __init__(self,code,quantity,price,brand,side):
        super(Bumpers,self).__init__(code,quantity,price)
        self.__brand=brand
        self.__side=side
        
    def getStockName(self):
        return "Bumpers"
    def getStockDescription(self):
        return "prevent physical damage"
    def getBrand(self):
        return self.__brand
    def setBrand(self,brand):
        self.__brand=brand
     
    def getSide(self):
            return self.__side
    def setSide(self,side):
        self.__side=side
        
    
    
    def __str__(self):
        return super().__str__()+'Side: '+self.getSide() +'\n Brand: '+self.getBrand()
    

# itemNav=Bumpers('1234',45,67.9,'bumps','front')
# print(itemNav)
        
