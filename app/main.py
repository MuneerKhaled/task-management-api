class Item:
    def __init__(self, code, name, cost, stock):
        self.code = code
        self.name = name
        self.cost = cost
        self.stock = stock


class Buyer:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.cart = []


class Store:
    def __init__(self):
        self.items = []
        self.buyers = []
        self.next_item_code = 1
        self.next_buyer_number = 1

    def get_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def get_buyer(self, number):
        for buyer in self.buyers:
            if buyer.number == number:
                return buyer
        return None

    def add_product(self):
        name = input("Enter product name: ")
        cost = float(input("Enter product price: "))
        stock = int(input("Enter available quantity: "))

        new_item = Item(
            self.next_item_code,
            name,
            cost,
            stock
        )

        self.items.append(new_item)
        self.next_item_code += 1

        print("Product added successfully.")

    def register_buyer(self):
        name = input("Enter customer name: ")

        new_buyer = Buyer(
            self.next_buyer_number,
            name
        )

        self.buyers.append(new_buyer)
        self.next_buyer_number += 1

        print("Customer registered successfully.")

    def display_inventory(self):
        if not self.items:
            print("No products available.")
            return

        print("\n========== INVENTORY ==========")

        for item in self.items:
            print(
                f"Code: {item.code} | "
                f"Name: {item.name} | "
                f"Price: ₹{item.cost} | "
                f"Available: {item.stock}"
            )

    def purchase_item(self):
        buyer_number = int(input("Enter customer ID: "))
        item_code = int(input("Enter product ID: "))
        amount = int(input("Enter quantity: "))

        buyer = self.get_buyer(buyer_number)
        item = self.get_item(item_code)

        if buyer is None:
            print("Customer not found.")
            return

        if item is None:
            print("Product not found.")
            return

        if amount <= 0:
            print("Quantity must be greater than zero.")
            return

        if amount > item.stock:
            print("Not enough stock available.")
            return

        buyer.cart.append({
            "item": item,
            "amount": amount
        })

        print("Product added to cart.")

    def get_total(self, buyer):
        total = 0

        for entry in buyer.cart:
            item = entry["item"]
            amount = entry["amount"]

            total += item.cost * amount

        return total

    def generate_bill(self):
        buyer_number = int(input("Enter customer ID: "))
        buyer = self.get_buyer(buyer_number)

        if buyer is None:
            print("Customer not found.")
            return

        if len(buyer.cart) == 0:
            print("Shopping cart is empty.")
            return

        total = self.get_total(buyer)

        if total >= 2000:
            discount_rate = 10
        elif total >= 1000:
            discount_rate = 5
        else:
            discount_rate = 0

        savings = total * discount_rate / 100
        final_price = total - savings

        for entry in buyer.cart:
            item = entry["item"]
            amount = entry["amount"]

            item.stock -= amount

        print("\n========== CUSTOMER BILL ==========")
        print("Customer Name:", buyer.name)
        print("Original Total: ₹", total)
        print("Discount Rate:", discount_rate, "%")
        print("Discount Amount: ₹", savings)
        print("Amount to Pay: ₹", final_price)
        print("===================================")

        buyer.cart.clear()


def run_store():
    store = Store()

    while True:
        print("""
========== SHOPPING MENU ==========

1. Add Product
2. Register Customer
3. Display Inventory
4. Purchase Product
5. Generate Bill
6. Close Program
""")

        option = input("Choose an option: ")

        if option == "1":
            store.add_product()

        elif option == "2":
            store.register_buyer()

        elif option == "3":
            store.display_inventory()

        elif option == "4":
            store.purchase_item()

        elif option == "5":
            store.generate_bill()

        elif option == "6":
            print("Thank you for using the shopping system.")
            break

        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    run_store()