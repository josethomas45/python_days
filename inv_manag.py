class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}  

    def add_new_product(self, product_id, name, category, quantity, price, discount):
        if product_id in self.inventory:
            print(f"Error: Product ID {product_id} already exists. Choose a unique ID.\n")
            return

        fixed_details = (product_id, name, category) 
        variable_details = [quantity, price, discount] 
        self.inventory[product_id] = (fixed_details, variable_details) 

    def update_stock_level(self, product_id, new_stock_level):
        if product_id in self.inventory:
            self.inventory[product_id][1][0] = new_stock_level  
        else:
            print(f"Error: Product ID {product_id} not found.")

    def update_price(self, product_id, new_price):
        if product_id in self.inventory:
            self.inventory[product_id][1][1] = new_price  
        else:
            print(f"Error: Product ID {product_id} not found.")

    def update_discount(self, product_id, new_discount):
        if product_id in self.inventory:
            self.inventory[product_id][1][2] = new_discount 
        else:
            print(f"Error: Product ID {product_id} not found.")

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return

        print("\nInventory Details:")
        for product_id, (fixed_details, variable_details) in self.inventory.items():
            print(f"Product ID: {fixed_details[0]}")
            print(f"Name: {fixed_details[1]}")
            print(f"Category: {fixed_details[2]}")
            print(f"Quantity: {variable_details[0]}")
            print(f"Price: {variable_details[1]}")
            print(f"Discount: {variable_details[2]}%\n")

ims = InventoryManagementSystem()

ims.add_new_product(1, 'Iphone 16', 'Digital', 100, 100000, 10)
ims.add_new_product(3, 'T-shirt', 'Clothing', 200, 500, 20)
ims.add_new_product(2, 'Digital drawing pad', 'Digital', 50, 5000, 5)
ims.add_new_product(4, 'Jeans', 'Clothing', 150, 1000, 15)
ims.add_new_product(5, 'Sneakers', 'Footwear', 100, 2000, 10)
ims.add_new_product(7, 'Laptop', 'Electronics', 50, 50000, 10)
ims.add_new_product(6, 'Formal shoes', 'Footwear', 50, 3000, 5)

print("\nInventory Management System:")
ims.display_inventory()

print("\nUpdating stock level of Product ID 1:")
ims.update_stock_level(1, 50)

print("\nUpdating price of Product ID 2:")
ims.update_price(2, 6000)

print("\nUpdating discount of Product ID 3:")
ims.update_discount(3, 25)

print("\nUpdated Inventory:")
ims.display_inventory()
