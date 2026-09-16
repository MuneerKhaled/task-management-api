class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = []


class Shop:
    def __init__(self):
        self.products = []
        self.customers = []
        self.next_product_id = 1
        self.next_customer_id = 1

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        product = Product(
            self.next_product_id,
            name,
            price,
            quantity
        )

        self.products.append(product)
        self.next_product_id += 1

        print("Product added successfully.")

    def add_customer(self):
        name = input("Enter customer name: ")

        customer = Customer(
            self.next_customer_id,
            name
        )

        self.customers.append(customer)
        self.next_customer_id += 1

        print("Customer registered successfully.")

    def show_products(self):
        if not self.products:
            print("No products found.")
            return

        print("\n========== PRODUCT LIST ==========")

        for product in self.products:
            print(
                f"ID: {product.product_id} | "
                f"Name: {product.name} | "
                f"Price: ₹{product.price} | "
                f"Quantity: {product.quantity}"
            )

    def add_to_cart(self):
        customer_id = int(input("Enter customer ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        customer = self.find_customer(customer_id)
        product = self.find_product(product_id)

        if customer is None:
            print("Customer not found.")
            return

        if product is None:
            print("Product not found.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > product.quantity:
            print("Insufficient stock.")
            return

        customer.cart.append({
            "product": product,
            "quantity": quantity
        })

        print("Product added to cart successfully.")

    def calculate_total(self, customer):
        total = 0

        for item in customer.cart:
            product = item["product"]
            quantity = item["quantity"]

            total += product.price * quantity

        return total

    def print_bill(self):
        customer_id = int(input("Enter customer ID: "))

        customer = self.find_customer(customer_id)

        if customer is None:
            print("Customer not found.")
            return

        if not customer.cart:
            print("Cart is empty.")
            return

        total = self.calculate_total(customer)

        if total >= 3000:
            discount = 15
        elif total >= 1500:
            discount = 10
        elif total >= 500:
            discount = 5
        else:
            discount = 0

        discount_amount = total * discount / 100
        payable_amount = total - discount_amount

        for item in customer.cart:
            product = item["product"]
            quantity = item["quantity"]

            product.quantity -= quantity

        print("\n========== FINAL BILL ==========")
        print("Customer:", customer.name)
        print("--------------------------------")

        for item in customer.cart:
            product = item["product"]
            quantity = item["quantity"]

            print(
                f"{product.name} x {quantity} "
                f"= ₹{product.price * quantity}"
            )

        print("--------------------------------")
        print("Total Amount: ₹", total)
        print("Discount:", discount, "%")
        print("Discount Amount: ₹", discount_amount)
        print("Final Amount: ₹", payable_amount)
        print("================================")

        customer.cart.clear()


def start_shop():
    shop = Shop()

    while True:
        print("""
========== SHOPPING SYSTEM ==========

1. Add Product
2. Register Customer
3. Show Products
4. Add Product to Cart
5. Print Bill
6. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            shop.add_product()

        elif choice == "2":
            shop.add_customer()

        elif choice == "3":
            shop.show_products()

        elif choice == "4":
            shop.add_to_cart()

        elif choice == "5":
            shop.print_bill()

        elif choice == "6":
            print("Thank you for using our shopping system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    start_shop()