from unittest import TestCase, main

from project.plantation import Plantation


class PlantationTest(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_invalid_size(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation = Plantation(-1)

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_valid_worker(self):
        result = self.plantation.hire_worker("Ivan")

        self.assertEqual("Ivan successfully hired.", result)
        self.assertEqual(["Ivan"], self.plantation.workers)

    def test_hire_same_worker_again(self):
        self.plantation.workers = ["Ivan", "Asen"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")

        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Ivan", "Asen"], self.plantation.workers)

    def test_len(self):
        self.plantation.plants["Ivan"] = ["Tulip", "Rose"]
        self.plantation.plants["Asen"] = ["Corn", "Pepper"]

        self.assertEqual(4, len(self.plantation))

    def test_planting_invalid(self):
        self.plantation.workers = ["Ivan", "Asen"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Petar", "Rose")

        self.assertEqual("Worker with name Petar is not hired!", str(ve.exception))

    def test_planting_if_plantation_is_full(self):
        self.plantation = Plantation(1)
        self.plantation.workers = ["Ivan"]
        self.plantation.planting("Ivan", "Rose")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "Tulip")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_successful_planting(self):
        self.plantation.workers = ["Ivan", "Asen"]

        first = self.plantation.planting("Ivan", "Rose")
        second = self.plantation.planting("Asen", "Corn")
        third = self.plantation.planting("Asen", "Pepper")

        self.assertEqual("Ivan planted it's first Rose.", first)
        self.assertEqual("Asen planted it's first Corn.", second)
        self.assertEqual("Asen planted Pepper.", third)
        self.assertEqual({"Ivan": ["Rose"], "Asen": ["Corn", "Pepper"]}, self.plantation.plants)

    def test_return_str_data(self):
        self.plantation.workers = ["Ivan", "Asen"]

        self.plantation.planting("Ivan", "Rose")
        self.plantation.planting("Asen", "Corn")
        self.plantation.planting("Asen", "Pepper")

        message = "Plantation size: 10\n" \
                  "Ivan, Asen\n" \
                  "Ivan planted: Rose\n" \
                  "Asen planted: Corn, Pepper"
        self.assertEqual(message, str(self.plantation))

    def test_return_repr(self):
        self.plantation.workers = ["Ivan", "Asen"]

        self.plantation.planting("Ivan", "Rose")
        self.plantation.planting("Asen", "Corn")
        self.plantation.planting("Asen", "Pepper")

        message = "Size: 10\nWorkers: Ivan, Asen"

        self.assertEqual(message, self.plantation.__repr__())


if __name__ == "__main__":
    main()
