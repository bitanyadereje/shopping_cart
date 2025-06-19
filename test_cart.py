import unittest
from cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Pen", 10.0, 2)
        self.assertIn("Pen", self.cart.items)
        self.assertEqual(self.cart.items["Pen"]["quantity"], 2)

    def test_remove_item(self):
        self.cart.add_item("Book", 15.0, 1)
        self.cart.remove_item("Book")
        self.assertNotIn("Book", self.cart.items)

    def test_calculate_total(self):
        self.cart.add_item("Pen", 10.0, 2)
        self.cart.add_item("Notebook", 20.0, 1)
        total = self.cart.calculate_total()
        self.assertEqual(total, 40.0)

    def test_get_cart(self):
        self.cart.add_item("Pencil", 5.0, 3)
        cart_data = self.cart.get_cart()
        self.assertIn("Pencil", cart_data)
        self.assertEqual(cart_data["Pencil"]["quantity"], 3)
        self.assertEqual(cart_data["Pencil"]["price"], 5.0)

if __name__ == '__main__':
    unittest.main()
