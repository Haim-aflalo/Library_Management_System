class Library:
    def __init__(self, books: list, users: list):
        self.books = books
        self.users = users

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, user_id):
        self.users.append(user_id)