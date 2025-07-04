# cart.py

# --- Custom Exceptions ---
class ItemNotFoundError(Exception):
    """Raised when the item is not found in the cart."""
    pass

class InvalidItemError(Exception):
    """Raised when the item input is invalid."""
    pass

# --- Item Class ---
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# --- ShoppingCart Class ---
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        if not name or price <= 0 or quantity <= 0:
            raise InvalidItemError("Item must have valid name, positive price, and quantity.")

        if name in self.items:
            self.items[name]['quantity'] += quantity
            self.items[name]['item'].price = price  # Update price
        else:
            self.items[name] = {
                'item': Item(name, price),
                'quantity': quantity
            }

    def remove_item(self, name):
        if name not in self.items:
            raise ItemNotFoundError(f"Item '{name}' not found in cart.")
        del self.items[name]

    def update_item(self, name, price=None, quantity=None):
        if name not in self.items:
            raise ItemNotFoundError(f"Item '{name}' not found in cart.")

        if price is not None:
            if price <= 0:
                raise InvalidItemError("Price must be positive.")
            self.items[name]['item'].price = price

        if quantity is not None:
            if quantity <= 0:
                raise InvalidItemError("Quantity must be positive.")
            self.items[name]['quantity'] = quantity

    def calculate_total(self):
        return sum(data['item'].price * data['quantity'] for data in self.items.values())

    def get_cart(self):
        return {
            name: {
                'price': data['item'].price,
                'quantity': data['quantity']
            } for name, data in self.items.items()
        }
