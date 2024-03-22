from unittest import TestCase, main

from ex_03_list.extended_list import IntegerList


class IntegerListTest(TestCase):
    def setUp(self):
        self.int_list = IntegerList(7, 8.5, 9, 2, 4, 3, "asd", 58, "50", False)

    def test_text_correct_initialization_and_get_data(self):
        self.assertEqual([7, 9, 2, 4, 3, 58], self.int_list.get_data())

    def test_adding_new_int_to_int_list(self):
        expected_result = [7, 9, 2, 4, 3, 58, 17]
        self.int_list.add(17)

        self.assertEqual(expected_result, self.int_list.get_data())

    def test_adding_new_element_to_int_list_and_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.add("-40")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_removing_index_from_int_list(self):
        expected_result = 7

        self.assertEqual(expected_result, self.int_list.remove_index(0))

    def test_removing_out_of_range_index_from_int_list_and_raise_exception(self):

        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(10)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_getting_index_from_int_list(self):
        expected_result = 9
        self.assertEqual(expected_result, self.int_list.get(1))

    def test_getting_out_of_range_index_from_int_list_and_raise_exception(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(9)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_inserting_int_at_certain_index(self):
        expected_result = [4, 7, 9, 2, 4, 3, 58]

        self.int_list.insert(0, 4)

        self.assertEqual(expected_result, self.int_list.get_data())

    def test_inserting_element_at_certain_index_and_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(0, "asd")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_inserting_element_at_certain_index_and_raise_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(9, 75)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_getting_biggest_int_in_int_list(self):
        expected_result = 58

        self.assertEqual(expected_result, self.int_list.get_biggest())

    def test_getting_index_based_on_an_element_in_int_list(self):
        expected_result = 0

        self.assertEqual(expected_result, self.int_list.get_index(7))


if __name__ == '__main__':
    main()
