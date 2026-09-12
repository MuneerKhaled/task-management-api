
class Product:
    def __init__(self, product_id, product_name, product_price, product_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_stock = product_stock

    def reduce_stock(self, quantity):
        self.product_stock -= quantity


class Customer:
    def __init__(self, customer_id, customer_name):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.cart = {}


class Store:
    def __init__(self):
        self.product_data = {}
        self.customer_data = {}
        self.product_counter = 1
        self.customer_counter = 1

    def create_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        product = Product(
            self.product_counter,
            name,
            price,
            stock
        )

        self.product_data[self.product_counter] = product
        self.product_counter += 1

        print("Product created successfully.")

    def create_customer(self):
        name = input("Enter customer name: ")

        customer = Customer(
            self.customer_counter,
            name
        )

        self.customer_data[self.customer_counter] = customer
        self.customer_counter += 1

        print("Customer created successfully.")

    def display_products(self):
        if not self.product_data:
            print("No products found.")
            return

        print("\n-------- AVAILABLE PRODUCTS --------")

        for product in self.product_data.values():
            print(
                "ID:", product.product_id,
                "| Name:", product.product_name,
                "| Price:", product.product_price,
                "| Stock:", product.product_stock
            )

    def add_product_to_cart(self):
        customer_id = int(input("Enter customer ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        customer = self.customer_data.get(customer_id)
        product = self.product_data.get(product_id)

        if customer is None:
            print("Customer not found.")
            return

        if product is None:
            print("Product not found.")
            return

        if quantity <= 0:
            print("Invalid quantity.")
            return

        if quantity > product.product_stock:
            print("Not enough stock available.")
            return

        if product_id in customer.cart:
            customer.cart[product_id] += quantity
        else:
            customer.cart[product_id] = quantity

        print("Product added to cart.")

    def show_cart(self, customer):
        print("\n-------- SHOPPING CART --------")

        for product_id, quantity in customer.cart.items():
            product = self.product_data[product_id]

            print(
                product.product_name,
                "x", quantity,
                "=", product.product_price * quantity
            )

    def checkout(self):
        customer_id = int(input("Enter customer ID: "))
        customer = self.customer_data.get(customer_id)

        if customer is None:
            print("Customer not found.")
            return

        if not customer.cart:
            print("Your cart is empty.")
            return

        self.show_cart(customer)

        total_price = 0

        for product_id, quantity in customer.cart.items():
            product = self.product_data[product_id]
            total_price += product.product_price * quantity

        if total_price >= 2000:
            discount = 0.10
        elif total_price >= 1000:
            discount = 0.05
        else:
            discount = 0

        discount_amount = total_price * discount
        final_price = total_price - discount_amount

        for product_id, quantity in customer.cart.items():
            product = self.product_data[product_id]
            product.reduce_stock(quantity)

        print("\n========== BILL ==========")
        print("Customer:", customer.customer_name)
        print("Total:", total_price)
        print("Discount:", discount_amount)
        print("Payable amount:", final_price)
        print("==========================")

        customer.cart.clear()


def main():
    store = Store()

    while True:
        print("""
========== STORE MENU ==========

1. Create Product
2. Create Customer
3. Display Products
4. Add Product to Cart
5. Checkout
6. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            store.create_product()

        elif choice == "2":
            store.create_customer()

        elif choice == "3":
            store.display_products()

        elif choice == "4":
            store.add_product_to_cart()

        elif choice == "5":
            store.checkout()

        elif choice == "6":
            print("Exiting store system...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()