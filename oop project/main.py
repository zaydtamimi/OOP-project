
from NavSys import NavSys
from Fenders import Fenders
from Bumpers import Bumpers
from RadiatorBeam import RadiatorBeam
print('------- CAR PARTS AND ACCESSORIES -------')
parts=[]
parts.append(NavSys('1234',45,67.9,'TomTom'))
parts.append(Fenders('1234',45,67.9,'fenos'))
parts.append(Bumpers('1234',45,67.9,'bumps','front'))
parts.append(RadiatorBeam('1234',45,67.9,45,'radio'))
counter=1

def menu():
    print('1 - Show stock items')
    print('2 - edit/sell stock item')
    
    print('3 - exit')
    ch=int(input('Enter choice: '))
    return ch

def printStockItems():
    counter=1
    for item in parts:
        print('---- '+str(counter)+' ----')
        print(item)
        print()
        counter=counter+1    

def editNavSys():
    print('---- NavSys ----')
    print('1 - Edit code')
    print('2 - Edit Quantity')
    print('3 - Edit Price')
    print('4 - Increase Stock')
    print('5 - Sell Stock')
    print('6 - Get Item Information')
    print('7 - Back')
    ch=int(input('Enter choice: '))
    if ch==1:
        new_code=input('Enter new code: ')
        parts[0].setCode(new_code)
    elif ch==2:
        new_quantity=int(input('Enter new quantity: '))
        parts[0].setQuantity(new_quantity)
    elif ch==3:
        new_price=float(input('Enter new price: '))
        parts[0].setPrice(new_price)
    elif ch==4:
        stock_increament=int(input('Enter stock increament: '))
        parts[0].increaseStock(stock_increament)
    elif ch==5:
        sell_stock=int(input('Enter sell stock quantity: '))
        parts[0].sellStock(sell_stock)
    elif ch==6:
        print(parts[0])
    elif ch==7:
        pass
    
def editFenders():
    print('---- Fendors ----')
    print('1 - Edit code')
    print('2 - Edit Quantity')
    print('3 - Edit Price')
    print('4 - Increase Stock')
    print('5 - Sell Stock')
    print('6 - Get Item Information')
    print('7 - Back')
    ch=int(input('Enter choice: '))
    if ch==1:
        new_code=input('Enter new code: ')
        parts[1].setCode(new_code)
    elif ch==2:
        new_quantity=int(input('Enter new quantity: '))
        parts[1].setQuantity(new_quantity)
    elif ch==3:
        new_price=float(input('Enter new price: '))
        parts[1].setPrice(new_price)
    elif ch==4:
        stock_increament=int(input('Enter stock increament: '))
        parts[1].increaseStock(stock_increament)
    elif ch==5:
        sell_stock=int(input('Enter sell stock quantity: '))
        parts[1].sellStock(sell_stock)
    elif ch==6:
        print(parts[1])
    elif ch==7:
        pass
    
def editBumpers():
    print('---- Bumpers ----')
    print('1 - Edit code')
    print('2 - Edit Quantity')
    print('3 - Edit Price')
    print('4 - Edit Bumper Side')
    print('5 - Increase Stock')
    print('6 - Sell Stock')
    print('7 - Get Item Information')
    print('8 - Back')
    ch=int(input('Enter choice: '))
    if ch==1:
        new_code=input('Enter new code: ')
        parts[2].setCode(new_code)
    elif ch==2:
        new_quantity=int(input('Enter new quantity: '))
        parts[2].setQuantity(new_quantity)
    elif ch==3:
        new_price=float(input('Enter new price: '))
        parts[2].setPrice(new_price)
    elif ch==4:
        new_side=input('Enter bumper side: ')
        parts[2].setSide(new_side)
    elif ch==5:
        stock_increament=int(input('Enter stock increament: '))
        parts[2].increaseStock(stock_increament)
    elif ch==6:
        sell_stock=int(input('Enter sell stock quantity: '))
        parts[2].sellStock(sell_stock)
    elif ch==7:
        print(parts[2])
    elif ch==8:
        pass
    
def editRadiatorsBeam():
    print('---- NavSys ----')
    print('1 - Edit code')
    print('2 - Edit Quantity')
    print('3 - Edit Price')
    print('4 - Edit InletTank Capcity')
    print('5 - Increase Stock')
    print('6 - Sell Stock')
    print('7 - Get Item Information')
    print('8 - Back')
    ch=int(input('Enter choice: '))
    if ch==1:
        new_code=input('Enter new code: ')
        parts[0].setCode(new_code)
    elif ch==2:
        new_quantity=int(input('Enter new quantity: '))
        parts[0].setQuantity(new_quantity)
    elif ch==3:
        new_price=float(input('Enter new price: '))
        parts[0].setPrice(new_price)
    elif ch==4:
        new_cap=float(input('Enter new capcity: '))
        parts[0].setInLetTankCap(new_cap)
    elif ch==5:
        stock_increament=int(input('Enter stock increament: '))
        parts[0].increaseStock(stock_increament)
    elif ch==6:
        sell_stock=int(input('Enter sell stock quantity: '))
        parts[0].sellStock(sell_stock)
    elif ch==7:
        print(parts[0])
    elif ch==8:
        pass
    

ch=menu()
while ch!=4:

    if ch==1:
        printStockItems()
    elif ch==2:
        printStockItems()
        item=int(input('select stock item: '))
        
        if item==1:
            editNavSys()
        elif item==2:
            editFenders()
        elif item==3:
            editBumpers()
        elif item==4:
            editRadiatorsBeam()
        else:
            pass
    else:
        break
        
    ch=menu()
