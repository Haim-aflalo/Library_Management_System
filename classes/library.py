from classes.book import Book
from classes.user import User


class Library:
    def __init__(self, books: list, users: list):
        self.books = books
        self.users = users

    def add_book(self, book):
        self.books.append(book.isbn)

    def add_user(self, user):
        self.users.append(user.name)

    @staticmethod
    def borrow_book(user, book):
        if book.is_available:
            user.borrowed_books.append(book.book_isbn)
            book.is_available = False
        else:
            print("the book is already borrowed")

    @staticmethod
    def return_book(user, book):
        if book.book_isbn in user.borrowed_books:
            book.is_available = True
            user.borrowed_books.remove(book.book_isbn)
        else:
            print("you didn't have this book")


    def set_available_books(self):
        available_book = []
        for i in self.books:
            if i.is_available:
                available_book.append(i.isbn)
        return available_book

    def search_book(self,author):
        book_by_author = []
        for i in self.books:
            if i == author:
                book_by_author.append(i)
        return book_by_author

