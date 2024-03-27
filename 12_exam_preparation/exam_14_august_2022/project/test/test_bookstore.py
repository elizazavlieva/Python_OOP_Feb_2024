from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTest(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(10)

    def test_valid_initialisation(self):
        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_invalid_book_limit(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore = Bookstore(0)

        message = f"Books limit of 0 is not valid"
        self.assertEqual(message, str(ve.exception))

    def test_total_num_of_books(self):
        self.bookstore.availability_in_store_by_book_titles = {"Hamlet": 4, "Beloved": 4}
        result = len(self.bookstore)
        self.assertEqual(result, 8)

    def test_receive_book_and_not_enough_space(self):
        self.bookstore.availability_in_store_by_book_titles = {"Hamlet": 10}

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Beloved", 4)

        message = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(message, str(ex.exception))

    def test_receive_book_with_different_title(self):
        self.bookstore.availability_in_store_by_book_titles = {"Hamlet": 5}
        result = self.bookstore.receive_book("Beloved", 4)
        message = f"4 copies of Beloved are available in the bookstore."
        self.assertEqual(message, result)
        self.assertEqual({"Hamlet": 5, "Beloved": 4}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_with_same_title(self):
        self.bookstore.availability_in_store_by_book_titles = {"Hamlet": 5}
        result = self.bookstore.receive_book("Hamlet", 4)
        message = f"9 copies of Hamlet are available in the bookstore."
        self.assertEqual(message, result)
        self.assertEqual({"Hamlet": 9}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_non_existing_book(self):
        self.bookstore.availability_in_store_by_book_titles = {"Hamlet": 5}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Beloved", 3)
        message = f"Book Beloved doesn't exist!"
        self.assertEqual(message, str(ex.exception))

    def test_sell_book_without_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"Hamlet": 5}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Hamlet", 6)
        message = "Hamlet has not enough copies to sell. Left: 5"
        self.assertEqual(message, str(ex.exception))

    def test_sell_book(self):
        self.bookstore.availability_in_store_by_book_titles = {"Hamlet": 5}
        result = self.bookstore.sell_book("Hamlet", 5)
        message = "Sold 5 copies of Hamlet"
        self.assertEqual(message, result)
        self.assertEqual(5, self.bookstore.total_sold_books)
        self.assertEqual(0, self.bookstore.availability_in_store_by_book_titles["Hamlet"])

    def test_object_string_representation(self):
        self.bookstore.availability_in_store_by_book_titles = {"Hamlet": 5}
        self.bookstore.sell_book("Hamlet", 2)

        result = "Total sold books: 2\n" \
                 "Current availability: 3\n" \
                 " - Hamlet: 3 copies"
        self.assertEqual(result, str(self.bookstore))


if __name__ == "__main__":
    main()
