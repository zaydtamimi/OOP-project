from StockItem import StockItem
class RadiatorBeam(StockItem):
    def __init__(self,code,quantity,price,cap,brand):
        super(RadiatorBeam,self).__init__(code,quantity,price)
        self.__brand=brand
        self.__InLetTankCap=cap
        
    def getStockName(self):
        return "RadiatorBeam"
    def getStockDescription(self):
        return "used for internal cooling"
    def getBrand(self):
        return self.__brand
    def setBrand(self,brand):
        self.__brand=brand
        
    def getInLetTankCap(self):
        return self.__InLetTankCap
    def setInLetTankCap(self,InLetTankCap):
        self.__InLetTankCap=InLetTankCap
        
    
    def __str__(self):
        return super().__str__()+'inlet Tank Capacity: '+str(self.getInLetTankCap())+'\n Brand: '+self.getBrand()
    

# itemNav=RadiatorBeam('1234',45,67.9,45,'radio')
# print(itemNav)
        
