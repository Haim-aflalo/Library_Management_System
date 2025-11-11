class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"Book:{self.title} by {self.author} number:{self.isbn}, is_available:{self.is_available}"
