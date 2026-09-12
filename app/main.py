
class Store:
    def __init__(self):
        self.products = {}
        self.customers = {}
        self.product_id = 1
        self.customer_id = 1

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter stock quantity: "))

        self.products[self.product_id] = {
            "name": name,
            "price": price,
            "stock": quantity
        }

        print("Product added successfully!")
        self.product_id += 1

    def add_customer(self):
        name = input("Enter customer name: ")

        self.customers[self.customer_id] = {
            "name": name,
            "cart": []
        }

        print("Customer added successfully!")
        self.customer_id += 1

    def show_products(self):
        if not self.products:
            print("No products available.")
            return

        print("\nID  Name  Price  Stock")

        for pid, product in self.products.items():
            print(
                pid,
                product["name"],
                product["price"],
                product["stock"]
            )

    def find_customer(self, cid):
        return self.customers.get(cid)

    def find_product(self, pid):
        return self.products.get(pid)

    def add_to_cart(self):
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
            print("Quantity must be positive.")
            return

        if quantity > product["stock"]:
            print("Not enough stock.")
            return

        customer["cart"].append({
            "product_id": pid,
            "quantity": quantity
        })

        print("Product added to cart!")

    def checkout(self):
        cid = int(input("Enter customer ID: "))
        customer = self.find_customer(cid)

        if customer is None:
            print("Customer not found.")
            return

        cart = customer["cart"]

        if len(cart) == 0:
            print("Your cart is empty.")
            return

        total = 0

        for item in cart:
            product = self.products[item["product_id"]]
            quantity = item["quantity"]
            total += product["price"] * quantity

        if total >= 2000:
            discount = 10
        elif total >= 1000:
            discount = 5
        else:
            discount = 0

        final_amount = total - (total * discount / 100)

        for item in cart:
            product = self.products[item["product_id"]]
            product["stock"] -= item["quantity"]

        print("\n----- BILL -----")
        print("Customer:", customer["name"])
        print("Subtotal:", total)
        print("Discount:", discount, "%")
        print("Final Amount:", final_amount)
        print("Thank you for shopping!")

        cart.clear()


def main():
    store = Store()

    while True:
        print("""
===== STORE MANAGEMENT SYSTEM =====

1. Add Product
2. Add Customer
3. Display Products
4. Add Product to Cart
5. Checkout
6. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            store.add_product()

        elif choice == "2":
            store.add_customer()

        elif choice == "3":
            store.show_products()

        elif choice == "4":
            store.add_to_cart()

        elif choice == "5":
            store.checkout()

        elif choice == "6":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()