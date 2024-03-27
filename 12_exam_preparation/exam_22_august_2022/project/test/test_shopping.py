from unittest import TestCase

from project.shopping_cart import ShoppingCart


class ShoppingCartTest(TestCase):
    def test_valid_initialisation(self):
        shop = ShoppingCart("Lidl", 300)
        self.assertEqual("Lidl", shop.shop_name)
        self.assertEqual(300, shop.budget)
        self.assertEqual({}, shop.products)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("lidl5", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_unsuccessful_add_to_cart_product_equal_or_above_hundred(self):
        shop = ShoppingCart("Lidl", 300)
        with self.assertRaises(ValueError) as ve:
            shop.add_to_cart("ham", 100)

        self.assertEqual("Product ham cost too much!", str(ve.exception))

    def test_add_to_cart_with_valid_data(self):
        shop = ShoppingCart("Lidl", 300)
        shop.add_to_cart("ham", 70)

        self.assertEqual("Potatoes product was successfully added to the cart!", shop.add_to_cart("Potatoes", 25))
        self.assertEqual({"ham": 70, "Potatoes": 25}, shop.products)

    def test_removing_unexisting_product(self):
        shop = ShoppingCart("Lidl", 300)
        with self.assertRaises(ValueError) as ve:
            shop.remove_from_cart("tomato")

        self.assertEqual("No product with name tomato in the cart!", str(ve.exception))

    def test_remove_product(self):
        shop = ShoppingCart("Lidl", 300)
        shop.add_to_cart("ham", 25)
        shop.add_to_cart("cheese", 27)
        result = shop.remove_from_cart("ham")
        self.assertEqual(result, "Product ham was successfully removed from the cart!")
        self.assertEqual({"cheese": 27}, shop.products)

    def test_add_new_shopping_cart_instance(self):
        shop = ShoppingCart("Lidl", 300)
        shop.add_to_cart("product", 25)
        new_shop = ShoppingCart("Bill", 200)
        new_shop.add_to_cart('test', 22)
        merge = shop + new_shop
        self.assertEqual("LidlBill", merge.shop_name)
        self.assertEqual(500, merge.budget)
        self.assertEqual({"product": 25, 'test': 22}, merge.products)

    def test_successful_purchase(self):
        shop = ShoppingCart("Lidl", 300)
        shop.add_to_cart("test", 50)
        shop.add_to_cart("test2", 40)
        message = f'Products were successfully bought! Total cost: 90.00lv.'
        result = shop.buy_products()
        self.assertEqual(message, result)

    def test_unsuccessful_purchase(self):
        shop = ShoppingCart("Lidl", 100)
        shop.add_to_cart("test", 99)
        shop.add_to_cart("test2", 99)
        with self.assertRaises(ValueError) as ve:
            shop.buy_products()

        message = f"Not enough money to buy the products! Over budget with 98.00lv!"

        self.assertEqual(message, str(ve.exception))

