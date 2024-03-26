from ex_01.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTest(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver('Ivan', 10.5)

    def test_valid_initialisation(self):
        self.assertEqual("Ivan", self.driver.name)
        self.assertEqual(10.5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_invalid_money(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = - 10

        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ve.exception))

    def test_add_already_existing_cargo_offer(self):
        self.driver.available_cargos = {"London": 25456}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("London", 25456)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer(self):
        result = self.driver.add_cargo_offer("London", 25456)
        expected_result = f"Cargo for 25456 to London was added as an offer."
        self.assertEqual(expected_result, result)
        self.assertEqual({"London": 25456}, self.driver.available_cargos)

    def test_best_cargo_offer(self):
        self.driver.available_cargos = {"London": 25456, "Paris": 20565}
        result = self.driver.drive_best_cargo_offer()
        expected_result = f"{self.driver.name} is driving 25456 to London."

        self.assertEqual(expected_result, result)
        self.assertEqual(241143.0, self.driver.earned_money)
        self.assertEqual(25456, self.driver.miles)

    def test_failed_cargo_offer(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_text_representation(self):
        self.driver.miles = 20
        result = str(self.driver)
        expected_result = "Ivan has 20 miles behind his back."
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()