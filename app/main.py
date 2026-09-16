# ============================================================
#              SHOPPING MANAGEMENT SYSTEM
# ============================================================
# This program demonstrates Object-Oriented Programming (OOP)
# concepts in Python.
#
# Main features:
# 1. Add products
# 2. Update products
# 3. Remove products
# 4. Search products
# 5. Register customers
# 6. Show customers
# 7. Add products to cart
# 8. Remove products from cart
# 9. Update cart quantity
# 10. View cart
# 11. Calculate total
# 12. Apply discount
# 13. Checkout
# 14. Print bill
# 15. Store order history
# 16. Show order history
# 17. Show shop statistics
# 18. Main menu
# ============================================================


# ============================================================
# PRODUCT CLASS
# ============================================================

class Product:

    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display(self):
        print("---------------------------------------------")
        print("Product ID :", self.product_id)
        print("Name       :", self.name)
        print("Category   :", self.category)
        print("Price      : ₹", self.price)
        print("Stock      :", self.quantity)
        print("---------------------------------------------")

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def reduce_stock(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            return True

        return False

    def increase_stock(self, quantity):
        self.quantity += quantity


# ============================================================
# CART ITEM CLASS
# ============================================================

class CartItem:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        return self.product.price * self.quantity

    def display(self):
        total = self.get_total()

        print(
            f"{self.product.name} | "
            f"Quantity: {self.quantity} | "
            f"Price: ₹{self.product.price} | "
            f"Total: ₹{total}"
        )


# ============================================================
# ORDER ITEM CLASS
# ============================================================

class OrderItem:

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity

    def display(self):
        print(
            f"{self.product_name} x {self.quantity} "
            f"= ₹{self.get_total()}"
        )


# ============================================================
# ORDER CLASS
# ============================================================

class Order:

    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
        self.total = 0
        self.discount = 0
        self.discount_amount = 0
        self.final_amount = 0

    def add_item(self, product_name, price, quantity):

        item = OrderItem(
            product_name,
            price,
            quantity
        )

        self.items.append(item)

    def calculate_total(self):

        self.total = 0

        for item in self.items:
            self.total += item.get_total()

        return self.total

    def calculate_discount(self):

        self.calculate_total()

        if self.total >= 5000:
            self.discount = 20

        elif self.total >= 3000:
            self.discount = 15

        elif self.total >= 1500:
            self.discount = 10

        elif self.total >= 500:
            self.discount = 5

        else:
            self.discount = 0

        self.discount_amount = (
            self.total * self.discount / 100
        )

        self.final_amount = (
            self.total - self.discount_amount
        )

        return self.final_amount

    def display_order(self):

        print("\n=============================================")
        print("                 ORDER")
        print("=============================================")

        print("Order ID      :", self.order_id)
        print("Customer Name :", self.customer_name)

        print("---------------------------------------------")

        for item in self.items:
            item.display()

        print("---------------------------------------------")

        print("Total Amount  : ₹", self.total)
        print("Discount      :", self.discount, "%")
        print("Discount Amt  : ₹", self.discount_amount)
        print("Final Amount  : ₹", self.final_amount)

        print("=============================================")


# ============================================================
# CUSTOMER CLASS
# ============================================================

class Customer:

    def __init__(self, customer_id, name, phone, email):

        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

        self.cart = []
        self.order_history = []

    # --------------------------------------------------------
    # Add item to cart
    # --------------------------------------------------------

    def add_to_cart(self, product, quantity):

        for item in self.cart:

            if item.product.product_id == product.product_id:

                item.quantity += quantity

                return

        item = CartItem(
            product,
            quantity
        )

        self.cart.append(item)

    # --------------------------------------------------------
    # Remove item from cart
    # --------------------------------------------------------

    def remove_from_cart(self, product_id):

        for item in self.cart:

            if item.product.product_id == product_id:

                self.cart.remove(item)

                return True

        return False

    # --------------------------------------------------------
    # Update cart quantity
    # --------------------------------------------------------

    def update_cart_quantity(
        self,
        product_id,
        quantity
    ):

        for item in self.cart:

            if item.product.product_id == product_id:

                item.quantity = quantity

                return True

        return False

    # --------------------------------------------------------
    # Find cart item
    # --------------------------------------------------------

    def find_cart_item(self, product_id):

        for item in self.cart:

            if item.product.product_id == product_id:

                return item

        return None

    # --------------------------------------------------------
    # Calculate cart total
    # --------------------------------------------------------

    def calculate_cart_total(self):

        total = 0

        for item in self.cart:

            total += item.get_total()

        return total

    # --------------------------------------------------------
    # Clear cart
    # --------------------------------------------------------

    def clear_cart(self):

        self.cart.clear()

    # --------------------------------------------------------
    # Display customer
    # --------------------------------------------------------

    def display_customer(self):

        print("---------------------------------------------")

        print("Customer ID :", self.customer_id)
        print("Name        :", self.name)
        print("Phone       :", self.phone)
        print("Email       :", self.email)

        print("---------------------------------------------")


# ============================================================
# SHOP CLASS
# ============================================================

class Shop:

    def __init__(self):

        self.products = []
        self.customers = []
        self.orders = []

        self.next_product_id = 1
        self.next_customer_id = 1
        self.next_order_id = 1

    # ========================================================
    # PRODUCT METHODS
    # ========================================================

    # --------------------------------------------------------
    # Find product
    # --------------------------------------------------------

    def find_product(self, product_id):

        for product in self.products:

            if product.product_id == product_id:

                return product

        return None

    # --------------------------------------------------------
    # Add product
    # --------------------------------------------------------

    def add_product(self):

        print("\n========== ADD PRODUCT ==========")

        name = input("Enter product name: ")

        category = input(
            "Enter product category: "
        )

        try:

            price = float(
                input("Enter product price: ")
            )

            quantity = int(
                input("Enter product quantity: ")
            )

        except ValueError:

            print("Invalid price or quantity.")

            return

        if price <= 0:

            print("Price must be greater than zero.")

            return

        if quantity < 0:

            print("Quantity cannot be negative.")

            return

        product = Product(
            self.next_product_id,
            name,
            category,
            price,
            quantity
        )

        self.products.append(product)

        self.next_product_id += 1

        print("Product added successfully.")

    # --------------------------------------------------------
    # Show products
    # --------------------------------------------------------

    def show_products(self):

        if len(self.products) == 0:

            print("\nNo products available.")

            return

        print("\n")
        print("============================================================")
        print("                     PRODUCT LIST")
        print("============================================================")

        for product in self.products:

            print(
                f"ID: {product.product_id} | "
                f"Name: {product.name} | "
                f"Category: {product.category} | "
                f"Price: ₹{product.price} | "
                f"Stock: {product.quantity}"
            )

        print("============================================================")

    # --------------------------------------------------------
    # Search product
    # --------------------------------------------------------

    def search_product(self):

        keyword = input(
            "Enter product name or category to search: "
        ).lower()

        found = False

        print("\n========== SEARCH RESULTS ==========")

        for product in self.products:

            if (
                keyword in product.name.lower()
                or keyword in product.category.lower()
            ):

                print(
                    f"ID: {product.product_id} | "
                    f"Name: {product.name} | "
                    f"Category: {product.category} | "
                    f"Price: ₹{product.price} | "
                    f"Stock: {product.quantity}"
                )

                found = True

        if not found:

            print("No matching products found.")

    # --------------------------------------------------------
    # Update product
    # --------------------------------------------------------

    def update_product(self):

        try:

            product_id = int(
                input("Enter product ID: ")
            )

        except ValueError:

            print("Invalid product ID.")

            return

        product = self.find_product(product_id)

        if product is None:

            print("Product not found.")

            return

        print("\nProduct found.")

        product.display()

        print("\n1. Update Name")
        print("2. Update Category")
        print("3. Update Price")
        print("4. Update Quantity")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            product.name = input(
                "Enter new name: "
            )

            print("Name updated.")

        elif choice == "2":

            product.category = input(
                "Enter new category: "
            )

            print("Category updated.")

        elif choice == "3":

            try:

                price = float(
                    input("Enter new price: ")
                )

                if price <= 0:

                    print("Price must be positive.")

                    return

                product.update_price(price)

                print("Price updated.")

            except ValueError:

                print("Invalid price.")

        elif choice == "4":

            try:

                quantity = int(
                    input("Enter new quantity: ")
                )

                if quantity < 0:

                    print("Quantity cannot be negative.")

                    return

                product.update_quantity(quantity)

                print("Quantity updated.")

            except ValueError:

                print("Invalid quantity.")

        else:

            print("Invalid choice.")

    # --------------------------------------------------------
    # Remove product
    # --------------------------------------------------------

    def remove_product(self):

        try:

            product_id = int(
                input("Enter product ID: ")
            )

        except ValueError:

            print("Invalid product ID.")

            return

        product = self.find_product(product_id)

        if product is None:

            print("Product not found.")

            return

        self.products.remove(product)

        print("Product removed successfully.")

    # ========================================================
    # CUSTOMER METHODS
    # ========================================================

    # --------------------------------------------------------
    # Find customer
    # --------------------------------------------------------

    def find_customer(self, customer_id):

        for customer in self.customers:

            if customer.customer_id == customer_id:

                return customer

        return None

    # --------------------------------------------------------
    # Register customer
    # --------------------------------------------------------

    def add_customer(self):

        print("\n========== CUSTOMER REGISTRATION ==========")

        name = input(
            "Enter customer name: "
        )

        phone = input(
            "Enter phone number: "
        )

        email = input(
            "Enter email: "
        )

        customer = Customer(
            self.next_customer_id,
            name,
            phone,
            email
        )

        self.customers.append(customer)

        self.next_customer_id += 1

        print(
            "Customer registered successfully."
        )

    # --------------------------------------------------------
    # Show customers
    # --------------------------------------------------------

    def show_customers(self):

        if len(self.customers) == 0:

            print("No customers registered.")

            return

        print("\n========== CUSTOMER LIST ==========")

        for customer in self.customers:

            customer.display_customer()

    # ========================================================
    # CART METHODS
    # ========================================================

    # --------------------------------------------------------
    # Add product to cart
    # --------------------------------------------------------

    def add_to_cart(self):

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

        except ValueError:

            print("Invalid input.")

            return

        customer = self.find_customer(
            customer_id
        )

        if customer is None:

            print("Customer not found.")

            return

        product = self.find_product(
            product_id
        )

        if product is None:

            print("Product not found.")

            return

        if quantity <= 0:

            print(
                "Quantity must be greater than zero."
            )

            return

        existing_item = customer.find_cart_item(
            product_id
        )

        current_quantity = 0

        if existing_item is not None:

            current_quantity = existing_item.quantity

        if current_quantity + quantity > product.quantity:

            print("Not enough stock.")

            return

        customer.add_to_cart(
            product,
            quantity
        )

        print(
            "Product added to cart successfully."
        )

    # --------------------------------------------------------
    # View cart
    # --------------------------------------------------------

    def view_cart(self):

        try:

            customer_id = int(
                input("Enter customer ID: ")
            )

        except ValueError:

            print("Invalid customer ID.")

            return

        customer = self.find_customer(
            customer_id
        )

        if customer is None:

            print("Customer not found.")

            return

        if len(customer.cart) == 0:

            print("Cart is empty.")

            return

        print("\n")
        print("============================================================")
        print("                         CART")
        print("============================================================")

        for item in customer.cart:

            item.display()

        print("------------------------------------------------------------")

        total = customer.calculate_cart_total()

        print("Cart Total: ₹", total)

        print("============================================================")

    # --------------------------------------------------------
    # Remove item from cart
    # --------------------------------------------------------

    def remove_from_cart(self):

        try:

            customer_id = int(
                input("Enter customer ID: ")
            )

            product_id = int(
                input("Enter product ID: ")
            )

        except ValueError:

            print("Invalid input.")

            return

        customer = self.find_customer(
            customer_id
        )

        if customer is None:

            print("Customer not found.")

            return

        result = customer.remove_from_cart(
            product_id
        )

        if result:

            print(
                "Product removed from cart."
            )

        else:

            print(
                "Product not found in cart."
            )

    # --------------------------------------------------------
    # Update cart quantity
    # --------------------------------------------------------

    def update_cart(self):

        try:

            customer_id = int(
                input("Enter customer ID: ")
            )

            product_id = int(
                input("Enter product ID: ")
            )

            quantity = int(
                input("Enter new quantity: ")
            )

        except ValueError:

            print("Invalid input.")

            return

        customer = self.find_customer(
            customer_id
        )

        if customer is None:

            print("Customer not found.")

            return

        product = self.find_product(
            product_id
        )

        if product is None:

            print("Product not found.")

            return

        if quantity <= 0:

            print("Quantity must be greater than zero.")

            return

        if quantity > product.quantity:

            print("Not enough stock.")

            return

        result = customer.update_cart_quantity(
            product_id,
            quantity
        )

        if result:

            print(
                "Cart quantity updated."
            )

        else:

            print(
                "Product not found in cart."
            )

    # ========================================================
    # BILLING METHODS
    # ========================================================

    # --------------------------------------------------------
    # Calculate discount
    # --------------------------------------------------------

    def calculate_discount(self, total):

        if total >= 5000:

            return 20

        elif total >= 3000:

            return 15

        elif total >= 1500:

            return 10

        elif total >= 500:

            return 5

        else:

            return 0

    # --------------------------------------------------------
    # Checkout
    # --------------------------------------------------------

    def checkout(self):

        try:

            customer_id = int(
                input("Enter customer ID: ")
            )

        except ValueError:

            print("Invalid customer ID.")

            return

        customer = self.find_customer(
            customer_id
        )

        if customer is None:

            print("Customer not found.")

            return

        if len(customer.cart) == 0:

            print("Cart is empty.")

            return

        # Check stock one more time
        for item in customer.cart:

            product = item.product

            if item.quantity > product.quantity:

                print(
                    f"Not enough stock for {product.name}."
                )

                return

        # Create order
        order = Order(
            self.next_order_id,
            customer.name
        )

        # Add items to order
        for item in customer.cart:

            product = item.product

            order.add_item(
                product.name,
                product.price,
                item.quantity
            )

        # Calculate price
        order.calculate_discount()

        # Reduce stock
        for item in customer.cart:

            product = item.product

            product.reduce_stock(
                item.quantity
            )

        # Save order
        self.orders.append(order)

        self.next_order_id += 1

        # Print bill
        print("\n")
        print("*****************************************************")
        print("                    FINAL BILL")
        print("*****************************************************")

        print(
            "Order ID      :",
            order.order_id
        )

        print(
            "Customer Name :",
            customer.name
        )

        print("-----------------------------------------------------")

        for item in order.items:

            item.display()

        print("-----------------------------------------------------")

        print(
            "Total Amount  : ₹",
            order.total
        )

        print(
            "Discount      :",
            order.discount,
            "%"
        )

        print(
            "Discount Amt  : ₹",
            order.discount_amount
        )

        print(
            "Final Amount  : ₹",
            order.final_amount
        )

        print("*****************************************************")
        print("             THANK YOU FOR SHOPPING")
        print("*****************************************************")

        # Clear cart
        customer.clear_cart()

        # Save order in customer history
        customer.order_history.append(order)

        print(
            "\nCheckout completed successfully."
        )

    # ========================================================
    # ORDER HISTORY
    # ========================================================

    # --------------------------------------------------------
    # Show all orders
    # --------------------------------------------------------

    def show_all_orders(self):

        if len(self.orders) == 0:

            print("No orders found.")

            return

        print("\n========== ALL ORDERS ==========")

        for order in self.orders:

            order.display_order()

    # --------------------------------------------------------
    # Show customer order history
    # --------------------------------------------------------

    def show_customer_orders(self):

        try:

            customer_id = int(
                input("Enter customer ID: ")
            )

        except ValueError:

            print("Invalid customer ID.")

            return

        customer = self.find_customer(
            customer_id
        )

        if customer is None:

            print("Customer not found.")

            return

        if len(customer.order_history) == 0:

            print(
                "Customer has no previous orders."
            )

            return

        print("\n========== ORDER HISTORY ==========")

        for order in customer.order_history:

            order.display_order()

    # ========================================================
    # SHOP STATISTICS
    # ========================================================

    def shop_statistics(self):

        print("\n")
        print("============================================================")
        print("                    SHOP STATISTICS")
        print("============================================================")

        total_products = len(
            self.products
        )

        total_customers = len(
            self.customers
        )

        total_orders = len(
            self.orders
        )

        total_stock = 0

        for product in self.products:

            total_stock += product.quantity

        total_sales = 0

        for order in self.orders:

            total_sales += order.final_amount

        print(
            "Number of Products  :",
            total_products
        )

        print(
            "Number of Customers :",
            total_customers
        )

        print(
            "Number of Orders    :",
            total_orders
        )

        print(
            "Available Stock     :",
            total_stock
        )

        print(
            "Total Sales         : ₹",
            total_sales
        )

        print("============================================================")

    # ========================================================
    # LOW STOCK PRODUCTS
    # ========================================================

    def show_low_stock(self):

        print("\n========== LOW STOCK PRODUCTS ==========")

        found = False

        for product in self.products:

            if product.quantity <= 5:

                print(
                    f"ID: {product.product_id} | "
                    f"{product.name} | "
                    f"Stock: {product.quantity}"
                )

                found = True

        if not found:

            print("No low-stock products.")

    # ========================================================
    # OUT OF STOCK PRODUCTS
    # ========================================================

    def show_out_of_stock(self):

        print("\n========== OUT OF STOCK PRODUCTS ==========")

        found = False

        for product in self.products:

            if product.quantity == 0:

                print(
                    f"ID: {product.product_id} | "
                    f"Name: {product.name}"
                )

                found = True

        if not found:

            print("No products are out of stock.")

    # ========================================================
    # MOST EXPENSIVE PRODUCT
    # ========================================================

    def show_most_expensive(self):

        if len(self.products) == 0:

            print("No products available.")

            return

        expensive_product = self.products[0]

        for product in self.products:

            if product.price > expensive_product.price:

                expensive_product = product

        print("\n========== MOST EXPENSIVE PRODUCT ==========")

        expensive_product.display()

    # ========================================================
    # CHEAPEST PRODUCT
    # ========================================================

    def show_cheapest(self):

        if len(self.products) == 0:

            print("No products available.")

            return

        cheapest_product = self.products[0]

        for product in self.products:

            if product.price < cheapest_product.price:

                cheapest_product = product

        print("\n========== CHEAPEST PRODUCT ==========")

        cheapest_product.display()

    # ========================================================
    # ADMIN MENU
    # ========================================================

    def admin_menu(self):

        while True:

            print("""
============================================================
                       ADMIN MENU
============================================================

1. Add Product
2. Show Products
3. Search Product
4. Update Product
5. Remove Product
6. Show Customers
7. Show All Orders
8. Shop Statistics
9. Show Low Stock Products
10. Show Out of Stock Products
11. Show Most Expensive Product
12. Show Cheapest Product
13. Back to Main Menu

============================================================
""")

            choice = input(
                "Enter your choice: "
            )

            if choice == "1":

                self.add_product()

            elif choice == "2":

                self.show_products()

            elif choice == "3":

                self.search_product()

            elif choice == "4":

                self.update_product()

            elif choice == "5":

                self.remove_product()

            elif choice == "6":

                self.show_customers()

            elif choice == "7":

                self.show_all_orders()

            elif choice == "8":

                self.shop_statistics()

            elif choice == "9":

                self.show_low_stock()

            elif choice == "10":

                self.show_out_of_stock()

            elif choice == "11":

                self.show_most_expensive()

            elif choice == "12":

                self.show_cheapest()

            elif choice == "13":

                break

            else:

                print(
                    "Invalid choice. Please try again."
                )

    # ========================================================
    # CUSTOMER MENU
    # ========================================================

    def customer_menu(self):

        while True:

            print("""
============================================================
                     CUSTOMER MENU
============================================================

1. Register Customer
2. Show Customers
3. Add Product to Cart
4. View Cart
5. Update Cart
6. Remove Product from Cart
7. Checkout
8. View Order History
9. Back to Main Menu

============================================================
""")

            choice = input(
                "Enter your choice: "
            )

            if choice == "1":

                self.add_customer()

            elif choice == "2":

                self.show_customers()

            elif choice == "3":

                self.add_to_cart()

            elif choice == "4":

                self.view_cart()

            elif choice == "5":

                self.update_cart()

            elif choice == "6":

                self.remove_from_cart()

            elif choice == "7":

                self.checkout()

            elif choice == "8":

                self.show_customer_orders()

            elif choice == "9":

                break

            else:

                print(
                    "Invalid choice. Please try again."
                )


# ============================================================
# START SHOP
# ============================================================

def start_shop():

    shop = Shop()

    while True:

        print("""
################################################################
                 SHOPPING MANAGEMENT SYSTEM
################################################################

                    1. Admin Menu
                    2. Customer Menu
                    3. Show Products
                    4. Search Product
                    5. Exit

################################################################
""")

        choice = input(
            "Enter your choice: "
        )

        # ----------------------------------------------------
        # Admin
        # ----------------------------------------------------

        if choice == "1":

            shop.admin_menu()

        # ----------------------------------------------------
        # Customer
        # ----------------------------------------------------

        elif choice == "2":

            shop.customer_menu()

        # ----------------------------------------------------
        # Show products
        # ----------------------------------------------------

        elif choice == "3":

            shop.show_products()

        # ----------------------------------------------------
        # Search product
        # ----------------------------------------------------

        elif choice == "4":

            shop.search_product()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "5":

            print()
            print(
                "Thank you for using the Shopping System."
            )

            print(
                "Goodbye!"
            )

            break

        # ----------------------------------------------------
        # Invalid choice
        # ----------------------------------------------------

        else:

            print()
            print(
                "Invalid choice. Please enter a valid option."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    start_shop()