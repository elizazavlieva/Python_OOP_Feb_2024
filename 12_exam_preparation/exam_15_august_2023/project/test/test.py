from unittest import TestCase, main

from ex_01.trip import Trip


class TripTest(TestCase):
    def setUp(self) -> None:
        self.trip = Trip(2000.0, 2, True)

    def test_validate_initialisation(self):
        self.assertEqual(2000.0, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_below_one_travelers_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        expected_result = "At least one traveler is required!"

        self.assertEqual(expected_result, str(ve.exception))

    def test_is_family_below_two_travelers(self):
        self.trip = Trip(1000.0, 1, True)
        self.assertEqual(False, self.trip.is_family)

    def test_book_a_trip_not_in_destination_dict(self):
        expected_result = 'This destination is not in our offers, please choose a new one!'
        result = self.trip.book_a_trip("USA")

        self.assertEqual(expected_result, result)

    def test_book_a_trip_when_travelers_is_family(self):
        trip_price = (500 * 2) * 0.9
        destination = {"Bulgaria": trip_price}
        budget = 2000.0 - trip_price
        expected_result = f'Successfully booked destination Bulgaria! Your budget left is {budget:.2f}'

        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual(destination, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(budget, self.trip.budget)
        self.assertEqual(result, expected_result)

    def test_book_a_trip_when_travelers_not_family(self):
        self.trip.is_family = False
        trip_price = 500 * 2
        destination = {"Bulgaria": trip_price}
        budget = 2000.0 - trip_price
        expected_result = f'Successfully booked destination Bulgaria! Your budget left is {budget:.2f}'

        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual(destination, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(budget, self.trip.budget)
        self.assertEqual(result, expected_result)

    def test_book_a_trip_when_not_enough_budget(self):
        result = self.trip.book_a_trip('New Zealand')
        expected_result = 'Your budget is not enough!'

        self.assertEqual(result, expected_result)

    def test_booking_status_without_booked_destination(self):
        expected_result = f'No bookings yet. Budget: {self.trip.budget:.2f}'
        result = self.trip.booking_status()

        self.assertEqual(expected_result, result)

    def test_booking_status_with_booked_destination(self):
        self.trip.budget = 35_600.00
        self.trip.booked_destinations_paid_amounts = {"New Zealand": 13_500, "Bulgaria": 900}
        trip = sorted({"New Zealand": 13_500, "Bulgaria": 900}.items())
        expected_result = []
        for dest, price in trip:
            expected_result.append(f"Booked Destination: {dest}")
            expected_result.append(f"Paid Amount: {price:.2f}")
        expected_result.extend([f"Number of Travelers: 2", f"Budget Left: 35600.00"])
        expected_result = "\n".join(expected_result)

        result = self.trip.booking_status()
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    main()

