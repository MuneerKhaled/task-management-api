from datetime import datetime


# =========================================================
# Product Model
# =========================================================

class Product:

    def __init__(self, product_id, name, category, price, quantity):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.added_at = datetime.now()

    def add_stock(self, quantity):
        self.quantity += quantity

    def remove_stock(self, quantity):

        if quantity > self.quantity:
            print("\nNot enough stock.")
            return False

        self.quantity -= quantity
        return True

    def update_product(
        self,
        name=None,
        category=None,
        price=None,
        quantity=None
    ):

        if name:
            self.name = name

        if category:
            self.category = category

        if price is not None:
            self.price = price

        if quantity is not None:
            self.quantity = quantity

    def display(self):

        print("\n--------------------------------")
        print(f"Product ID : {self.id}")
        print(f"Name       : {self.name}")
        print(f"Category   : {self.category}")
        print(f"Price      : ₹{self.price}")
        print(f"Stock      : {self.quantity}")
        print(f"Added      : {self.added_at}")
        print("--------------------------------")


# =========================================================
# Customer Model
# =========================================================

class Customer:

    def __init__(self, customer_id, name, phone):

        self.id = customer_id
        self.name = name
        self.phone = phone
        self.cart = []
        self.total_spent = 0

    def add_to_cart(self, product, quantity):

        if quantity <= 0:
            print("\nInvalid quantity.")
            return False

        if quantity > product.quantity:
            print("\nNot enough stock.")
            return False

        self.cart.append({
            "product": product,
            "quantity": quantity
        })

        return True

    def clear_cart(self):
        self.cart.clear()

    def display(self):

        print("\n--------------------------------")
        print(f"Customer ID : {self.id}")
        print(f"Name        : {self.name}")
        print(f"Phone       : {self.phone}")
        print(f"Cart Items  : {len(self.cart)}")
        print(f"Total Spent : ₹{self.total_spent}")
        print("--------------------------------")


# =========================================================
# Store Manager
# =========================================================

