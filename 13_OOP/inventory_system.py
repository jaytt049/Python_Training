class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"{self.name} | Price: {self.price} | Qty: {self.quantity}")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("\nInventory:")
        for p in self.products:
            p.display()

    def total_value(self):
        total = 0
        for p in self.products:
            total += p.price * p.quantity
        return total


# Usage
p1 = Product("Laptop", 50000, 2)
p2 = Product("Mouse", 500, 5)

inv = Inventory()
inv.add_product(p1)
inv.add_product(p2)

inv.show_products()
print("Total Inventory Value:", inv.total_value())