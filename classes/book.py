class Book:

    def __init__(self,title,author,isbn,is_availabe=True):
        self.title = title
        self.author = author
        self.isbn = isbn 
        self.is_available = is_availabe

    def __str__(self):
        return f"Book: {self.title} by {self.author} number:{self.isbn}, is_availble:{self.is_available}"