from unittest import TestCase, main

from ex_04_car_manager.car_manager import Car


class CarManagerTest(TestCase):

    def setUp(self):
        self.car = Car("Chevrolet", "Impala", 11.98,  90.9)

    def test_checking_init(self):

        self.assertEqual("Chevrolet", self.car.make)
        self.assertEqual("Impala", self.car.model)
        self.assertEqual(11.98, self.car.fuel_consumption)
        self.assertEqual(90.9, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_missing_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("", "Impala", 11.98,  90.9)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_missing_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Chevrolet", "", 11.98, 90.9)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_negative_or_zero_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Chevrolet", "Impala", 0, 90.9)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_negative_or_zero_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("Chevrolet", "Impala", 11.98, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_positive_amount_of_fuel(self):
        expected_result = 50
        self.car.refuel(50)

        self.assertEqual(expected_result, self.car.fuel_amount)

    def test_refuel_with_negative_amount_of_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_driving_certain_distance_with_enough_fuel_amount(self):
        self.car.fuel_amount = 20
        expected_result = 14.01

        self.car.drive(50)

        self.assertEqual(expected_result, self.car.fuel_amount)

    def test_driving_certain_distance_without_enough_fuel_amount_raises_exception(self):
        self.car.fuel_amount = 5.50

        with self.assertRaises(Exception) as ex:
            self.car.drive(50)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
