class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, name, price):
        self.items.append((name, price))
        self.total += price

    def show_total(self):
        print("Items in cart:")
        for item, price in self.items:
            print(f"{item} - Rs.{price}")
        print("Total cost:", self.total)

cart = ShoppingCart()
cart.add_item("Apple", 200)
cart.add_item("Milk", 60)
cart.add_item("Bread", 30)

cart.show_total()