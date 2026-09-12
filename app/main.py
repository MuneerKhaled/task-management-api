
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int


@dataclass
class Customer:
    id: int
    name: str
    cart: list


class Store:
    def __init__(self):
        self.inventory = {}
        self.users = {}
        self.p_id = 1
        self.c_id = 1

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))

        self.inventory[self.p_id] = Product(
            self.p_id, name, price, stock
        )

        print("Product added with ID:", self.p_id)
        self.p_id += 1

    def add_customer(self):
        name = input("Enter customer name: ")

        self.users[self.c_id] = Customer(
            self.c_id, name, []
        )

        print("Customer added with ID:", self.c_id)
        self.c_id += 1

    def display_products(self):
        print("\n----- PRODUCT LIST -----")

        if not self.inventory:
            print("No products available.")
            return

        for product in self.inventory.values():
            print(
                f"{product.id}. {product.name} | "
                f"₹{product.price} | Stock: {product.stock}"
            )

    def add_to_cart(self):
        customer_id = int(input("Enter customer ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        customer = self.users.get(customer_id)
        product = self.inventory.get(product_id)

        if customer is None or product is None:
            print("Invalid customer or product.")
            return

        if quantity <= 0 or quantity > product.stock:
            print("Invalid quantity or insufficient stock.")
            return

        customer.cart.append((product_id, quantity))
        print("Added to cart.")

    def get_total(self, customer):
        total = 0

        for product_id, quantity in customer.cart:
            product = self.inventory[product_id]
            total += product.price * quantity

        return total

    def checkout(self):
        customer_id = int(input("Enter customer ID: "))
        customer = self.users.get(customer_id)

        if customer is None:
            print("Customer not found.")
            return

        if len(customer.cart) == 0:
            print("Cart is empty.")
            return

        total = self.get_total(customer)

        if total >= 2000:
            discount = 0.10
        elif total >= 1000:
            discount = 0.05
        else:
            discount = 0

        payable = total * (1 - discount)

        for product_id, quantity in customer.cart:
            self.inventory[product_id].stock -= quantity

        print("\n========= RECEIPT =========")
        print("Customer:", customer.name)
        print("Subtotal:", total)
        print("Discount:", discount * 100, "%")
        print("Amount payable:", payable)
        print("===========================")

        customer.cart.clear()


def main():
    store = Store()

    while True:
        print("""
========= STORE MENU =========

1. Add Product
2. Add Customer
3. Display Products
4. Add to Cart
5. Checkout
6. Exit
""")

        choice = input("Enter choice: ")

        if choice == "1":
            store.add_product()

        elif choice == "2":
            store.add_customer()

        elif choice == "3":
            store.display_products()

        elif choice == "4":
            store.add_to_cart()

        elif choice == "5":
            store.checkout()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()