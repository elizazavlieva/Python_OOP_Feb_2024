from ex_01.robot import Robot
from unittest import TestCase, main


class RobotTest(TestCase):
    def setUp(self) -> None:
        self.robot1 = Robot("D2", "Education", 20, 20_000)

    def test_validate_initialisation(self):
        self.assertEqual("D2", self.robot1.robot_id)
        self.assertEqual("Education", self.robot1.category)
        self.assertEqual(20, self.robot1.available_capacity)
        self.assertEqual(20_000, self.robot1.price)
        self.assertEqual([], self.robot1.hardware_upgrades)
        self.assertEqual([], self.robot1.software_updates)

    def test_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot1 = Robot("D2", "Sport", 20, 20_000)

        expected_result = f"Category should be one of '{self.robot1.ALLOWED_CATEGORIES}'"
        self.assertEqual(expected_result, str(ve.exception))

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as ve:
            self.robot1 = Robot("D2", "Education", 20, -10)

        expected_result = "Price cannot be negative!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_failed_hardware_upgrade(self):
        self.robot1.hardware_upgrades = ["RAM"]
        result = self.robot1.upgrade("RAM", 500)
        expected_result = f"Robot {self.robot1.robot_id} was not upgraded."
        self.assertEqual(expected_result, result)

    def test_successful_hardware_upgrade(self):
        result = self.robot1.upgrade("RAM", 500.0)
        expected_result = f'Robot {self.robot1.robot_id} was upgraded with RAM.'
        self.assertEqual(expected_result, result)
        self.assertEqual(["RAM"], self.robot1.hardware_upgrades)
        self.assertEqual(20_750.0, self.robot1.price)

    def test_successful_software_upgrade(self):
        result = self.robot1.update(1.56, 10)
        expected_result = f'Robot {self.robot1.robot_id} was updated to version 1.56.'
        self.assertEqual(expected_result, result)
        self.assertEqual([1.56], self.robot1.software_updates)
        self.assertEqual(10, self.robot1.available_capacity)

    def test_failed_software_upgrade_based_on_capacity_deficit(self):
        result = self.robot1.update(1.56, 25)
        expected_result = f"Robot {self.robot1.robot_id} was not updated."
        self.assertEqual(result, expected_result)

    def test_failed_software_upgrade_based_on_older_software_version(self):
        self.robot1.software_updates = [1.56]
        result = self.robot1.update(1.26, 10)
        expected_result = f"Robot {self.robot1.robot_id} was not updated."
        self.assertEqual(expected_result, result)

    def test_comparing_prices_robot1_with_bigger_price(self):
        self.robot2 = Robot("Z3", "Education", 40, 8_000)
        result = self.robot1 > self.robot2
        expected_result = f'Robot with ID {self.robot1.robot_id} is more expensive ' \
                          f'than Robot with ID {self.robot2.robot_id}.'

        self.assertEqual(expected_result, result)

    def test_comparing_robots_with_same_price(self):
        self.robot2 = Robot("Z3", "Education", 40, 20_000)
        result = self.robot1 > self.robot2
        expected_result = f'Robot with ID {self.robot1.robot_id} costs equal to ' \
                          f'Robot with ID {self.robot2.robot_id}.'

        self.assertEqual(expected_result, result)

    def test_comparing_prices_robot2_with_bigger_price(self):
        self.robot2 = Robot("Z3", "Education", 40, 40_000)
        result = self.robot1 > self.robot2
        expected_result = f'Robot with ID {self.robot1.robot_id} is cheaper than ' \
                          f'Robot with ID {self.robot2.robot_id}.'

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()