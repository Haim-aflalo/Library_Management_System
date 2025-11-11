from book import Book
from user import User


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book):
        self.books[book]= book.__str__()

    def add_user(self, user):
        self.users[user] = user.__str__()

    def borrow_book(self,user,book):
        if user not in self.users:
            print("the user doesn't exist")
        if book not in self.books:
            print("the book doesn't exist")
        if not book.is_available:
            print("this book is already borrowed ")
        else:
            user.borrowed_books.append(book.isbn)
            book.is_available = False

    def return_book(self,user, book):
        if user not in self.users:
            print("the user doesn't exist")
        if book not in self.books:
            print("the book doesn't exist")
        if book.is_available:
            print("this book is already returned ")
        else:
            user.borrowed_book.remove(book)
            book.is_available = True

    def set_available_books(self):
        available_book = []
        for book in self.books:
            if book.is_available:
                available_book.append(book.isbn)
        return available_book

    def search_book(self,author):
        book_by_author = []
        for i in self.books:
            if i.author == author:
                book_by_author.append(i.__str__())
        return book_by_author

