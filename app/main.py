
class Product:
    def __init__(self, number, title, cost, quantity):
        self.number = number
        self.title = title
        self.cost = cost
        self.quantity = quantity

    def display(self):
        print(
            f"ID: {self.number} | "
            f"Name: {self.title} | "
            f"Price: {self.cost} | "
            f"Stock: {self.quantity}"
        )


class Customer:
    def __init__(self, number, username):
        self.number = number
        self.username = username
        self.shopping_cart = []

    def add_item(self, product, amount):
        self.shopping_cart.append([product, amount])


class ShoppingStore:
    def __init__(self):
        self.inventory = []
        self.people = []

    def search_product(self, number):
        for product in self.inventory:
            if product.number == number:
                return product
        return None

    def search_customer(self, number):
        for customer in self.people:
            if customer.number == number:
                return customer
        return None

    def create_product(self):
        title = input("Product name: ")
        cost = float(input("Product price: "))
        quantity = int(input("Available quantity: "))

        new_product = Product(
            len(self.inventory) + 1,
            title,
            cost,
            quantity
        )

        self.inventory.append(new_product)
        print("New product created.")

    def create_customer(self):
        username = input("Customer name: ")

        new_customer = Customer(
            len(self.people) + 1,
            username
        )

        self.people.append(new_customer)
        print("New customer registered.")

    def display_inventory(self):
        if len(self.inventory) == 0:
            print("Inventory is empty.")
            return

        print("\n----- PRODUCT INVENTORY -----")

        for product in self.inventory:
            product.display()

    def purchase_product(self):
        customer_number = int(input("Customer ID: "))
        product_number = int(input("Product ID: "))
        amount = int(input("Enter quantity: "))

        customer = self.search_customer(customer_number)
        product = self.search_product(product_number)

        if customer is None:
            print("Customer does not exist.")
            return

        if product is None:
            print("Product does not exist.")
            return

        if amount <= 0:
            print("Enter a valid quantity.")
            return

        if amount > product.quantity:
            print("Insufficient stock.")
            return

        customer.add_item(product, amount)
        print("Item added to shopping cart.")

    def generate_bill(self):
        customer_number = int(input("Customer ID: "))
        customer = self.search_customer(customer_number)

        if customer is None:
            print("Customer not found.")
            return

        if not customer.shopping_cart:
            print("Shopping cart is empty.")
            return

        bill = 0

        for product, amount in customer.shopping_cart:
            bill += product.cost * amount

        if bill >= 2000:
            discount_rate = 0.10
        elif bill >= 1000:
            discount_rate = 0.05
        else:
            discount_rate = 0

        discount_value = bill * discount_rate
        payable = bill - discount_value

        for product, amount in customer.shopping_cart:
            product.quantity -= amount

        print("\n========== INVOICE ==========")
        print("Customer:", customer.username)
        print("Total price:", bill)
        print("Discount:", discount_value)
        print("Amount to pay:", payable)
        print("=============================")

        customer.shopping_cart = []


def run_store():
    shop = ShoppingStore()

    while True:
        print("""
========= SHOPPING MENU =========

1. Create Product
2. Register Customer
3. Display Inventory
4. Purchase Product
5. Generate Bill
6. Close Store
""")

        option = input("Select an option: ")

        if option == "1":
            shop.create_product()

        elif option == "2":
            shop.create_customer()

        elif option == "3":
            shop.display_inventory()

        elif option == "4":
            shop.purchase_product()

        elif option == "5":
            shop.generate_bill()

        elif option == "6":
            print("Store closed.")
            break

        else:
            print("Please select a valid option.")


run_store()