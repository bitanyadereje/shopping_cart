class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'item': Item(name, price), 'quantity': quantity}

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_cart(self):
        return {
            name: {
                'price': data['item'].price,
                'quantity': data['quantity']
            }
            for name, data in self.items.items()
        }

    def calculate_total(self):
        return sum(data['item'].price * data['quantity'] for data in self.items.values())
