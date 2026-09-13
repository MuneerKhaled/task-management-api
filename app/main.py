
class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock


class Customer:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.cart = []


class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.product_id = 1
        self.customer_id = 1

    def find(self, collection, code, attribute):
        for obj in collection:
            if getattr(obj, attribute) == code:
                return obj
        return None

    def create_product(self):
        name = input("Name of product: ")
        price = float(input("Price of product: "))
        stock = int(input("Quantity in stock: "))

        self.products.append(
            Product(self.product_id, name, price, stock)
        )

        print("Product ID:", self.product_id)
        self.product_id += 1

    def create_customer(self):
        name = input("Name of customer: ")

        self.customers.append(
            Customer(self.customer_id, name)
        )

        print("Customer ID:", self.customer_id)
        self.customer_id += 1

    def show_products(self):
        print("\n========== PRODUCTS ==========")

        if not self.products:
            print("No products available.")
            return

        for p in self.products:
            print(
                f"ID: {p.code} | "
                f"Name: {p.name} | "
                f"Price: ₹{p.price} | "
                f"Stock: {p.stock}"
            )

    def add_to_cart(self):
        cid = int(input("Customer ID: "))
        pid = int(input("Product ID: "))
        quantity = int(input("Quantity: "))

        customer = self.find(self.customers, cid, "code")
        product = self.find(self.products, pid, "code")

        if customer is None or product is None:
            print("Invalid customer or product.")
            return

        if quantity <= 0 or quantity > product.stock:
            print("Invalid quantity or insufficient stock.")
            return

        customer.cart.append((product, quantity))
        print("Added to cart successfully.")

    def calculate_discount(self, total):
        if total >= 2000:
            return 0.10
        if total >= 1000:
            return 0.05
        return 0

    def checkout(self):
        cid = int(input("Customer ID: "))
        customer = self.find(self.customers, cid, "code")

        if customer is None:
            print("Customer not found.")
            return

        if len(customer.cart) == 0:
            print("Cart is empty.")
            return

        total = 0

        for product, quantity in customer.cart:
            total += product.price * quantity

        discount_rate = self.calculate_discount(total)
        discount_amount = total * discount_rate
        final_total = total - discount_amount

        for product, quantity in customer.cart:
            product.stock -= quantity

        print("\n========== INVOICE ==========")
        print("Customer:", customer.name)
        print("Subtotal:", total)
        print("Discount:", discount_amount)
        print("Amount payable:", final_total)
        print("=============================")

        customer.cart.clear()


def main():
    store = Store()

    commands = {
        "1": store.create_product,
        "2": store.create_customer,
        "3": store.show_products,
        "4": store.add_to_cart,
        "5": store.checkout
    }

    while True:
        print("""
========== STORE SYSTEM ==========

1. Create Product
2. Create Customer
3. Show Products
4. Add to Cart
5. Checkout
6. Exit
""")

        choice = input("Select option: ")

        if choice == "6":
            print("Thank you for using the store.")
            break

        if choice in commands:
            commands[choice]()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()