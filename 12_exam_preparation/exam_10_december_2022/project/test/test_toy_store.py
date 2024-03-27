from ex_01.toy_store import ToyStore
from  unittest import TestCase, main

class ToyStoreTest(TestCase):

    def setUp(self) -> None:
        self.toys = ToyStore()

    def test_valid_initialisation(self):
        result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(result, self.toys.toy_shelf)

    def test_adding_toy_on_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toys.add_toy("Z", "Bear")

        result = "Shelf doesn't exist!"
        self.assertEqual(result, str(ex.exception))

    def test_adding_existing_toy_raises_exception(self):
        self.toys.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.toys.add_toy("A", "Bear")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_adding_toy_on_occupied_shelf(self):
        self.toys.toy_shelf["A"] = "Bear"
        with self.assertRaises(Exception) as ex:
            self.toys.add_toy("A", "Doll")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_adding_toy_on_the_shelf(self):
        result = self.toys.add_toy("A", "Doll")

        self.assertEqual(f"Toy:Doll placed successfully!", result)
        self.assertEqual("Doll", self.toys.toy_shelf["A"])

    def test_removing_toy_from_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toys.remove_toy("Z", "Bear")

        result = "Shelf doesn't exist!"
        self.assertEqual(result, str(ex.exception))

    def test_removing_different_toy(self):
        self.toys.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.toys.remove_toy("A", "Doll")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_removing_toy(self):
        self.toys.toy_shelf["A"] = "Doll"
        result = self.toys.remove_toy("A", "Doll")

        self.assertEqual(f"Remove toy:Doll successfully!", result)
        self.assertEqual(None, self.toys.toy_shelf["A"])


if __name__ == "__main__":
    main()