from typing import List,Dict
from library.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}
        self.rented_books: Dict[str: Dict[str: int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available.keys() and book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}

            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for users, rent in self.rented_books.items():
            if book_name in rent.keys():
                return f'The book "{book_name}" is already rented and will be available in ' \
                       f'{self.rented_books[users][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)

        return f"{user.username} doesn't have this book in his/her records!"
