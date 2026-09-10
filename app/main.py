class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock


class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cart = []


class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self):
        name = input("Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        self.products.append(
            Product(len(self.products) + 1, name, price, stock)
        )

    def add_customer(self):
        name = input("Customer name: ")
        self.customers.append(
            Customer(len(self.customers) + 1, name)
        )

    def products_list(self):
        for p in self.products:
            print(p.id, p.name, p.price, p.stock)

    def add_cart(self):
        cid = int(input("Customer ID: "))
        pid = int(input("Product ID: "))
        qty = int(input("Quantity: "))

        c = next((x for x in self.customers if x.id == cid), None)
        p = next((x for x in self.products if x.id == pid), None)

        if c and p and qty <= p.stock:
            c.cart.append((p, qty))
            print("Added!")
        else:
            print("Invalid request")

    def checkout(self):
        cid = int(input("Customer ID: "))
        c = next((x for x in self.customers if x.id == cid), None)

        if not c or not c.cart:
            print("Cart empty")
            return

        total = sum(p.price * q for p, q in c.cart)

        discount = 0.10 if total >= 2000 else 0.05 if total >= 1000 else 0

        for p, q in c.cart:
            p.stock -= q

        print("Total:", total * (1 - discount))
        c.cart.clear()


store = Store()

while True:
    print("""
1. Add Product
2. Add Customer
3. Show Products
4. Add to Cart
5. Checkout
6. Exit
""")

    ch = input("Choice: ")

    if ch == "1":
        store.add_product()
    elif ch == "2":
        store.add_customer()
    elif ch == "3":
        store.products_list()
    elif ch == "4":
        store.add_cart()
    elif ch == "5":
        store.checkout()
    elif ch == "6":
        break
    else:
        print("Invalid choice")