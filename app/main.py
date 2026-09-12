
class Item:
    def __init__(self, code, description, amount, available):
        self.code = code
        self.description = description
        self.amount = amount
        self.available = available


class Buyer:
    def __init__(self, code, fullname):
        self.code = code
        self.fullname = fullname
        self.basket = []


class Market:
    def __init__(self):
        self.catalog = []
        self.buyers = []
        self.next_item_code = 100
        self.next_buyer_code = 1

    def register_item(self):
        description = input("Enter item name: ")
        amount = float(input("Enter item price: "))
        available = int(input("Enter available stock: "))

        item = Item(
            self.next_item_code,
            description,
            amount,
            available
        )

        self.catalog.append(item)
        self.next_item_code += 1

        print("Item registered successfully.")

    def register_buyer(self):
        fullname = input("Enter buyer name: ")

        buyer = Buyer(
            self.next_buyer_code,
            fullname
        )

        self.buyers.append(buyer)
        self.next_buyer_code += 1

        print("Buyer registered successfully.")

    def locate_item(self, code):
        for item in self.catalog:
            if item.code == code:
                return item
        return None

    def locate_buyer(self, code):
        for buyer in self.buyers:
            if buyer.code == code:
                return buyer
        return None

    def show_catalog(self):
        if not self.catalog:
            print("There are no items in the catalog.")
            return

        print("\n--------- CATALOG ---------")

        for item in self.catalog:
            print(
                f"Code: {item.code}, "
                f"Name: {item.description}, "
                f"Price: ₹{item.amount}, "
                f"Available: {item.available}"
            )

    def put_in_basket(self):
        buyer_code = int(input("Enter buyer ID: "))
        item_code = int(input("Enter item code: "))
        requested = int(input("Enter quantity: "))

        buyer = self.locate_buyer(buyer_code)
        item = self.locate_item(item_code)

        if buyer is None or item is None:
            print("Invalid buyer or item.")
            return

        if requested <= 0:
            print("Quantity must be greater than zero.")
            return

        if requested > item.available:
            print("Requested quantity is unavailable.")
            return

        buyer.basket.append({
            "item": item,
            "count": requested
        })

        print("Item placed in basket.")

    def calculate_total(self, basket):
        total = 0

        for entry in basket:
            item = entry["item"]
            count = entry["count"]
            total += item.amount * count

        return total

    def apply_discount(self, total):
        if total >= 2000:
            return total * 0.90
        elif total >= 1000:
            return total * 0.95
        else:
            return total

    def finalize_purchase(self):
        buyer_code = int(input("Enter buyer ID: "))
        buyer = self.locate_buyer(buyer_code)

        if buyer is None:
            print("Buyer not found.")
            return

        if len(buyer.basket) == 0:
            print("Basket is empty.")
            return

        subtotal = self.calculate_total(buyer.basket)
        payable = self.apply_discount(subtotal)

        for entry in buyer.basket:
            entry["item"].available -= entry["count"]

        print("\n========= RECEIPT =========")
        print("Buyer:", buyer.fullname)
        print("Subtotal: ₹", subtotal)
        print("Final amount: ₹", payable)
        print("===========================")

        buyer.basket.clear()


def start_market():
    market = Market()

    actions = {
        "1": market.register_item,
        "2": market.register_buyer,
        "3": market.show_catalog,
        "4": market.put_in_basket,
        "5": market.finalize_purchase
    }

    while True:
        print("""
========== MARKET SYSTEM ==========

1. Register Item
2. Register Buyer
3. Show Catalog
4. Add Item to Basket
5. Finalize Purchase
6. Exit
""")

        choice = input("Choose an action: ")

        if choice == "6":
            print("Thank you for visiting!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    start_market()