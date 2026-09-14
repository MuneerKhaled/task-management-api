
class Product:
    def __init__(self, pid, title, price, quantity):
        self.pid = pid
        self.title = title
        self.price = price
        self.quantity = quantity


class Customer:
    def __init__(self, cid, username):
        self.cid = cid
        self.username = username
        self.items = []


class Shop:
    def __init__(self):
        self.product_list = []
        self.customer_list = []
        self.p_count = 0
        self.c_count = 0

    def find_product(self, pid):
        for product in self.product_list:
            if product.pid == pid:
                return product
        return None

    def find_customer(self, cid):
        for customer in self.customer_list:
            if customer.cid == cid:
                return customer
        return None

    def create_product(self):
        self.p_count += 1

        title = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter stock quantity: "))

        product = Product(
            self.p_count,
            title,
            price,
            quantity
        )

        self.product_list.append(product)
        print("Product added successfully.")

    def create_customer(self):
        self.c_count += 1

        username = input("Enter customer name: ")

        customer = Customer(
            self.c_count,
            username
        )

        self.customer_list.append(customer)
        print("Customer registered successfully.")

    def show_products(self):
        if len(self.product_list) == 0:
            print("No products in store.")
            return

        print("\n----- STORE PRODUCTS -----")

        for product in self.product_list:
            print(
                f"{product.pid} | {product.title} | "
                f"₹{product.price} | Stock: {product.quantity}"
            )

    def add_item(self):
        cid = int(input("Enter customer ID: "))
        pid = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        customer = self.find_customer(cid)
        product = self.find_product(pid)

        if customer is None:
            print("Customer not found.")
            return

        if product is None:
            print("Product not found.")
            return

        if quantity <= 0:
            print("Invalid quantity.")
            return

        if quantity > product.quantity:
            print("Insufficient stock.")
            return

        customer.items.append((product, quantity))
        print("Item added to cart.")

    def calculate_price(self, customer):
        total = 0

        for product, quantity in customer.items:
            total += product.price * quantity

        return total

    def print_bill(self):
        cid = int(input("Enter customer ID: "))
        customer = self.find_customer(cid)

        if customer is None:
            print("Customer not found.")
            return

        if not customer.items:
            print("Cart is empty.")
            return

        total = self.calculate_price(customer)

        if total >= 2000:
            discount = 10
        elif total >= 1000:
            discount = 5
        else:
            discount = 0

        discount_amount = total * discount / 100
        payable = total - discount_amount

        for product, quantity in customer.items:
            product.quantity -= quantity

        print("\n========== BILL ==========")
        print("Customer:", customer.username)
        print("Total amount:", total)
        print("Discount:", discount, "%")
        print("Discount amount:", discount_amount)
        print("Final amount:", payable)
        print("===========================")

        customer.items.clear()


def start():
    shop = Shop()

    while True:
        print("""
========= SHOPPING SYSTEM =========

1. Create Product
2. Create Customer
3. Show Products
4. Add Item to Cart
5. Print Bill
6. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            shop.create_product()

        elif choice == "2":
            shop.create_customer()

        elif choice == "3":
            shop.show_products()

        elif choice == "4":
            shop.add_item()

        elif choice == "5":
            shop.print_bill()

        elif choice == "6":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    start()
                