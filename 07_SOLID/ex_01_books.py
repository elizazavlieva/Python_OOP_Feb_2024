
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book: Book):
        if book.title not in self.books:
            self.books.append(book)

    def find_book(self, title):
        return f"Result: {next((b.title for b in self.books if b.title.lower() == title.lower()), None)}"


# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page

