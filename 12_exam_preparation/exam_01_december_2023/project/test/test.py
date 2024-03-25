from unittest import TestCase, main

from exam_01_december_2023.project.climbing_robot import ClimbingRobot


class ClimbingRobotTest(TestCase):

    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Arm", 100, 100)

    def test_valid_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Arm", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_with_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid"

        result = f"Category should be one of {self.robot.ALLOWED_CATEGORIES}"
        self.assertEqual(result, str(ve.exception))

    def test_get_used_capacity(self):
        self.robot.installed_software = [{"name": "Software", "capacity_consumption": 20, "memory_consumption": 20}]
        self.assertEqual(20, self.robot.get_used_capacity())

    def test_get_available_capacity(self):
        self.robot.installed_software = [{"capacity_consumption": 20}]
        self.assertEqual(80, self.robot.get_available_capacity())

    def test_get_used_memory(self):
        self.robot.installed_software = [{"name": "Software", "capacity_consumption": 20, "memory_consumption": 20}]
        self.assertEqual(20, self.robot.get_used_memory())

    def test_getting_available_memory(self):
        self.robot.installed_software = [{"memory_consumption": 20}]
        self.assertEqual(80, self.robot.get_available_memory())

    def test_successful_installation(self):
        software = {"name": "Software", "capacity_consumption": 20, "memory_consumption": 20}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' successfully installed on {self.robot.category} part."

        self.assertEqual([software], self.robot.installed_software)
        self.assertEqual(expected_result, result)

    def test_successful_installation_with_exact_memory_and_capacity(self):
        software = {"name": "Software", "capacity_consumption": 100, "memory_consumption": 100}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' successfully installed on {self.robot.category} part."

        self.assertEqual([software], self.robot.installed_software)
        self.assertEqual(expected_result, result)

    def test_failed_installation_capacity_condition(self):
        software = {"name": "Software1", "capacity_consumption": 110, "memory_consumption": 30}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."

        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(expected_result, result)

    def test_failed_installation_memory_condition(self):
        software = {"name": "Software", "capacity_consumption": 80, "memory_consumption": 120}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."

        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(expected_result, result)

    def test_failed_installation(self):
        software = {"name": "Software", "capacity_consumption": 110, "memory_consumption": 310}
        result = self.robot.install_software(software)
        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."

        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()