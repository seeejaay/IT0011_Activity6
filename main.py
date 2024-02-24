import os
class Item:
    output = ''
    def addItem(self,itemID,itemName,itemDescription,itemPrice):
        try:
            f = open('inventory.txt', 'a')
            self.output = f'{itemID}, {itemName}, {itemDescription}, {itemPrice}\n'
            f.write(self.output)
            f.close()
            print('Successfully Added Item.')
        except:
            print('Error Occured while writing in inventory.txt.')

    def readItems(self):
        try:
            f = open('inventory.txt', 'r')
            records = f.read()
            print("Showing All Items in inventory.txt: \n")
            print(records)
        except:
            print('Error Occured while tring to read inventory.txt.')
        
    def updateItem(self,itemID,itemName,itemDescription,itemPrice):
        try:
            f = open('inventory.txt', 'r')
            Items = f.readlines()
            f.close()
            
            f = open('inventory.txt', 'w')
            for item in Items:
                if item.split(',')[0] == itemID:
                    self.output = f'{itemID}, {itemName}, {itemDescription}, {itemPrice}\n'
                    f.write(self.output)
                else: 
                    f.write(item)
            f.close()
            print('Successfully Updated Item.')
        except: 
            print('Error Occured while updating record.')
    def deleteItem(self,itemID):
        try:
            f = open('inventory.txt','r')
            Items = f.readlines()
            f.close()
            
            f = open('inventory.txt','w')
            for item in Items:
                if item.split(',')[0] != itemID:
                    f.write(item)
                else: continue
            f.close()
            print('Successfully Deleted Item.')
        except: 
            print("Error Occured while deleting a record.")
            
def inputItemInfo():
    itemID = input('Enter item ID: ')
    itemName = input('Enter item name: ')
    itemDescription = input('Enter item description: ')
    itemPrice = input('Enter item price: ')
    return itemID, itemName, itemDescription, itemPrice

newItem = Item()
Notfinished = True
while Notfinished == True:
    try:
        print("Welcome to the inventory management system")
        print("1. Create\n2. Read\n3. Update\n4. Delete")
        choice = int(input('Choice: '))
    except ValueError:
        print('Please enter a number')
        os.system('pause')
        os.system('cls')
        continue

    if choice == 1:
        newItem.addItem(*inputItemInfo())
    elif choice == 2:
        newItem.readItems()
    elif choice == 3:
        newItem.updateItem(*inputItemInfo())
    elif choice == 4:
        itemID = input('Enter Item ID to delete: ')
        newItem.deleteItem(itemID)
    

    redo = input('Are you finished? (y/n): ')
    redo = redo.upper()
    
    if redo == 'Y':
        Notfinished = False
        break
    
    os.system('cls')
    
    