class StoreManager:

    def __init__(self):

        self.products = []
        self.customers = []

        self.next_product_id = 1
        self.next_customer_id = 1

        self.total_sales = 0
        self.total_orders = 0

    # =====================================================
    # PRODUCT MANAGEMENT
    # =====================================================

    def add_product(
        self,
        name,
        category,
        price,
        quantity
    ):

        product = Product(
            self.next_product_id,
            name,
            category,
            price,
            quantity
        )

        self.products.append(product)

        self.next_product_id += 1

        print("\nProduct added successfully!")

    def get_product(self, product_id):

        for product in self.products:

            if product.id == product_id:
                return product

        return None

    def show_all_products(self):

        if not self.products:
            print("\nNo products found.")
            return

        print("\n========== ALL PRODUCTS ==========")

        for product in self.products:
            product.display()

    def update_product(
        self,
        product_id,
        name=None,
        category=None,
        price=None,
        quantity=None
    ):

        product = self.get_product(product_id)

        if product is None:
            print("\nProduct not found.")
            return

        product.update_product(
            name,
            category,
            price,
            quantity
        )

        print("\nProduct updated successfully!")

    def delete_product(self, product_id):

        product = self.get_product(product_id)

        if product is None:
            print("\nProduct not found.")
            return

        self.products.remove(product)

        print("\nProduct deleted successfully!")

    # =====================================================
    # SEARCH PRODUCTS
    # =====================================================

    def search_products(self, keyword):

        results = []

        keyword = keyword.lower()

        for product in self.products:

            if (
                keyword in product.name.lower()
                or keyword in product.category.lower()
            ):
                results.append(product)

        if not results:
            print("\nNo matching products found.")
            return

        print("\n========== SEARCH RESULTS ==========")

        for product in results:
            product.display()

    # =====================================================
    # LOW STOCK PRODUCTS
    # =====================================================

    def show_low_stock(self):

        low_stock = [
            product
            for product in self.products
            if product.quantity <= 5
        ]

        if not low_stock:
            print("\nNo low-stock products.")
            return

        print("\n========== LOW STOCK ==========")

        for product in low_stock:
            product.display()

    # =====================================================
    # CUSTOMER MANAGEMENT
    # =====================================================

    def add_customer(self, name, phone):

        customer = Customer(
            self.next_customer_id,
            name,
            phone
        )

        self.customers.append(customer)

        self.next_customer_id += 1

        print("\nCustomer added successfully!")

    def get_customer(self, customer_id):

        for customer in self.customers:

            if customer.id == customer_id:
                return customer

        return None

    def show_all_customers(self):

        if not self.customers:
            print("\nNo customers found.")
            return

        print("\n========== ALL CUSTOMERS ==========")

        for customer in self.customers:
            customer.display()

    # =====================================================
    # ADD TO CART
    # =====================================================

    def add_to_cart(
        self,
        customer_id,
        product_id,
        quantity
    ):

        customer = self.get_customer(customer_id)
        product = self.get_product(product_id)

        if customer is None:
            print("\nCustomer not found.")
            return

        if product is None:
            print("\nProduct not found.")
            return

        if customer.add_to_cart(
            product,
            quantity
        ):

            print(
                f"\n{product.name} "
                f"added to cart."
            )

    # =====================================================
    # SHOW CART
    # =====================================================

    def show_cart(self, customer_id):

        customer = self.get_customer(customer_id)

        if customer is None:
            print("\nCustomer not found.")
            return

        if not customer.cart:
            print("\nCart is empty.")
            return

        print("\n========== SHOPPING CART ==========")

        total = 0

        for item in customer.cart:

            product = item["product"]
            quantity = item["quantity"]

            item_total = product.price * quantity

            print(
                f"{product.name} x {quantity} "
                f"= ₹{item_total}"
            )

            total += item_total

        print("--------------------------------")
        print(f"Subtotal: ₹{total}")

    # =====================================================
    # CHECKOUT
    # =====================================================

    def checkout(self, customer_id):

        customer = self.get_customer(customer_id)

        if customer is None:
            print("\nCustomer not found.")
            return

        if not customer.cart:
            print("\nCart is empty.")
            return

        subtotal = 0

        print("\n========== BILL ==========")

        for item in customer.cart:

            product = item["product"]
            quantity = item["quantity"]

            if quantity > product.quantity:

                print(
                    f"\nNot enough stock for "
                    f"{product.name}."
                )

                return

            item_total = product.price * quantity

            subtotal += item_total

        # Discount
        if subtotal >= 2000:
            discount = subtotal * 0.10

        elif subtotal >= 1000:
            discount = subtotal * 0.05

        else:
            discount = 0

        final_amount = subtotal - discount

        # Remove stock
        for item in customer.cart:

            product = item["product"]
            quantity = item["quantity"]

            product.remove_stock(quantity)

        customer.total_spent += final_amount

        self.total_sales += final_amount
        self.total_orders += 1

        print(f"Subtotal : ₹{subtotal:.2f}")
        print(f"Discount : ₹{discount:.2f}")
        print("--------------------------------")
        print(f"Total    : ₹{final_amount:.2f}")
        print("--------------------------------")

        customer.clear_cart()

        print("\nPurchase completed successfully!")

    # =====================================================
    # STORE STATISTICS
    # =====================================================

    def show_statistics(self):

        total_products = len(self.products)

        total_customers = len(self.customers)

        total_stock = sum(
            product.quantity
            for product in self.products
        )

        print("\n========== STORE STATISTICS ==========")

        print(f"Products       : {total_products}")
        print(f"Customers      : {total_customers}")
        print(f"Total Stock    : {total_stock}")
        print(f"Total Orders   : {self.total_orders}")
        print(f"Total Sales    : ₹{self.total_sales:.2f}")


# =========================================================
# Menu
# =========================================================

def show_menu():

    print("\n")
    print("==========================================")
    print("       GROCERY STORE MANAGEMENT SYSTEM")
    print("==========================================")

    print("\nPRODUCT MANAGEMENT")
    print("1. Add product")
    print("2. Show all products")
    print("3. Update product")
    print("4. Delete product")
    print("5. Search products")
    print("6. Show low-stock products")

    print("\nCUSTOMER MANAGEMENT")
    print("7. Add customer")
    print("8. Show all customers")

    print("\nSHOPPING")
    print("9. Add product to cart")
    print("10. Show cart")
    print("11. Checkout")

    print("\nOTHER")
    print("12. Show store statistics")
    print("13. Exit")

    print("==========================================")


# =========================================================
# Main Application
# =========================================================

