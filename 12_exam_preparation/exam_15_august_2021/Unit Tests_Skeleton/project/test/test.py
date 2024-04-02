from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Happy paw")

    def test_init(self):
        self.assertEqual("Happy paw", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_invalid_food_qnty(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("Test", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("Test", -4)

            self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food(self):
        result = self.shop.add_food("Test", 100.5)

        self.assertEqual("Successfully added 100.50 grams of Test.", result)
        self.assertEqual({"Test": 100.5}, self.shop.food)

        result = self.shop.add_food("Test", 100.0)

        self.assertEqual("Successfully added 100.00 grams of Test.", result)
        self.assertEqual({"Test": 200.5}, self.shop.food)

    def test_add_pet(self):
        result = self.shop.add_pet("dog")
        self.assertEqual("Successfully added dog.", result)
        self.assertEqual(["dog"], self.shop.pets)

        result = self.shop.add_pet("cat")
        self.assertEqual("Successfully added cat.", result)
        self.assertEqual(["dog", "cat"], self.shop.pets)

    def test_add_same_pet_raises(self):
        self.shop.pets = ["dog", "cat"]

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("cat")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_invalid_pet(self):
        self.shop.pets = ["dog", "cat"]
        self.shop.food = {"Test": 200.0, "Test2": 500.0}

        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("Test", "Rabbit")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_with_invalid_food(self):
        self.shop.pets = ["dog", "cat"]
        self.shop.food = {"Test": 200.0, "Test2": 500.0}

        result = self.shop.feed_pet("Test4", "cat")
        self.assertEqual("You do not have Test4", result)

    def test_feed_with_not_enough_qnty(self):
        self.shop.pets = ["dog", "cat"]
        self.shop.food = {"Test": 90.0, "Test2": 500.0}
        result = self.shop.feed_pet("Test", "dog")

        self.assertEqual("Adding food...", result)
        self.assertEqual({"Test": 1090.0, "Test2": 500.0}, self.shop.food)

    def test_feed_pet(self):
        self.shop.pets = ["dog", "cat"]
        self.shop.food = {"Test": 200.0, "Test2": 500.0}
        result = self.shop.feed_pet("Test", "dog")

        self.assertEqual("dog was successfully fed", result)
        self.assertEqual({"Test": 100.0, "Test2": 500.0}, self.shop.food)

    def test_repr(self):
        self.shop.pets = ["dog", "cat"]
        result = 'Shop Happy paw:\nPets: dog, cat'
        self.assertEqual(result, repr(self.shop))


if __name__ == "__main__":
    main()
