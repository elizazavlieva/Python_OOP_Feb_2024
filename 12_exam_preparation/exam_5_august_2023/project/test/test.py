from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class SecondHandCarTest(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Astra", "Family car", 120_000, 10_000)

    def test_validate_initialisation(self):
        self.assertEqual("Astra", self.car.model)
        self.assertEqual("Family car", self.car.car_type)
        self.assertEqual(120_000, self.car.mileage)
        self.assertEqual(10_000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_below_one(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5
        expected_result = 'Price should be greater than 1.0!'
        self.assertEqual(expected_result, str(ve.exception))

    def test_mileage_below_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        expected_result = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected_result, str(ve.exception))

    def test_successfully_set_promotional_price(self):
        result = self.car.set_promotional_price(5_000)
        expected_result = 'The promotional price has been successfully set.'
        self.assertEqual(5_000, self.car.price)
        self.assertEqual(expected_result, result)

    def test_set_promotional_price_equal_to_regular_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(10_000)
        expected_result = 'You are supposed to decrease the price!'
        self.assertEqual(expected_result, str(ve.exception))

    def test_set_promotional_price_above_regular_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(15_000)
        expected_result = 'You are supposed to decrease the price!'
        self.assertEqual(expected_result, str(ve.exception))

    def test_unsuccessful_repair(self):
        expected_result = 'Repair is impossible!'
        result = self.car.need_repair(6_000, "new paint")
        self.assertEqual(expected_result, result)

    def test_successful_repair(self):
        expected_result = 'Price has been increased due to repair charges.'
        result = self.car.need_repair(1_000, "new tires")

        self.assertEqual(expected_result, result)
        self.assertEqual(11_000, self.car.price)
        self.assertEqual(["new tires"], self.car.repairs)

    def test_comparing_two_cars_with_same_type(self):
        self.other = SecondHandCar("Clio", "Family car", 130_000, 7_000)
        result = self.car > self.other
        self.assertEqual(True, result)

    def test_comparing_two_cars_with_different_type(self):
        self.other = SecondHandCar("Agora", "Bus", 130_000, 7_000)
        result = self.car > self.other
        expected_result = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(expected_result, result)

    def test_get_string_representation_of_the_object(self):
        result = str(self.car)
        expected_result = f"Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km\n" \
                          f"Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    main()