def main():

    store = StoreManager()

    # -----------------------------------------------------
    # Sample Products
    # -----------------------------------------------------

    store.add_product(
        "Rice",
        "Grocery",
        60,
        50
    )

    store.add_product(
        "Milk",
        "Dairy",
        30,
        40
    )

    store.add_product(
        "Bread",
        "Bakery",
        40,
        25
    )

    store.add_product(
        "Apples",
        "Fruits",
        120,
        20
    )

    store.add_product(
        "Soap",
        "Personal Care",
        45,
        30
    )

    # -----------------------------------------------------
    # Sample Customers
    # -----------------------------------------------------

    store.add_customer(
        "Muneer",
        "9876543210"
    )

    store.add_customer(
        "Rahul",
        "9876501234"
    )

    # -----------------------------------------------------
    # Application Loop
    # -----------------------------------------------------

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        # -------------------------------------------------
        # Add Product
        # -------------------------------------------------

        if choice == "1":

            try:

                name = input("Enter product name: ")
                category = input("Enter category: ")

                price = float(
                    input("Enter price: ")
                )

                quantity = int(
                    input("Enter quantity: ")
                )

                store.add_product(
                    name,
                    category,
                    price,
                    quantity
                )

            except ValueError:

                print("\nInvalid price or quantity.")

        # -------------------------------------------------
        # Show Products
        # -------------------------------------------------

        elif choice == "2":

            store.show_all_products()

        # -------------------------------------------------
        # Update Product
        # -------------------------------------------------

        elif choice == "3":

            try:

                product_id = int(
                    input("Enter product ID: ")
                )

                name = input("Enter new name: ")
                category = input("Enter new category: ")

                price = float(
                    input("Enter new price: ")
                )

                quantity = int(
                    input("Enter new quantity: ")
                )

                store.update_product(
                    product_id,
                    name,
                    category,
                    price,
                    quantity
                )

            except ValueError:

                print("\nInvalid input.")

        # -------------------------------------------------
        # Delete Product
        # -------------------------------------------------

        elif choice == "4":

            try:

                product_id = int(
                    input("Enter product ID: ")
                )

                store.delete_product(product_id)

            except ValueError:

                print("\nInvalid product ID.")

        # -------------------------------------------------
        # Search
        # -------------------------------------------------

        elif choice == "5":

            keyword = input(
                "Enter product name or category: "
            )

            store.search_products(keyword)

        # -------------------------------------------------
        # Low Stock
        # -------------------------------------------------

        elif choice == "6":

            store.show_low_stock()

        # -------------------------------------------------
        # Add Customer
        # -------------------------------------------------

        elif choice == "7":

            name = input("Enter customer name: ")
            phone = input("Enter phone number: ")

            store.add_customer(
                name,
                phone
            )

        # -------------------------------------------------
        # Show Customers
        # -------------------------------------------------

        elif choice == "8":

            store.show_all_customers()

        # -------------------------------------------------
        # Add To Cart
        # -------------------------------------------------

        elif choice == "9":

            try:

                customer_id = int(
                    input("Enter customer ID: ")
                )

                product_id = int(
                    input("Enter product ID: ")
                )

                quantity = int(
                    input("Enter quantity: ")
                )

                store.add_to_cart(
                    customer_id,
                    product_id,
                    quantity
                )

            except ValueError:

                print("\nInvalid input.")

        # -------------------------------------------------
        # Show Cart
        # -------------------------------------------------

        elif choice == "10":

            try:

                customer_id = int(
                    input("Enter customer ID: ")
                )

                store.show_cart(customer_id)

            except ValueError:

                print("\nInvalid customer ID.")

        # -------------------------------------------------
        # Checkout
        # -------------------------------------------------

        elif choice == "11":

            try:

                customer_id = int(
                    input("Enter customer ID: ")
                )

                store.checkout(customer_id)

            except ValueError:

                print("\nInvalid customer ID.")

        # -------------------------------------------------
        # Statistics
        # -------------------------------------------------

        elif choice == "12":

            store.show_statistics()

        # -------------------------------------------------
        # Exit
        # -------------------------------------------------

        elif choice == "13":

            print(
                "\nThank you for using "
                "the Grocery Store Management System!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please try again."
            )


# =========================================================
# Start Application
# =========================================================

if __name__ == "__main__":
    main()
    