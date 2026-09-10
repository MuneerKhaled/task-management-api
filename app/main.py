class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock


class Store:
    def __init__(self):
        self.products = []
        self.cart = []

    def add_product(self):
        name = input("Product name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        self.products.append(
            Product(len(self.products) + 1, name, price, stock)
        )
        print("Product added!")

    def show_products(self):
        for p in self.products:
            print(p.id, p.name, "₹", p.price, "Stock:", p.stock)

    def add_to_cart(self):
        id = int(input("Product ID: "))
        qty = int(input("Quantity: "))

        for p in self.products:
            if p.id == id:
                if qty <= p.stock:
                    self.cart.append((p, qty))
                    print("Added to cart!")
                else:
                    print("Not enough stock.")
                return

        print("Product not found.")

    def checkout(self):
        if not self.cart:
            print("Cart is empty.")
            return

        total = 0

        for p, qty in self.cart:
            total += p.price * qty
            p.stock -= qty

        if total >= 2000:
            discount = total * 0.10
        elif total >= 1000:
            discount = total * 0.05
        else:
            discount = 0

        print("Total:", total - discount)
        self.cart.clear()


store = Store()

while True:
    print("""
1. Add Product
2. Show Products
3. Add to Cart
4. Checkout
5. Exit
""")

    choice = input("Choice: ")

    if choice == "1":
        store.add_product()
    elif choice == "2":
        store.show_products()
    elif choice == "3":
        store.add_to_cart()
    elif choice == "4":
        store.checkout()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")