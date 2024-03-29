from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Green Idea", 10)

    def test_valid_initialisation(self):
        self.assertEqual("Green Idea", self.factory.name)
        self.assertEqual(10, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_can_add(self):
        self.factory.add_ingredient("white", 3)
        self.factory.add_ingredient("white", 2)
        result = self.factory.can_add(4)
        self.assertTrue(result)

    def test_cannot_add(self):
        self.factory.add_ingredient("white", 7)
        self.factory.add_ingredient("white", 3)
        result = self.factory.can_add(4)
        self.assertFalse(result)

    def test_adding_successfully_ingredient(self):
        self.factory.add_ingredient("white", 3)
        self.factory.add_ingredient("white", 2)
        self.assertEqual({"white": 5}, self.factory.ingredients)

    def test_add_unknown_ingredient(self):
        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient("black", 4)

        message = f"Ingredient of type black not allowed in PaintFactory"
        self.assertEqual(message, str(te.exception))

    def test_add_ingredient_full_capacity_raises(self):
        self.factory = PaintFactory("Green Idea", 3)
        self.factory.add_ingredient("blue", 3)

        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient("green", 4)

        message = "Not enough space in factory"
        self.assertEqual(message, str(ve.exception))

    def test_removing_successfully_ingredient(self):
        self.factory.add_ingredient("blue", 5)
        self.factory.remove_ingredient("blue", 4)
        self.assertEqual({"blue": 1}, self.factory.ingredients)


    def test_removing_more_ingredients_than_existing_raises(self):
        self.factory.add_ingredient("blue", 5)
        self.factory.add_ingredient("red", 5)

        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient("red", 7)

        message = "Ingredients quantity cannot be less than zero"
        self.assertEqual(message, str(ve.exception))

    def test_removing_unknown_ingredient(self):
        self.factory.add_ingredient("blue", 5)
        self.factory.add_ingredient("red", 5)

        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("silver", 7)

        message = "No such ingredient in the factory"
        self.assertEqual(message, str(ke.exception))

    def test_product(self):
        self.factory.add_ingredient("blue", 4)
        self.factory.add_ingredient("red", 5)

        result = self.factory.products
        self.assertEqual({"blue": 4, "red": 5}, result)

    def test_get_string_repr(self):
        self.factory.add_ingredient("blue", 5)
        self.factory.add_ingredient("red", 5)
        message = f"Factory name: Green Idea with capacity 10.\n" \
                  f"blue: 5\n" \
                  f"red: 5\n"

        self.assertEqual(message, self.factory.__repr__())

if __name__ == "__main__":
    main()
