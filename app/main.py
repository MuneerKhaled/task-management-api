
class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity):
        return quantity > 0 and quantity <= self.stock


class Customer:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        self.cart.append({
            "product": product,
            "quantity": quantity
        })

    def empty_cart(self):
        self.cart = []


class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.product_code = 1
        self.customer_code = 1

    def get_product(self, code):
        for product in self.products:
            if product.code == code:
                return product
        return None

    def get_customer(self, code):
        for customer in self.customers:
            if customer.code == code:
                return customer
        return None

    def add_new_product(self):
        product_name = input("Product name: ")
        product_price = float(input("Product price: "))
        product_stock = int(input("Product stock: "))

        product = Product(
            self.product_code,
            product_name,
            product_price,
            product_stock
        )

        self.products.append(product)
        self.product_code += 1

        print("Product added.")

    def register_customer(self):
        customer_name = input("Customer name: ")

        customer = Customer(
            self.customer_code,
            customer_name
        )

        self.customers.append(customer)
        self.customer_code += 1

        print("Customer registered.")

    def list_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\nID\tName\tPrice\tStock")

        for product in self.products:
            print(
                product.code,
                product.name,
                product.price,
                product.stock,
                sep="\t"
            )

    def add_item(self):
        customer_code = int(input("Customer ID: "))
        product_code = int(input("Product ID: "))
        quantity = int(input("Quantity: "))

        customer = self.get_customer(customer_code)
        product = self.get_product(product_code)

        if customer is None:
            print("Customer not found.")
            return

        if product is None:
            print("Product not found.")
            return

        if not product.is_available(quantity):
            print("Invalid quantity or insufficient stock.")
            return

        customer.add_to_cart(product, quantity)
        print("Item added successfully.")

    def calculate_bill(self, customer):
        amount = 0

        for item in customer.cart:
            product = item["product"]
            quantity = item["quantity"]
            amount += product.price * quantity

        return amount

    def checkout_customer(self):
        customer_code = int(input("Customer ID: "))
        customer = self.get_customer(customer_code)

        if customer is None:
            print("Customer not found.")
            return

        if not customer.cart:
            print("No items in cart.")
            return

        total = self.calculate_bill(customer)

        if total >= 2000:
            discount = 10
        elif total >= 1000:
            discount = 5
        else:
            discount = 0

        payable = total - (total * discount / 100)

        for item in customer.cart:
            product = item["product"]
            quantity = item["quantity"]
            product.stock -= quantity

        print("\n--------- CUSTOMER BILL ---------")
        print("Customer:", customer.name)
        print("Original amount:", total)
        print("Discount:", discount, "%")
        print("Final amount:", payable)
        print("---------------------------------")

        customer.empty_cart()


def menu():
    shop = Store()

    while True:
        print("""
========= STORE MANAGEMENT =========

1. Add New Product
2. Register New Customer
3. List All Products
4. Add Item to Cart
5. Checkout Customer
6. Quit
""")

        option = input("Enter option: ")

        if option == "1":
            shop.add_new_product()

        elif option == "2":
            shop.register_customer()

        elif option == "3":
            shop.list_products()

        elif option == "4":
            shop.add_item()

        elif option == "5":
            shop.checkout_customer()

        elif option == "6":
            print("Goodbye!")
            break

        else:
            print("Wrong option.")


menu()