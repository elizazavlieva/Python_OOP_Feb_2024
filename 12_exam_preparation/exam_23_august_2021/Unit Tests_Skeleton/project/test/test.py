from project.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library("Lib")

    def test_init(self):
        self.assertEqual("Lib", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            library = Library("")
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book(self):
        self.library.add_book("Andrzej Sapkowski", "The Last Wish")
        result = {"Andrzej Sapkowski": ["The Last Wish"]}
        self.assertEqual(result, self.library.books_by_authors)

        self.library.add_book("Andrzej Sapkowski", "The Last Wish")
        result = {"Andrzej Sapkowski": ["The Last Wish"]}
        self.assertEqual(result, self.library.books_by_authors)

        self.library.add_book("Andrzej Sapkowski", "Blood of Elves")
        result = {"Andrzej Sapkowski": ["The Last Wish", "Blood of Elves"]}
        self.assertEqual(result, self.library.books_by_authors)

        self.library.add_book("Test", "Blood of Elves")
        result = {"Andrzej Sapkowski": ["The Last Wish", "Blood of Elves"], "Test": ["Blood of Elves"]}
        self.assertEqual(result, self.library.books_by_authors)

    def test_add_reader(self):
        self.library.add_reader("Ivan")
        self.assertEqual({"Ivan": []}, self.library.readers)

        self.library.add_reader("Asen")
        self.assertEqual({"Ivan": [], "Asen": []}, self.library.readers)

    def test_add_same_reader(self):
        self.library.add_reader("Ivan")
        message = f"Ivan is already registered in the Lib library."
        self.assertEqual(message, self.library.add_reader("Ivan"))

    def test_rent_book_invalid_reader(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Andrzej Sapkowski": ["The Last Wish", "Blood of Elves"]}

        result = self.library.rent_book("Boris", "Andrzej Sapkowski", "The Last Wish")
        message = "Boris is not registered in the Lib Library."

        self.assertEqual(result, message)

    def test_rent_invalid_author(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Andrzej Sapkowski": ["The Last Wish", "Blood of Elves"]}

        result = self.library.rent_book("Ivan", "Test", "The Last Wish")
        message = f"Lib Library does not have any Test's books."

        self.assertEqual(result, message)

    def test_rent_invalid_title(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Andrzej Sapkowski": ["Blood of Elves"]}

        result = self.library.rent_book("Ivan", "Andrzej Sapkowski", "The Last Wish")
        message = """Lib Library does not have Andrzej Sapkowski's "The Last Wish"."""

        self.assertEqual(result, message)
    def test_rent_book(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Andrzej Sapkowski": ["The Last Wish", "Blood of Elves"]}

        self.library.rent_book("Ivan", "Andrzej Sapkowski", "The Last Wish")
        library = {"Andrzej Sapkowski": ["Blood of Elves"]}
        readers = {"Ivan": [{"Andrzej Sapkowski": "The Last Wish"}]}
        self.assertEqual(readers, self.library.readers)
        self.assertEqual(library, self.library.books_by_authors)

        self.library.rent_book("Ivan", "Andrzej Sapkowski", "Blood of Elves")
        library = {"Andrzej Sapkowski": []}
        readers = {"Ivan": [{"Andrzej Sapkowski": "The Last Wish"}, {"Andrzej Sapkowski": "Blood of Elves"}]}
        self.assertEqual(readers, self.library.readers)
        self.assertEqual(library, self.library.books_by_authors)


if __name__ == "__main__":
    main()
