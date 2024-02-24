class operations:
    output = ''
    def create(self,id,name,description,price):
        f = open('inventory.txt', 'a')
        self.output += f'{id}, {name}, {description}, {price}\n'
        f.write(self.output)
        f.close()
    def read(self):
        f = open('inventory.txt', 'r')
        records = f.read()
        print(records)
        f.close()
    def update(self):
        id = input('ID to edit: ')
        name = input('Name to edit: ')
        description = input('Description to edit: ')
        price = input('Price to edit: ')
        
        f = open('inventory.txt', 'r')
        records = f.readlines()
        f.close()
        
        f = open('inventory.txt', 'w')
        for record in records:
            if record.split(',')[0] == id:
                f.write(f'{id}, {name}, {description}, {price}')
            else: 
                f.write(record)
        f.close()
        
    def delete(self):
        f = open('inventory.txt', 'a')
        f.write('')
        
operate = operations()

print("Welcome to the inventory management system")
print("1. Create\n2. Read\n3. Update\n3. Delete")
choice = int(input('Choice: '))

if choice == 1:
    operate.create(1,'Banana','Fruit','$1.00')
elif choice == 2:
    operate.read()
elif choice == 3:
    operate.update()
elif choice == 4:
    operate.delete()