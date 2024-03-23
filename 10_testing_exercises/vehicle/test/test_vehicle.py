from unittest import TestCase, main

from vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(55.5, 120.5)

    def test_validating_init(self):
        self.assertEqual(55.5, self.vehicle.fuel)
        self.assertEqual(55.5, self.vehicle.capacity)
        self.assertEqual(120.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive(self):
        expected_result = 30.5
        self.vehicle.drive(20)

        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_drive_and_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(70)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.fuel = 20
        expected_result = 50

        self.vehicle.refuel(30)
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_and_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_text(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected_result, str(self.vehicle))

if __name__ == '__main__':
    main()