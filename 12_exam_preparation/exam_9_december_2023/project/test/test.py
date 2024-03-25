from collections import deque
from unittest import TestCase, main

from ex_01.railway_station import RailwayStation


class RailwayStationTest(TestCase):
    def setUp(self) -> None:
        self.railway = RailwayStation("Grand Central Terminal")

    def test_validate_initialisation(self):
        self.assertEqual("Grand Central Terminal", self.railway.name)
        self.assertEqual(deque(), self.railway.arrival_trains)
        self.assertEqual(deque(), self.railway.departure_trains)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.railway.name = "no"
        expected_result = "Name should be more than 3 symbols!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_new_arrival_on_board(self):
        train_info = 'NYC to Boston'
        self.railway.new_arrival_on_board(train_info)
        self.assertEqual(deque(['NYC to Boston']), self.railway.arrival_trains)

    def test_train_has_arrived_with_other_train_before_that(self):
        train_info = 'NYC to Buffalo'
        self.railway.arrival_trains = deque(['NYC to Boston'])
        result = self.railway.train_has_arrived(train_info)
        expected_result = f"There are other trains to arrive before {train_info}."
        self.assertEqual(result, expected_result)

    def test_train_has_arrived_with_same_train(self):
        train_info = 'NYC to Boston'
        self.railway.arrival_trains = deque(['NYC to Boston'])
        result = self.railway.train_has_arrived(train_info)
        expected_result = f"{train_info} is on the platform and will leave in 5 minutes."
        self.assertEqual(result, expected_result)
        self.assertEqual(deque(['NYC to Boston']), self.railway.departure_trains)
        self.assertEqual(deque(), self.railway.arrival_trains)

    def test_train_has_arrived_without_arrival_trains(self):
        train_info = 'NYC to Boston'
        with self.assertRaises(IndexError) as ie:
            self.railway.train_has_arrived(train_info)
        expected_result = "pop from an empty deque"
        self.assertEqual(expected_result, str(ie.exception))

    def test_train_has_left_without_departure_trains(self):
        train_info = 'NYC to Boston'
        result = self.railway.train_has_left(train_info)
        self.assertEqual(False, result)


    def test_train_has_left_with_same_train(self):
        train_info = 'NYC to Boston'
        self.railway.departure_trains = deque(['NYC to Boston'])
        result = self.railway.train_has_left(train_info)
        self.assertEqual(True, result)
        self.assertEqual(deque(), self.railway.departure_trains)

    def test_train_has_left_with_different_train(self):
        train_info = 'NYC to Buffalo'
        self.railway.departure_trains = deque(['NYC to Boston'])
        result = self.railway.train_has_left(train_info)
        self.assertEqual(False, result)

if __name__ == '__main__':
    main()