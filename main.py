from classes.user import User
from classes.library import Library
from classes.book import Book


def start():
    library = Library()
    print(
        "1. add book \n 2. add user \n 3. borrow book\n 4.return book \n 5. list available books \n 6. search book \n 7. save and Exit")
    while True:
        choice = input("enter your choice..")
        if choice == "1":
            title = input("enter title")
            author = input("enter the author")
            isbn = input("enter the isbn")
            book = Book(title,author,isbn)
            library.add_book(book)
            continue
        if choice == "2":
            name = input("enter your name")
            id = input("enter your id ")
            new_user = User(name, id)
            library.add_user(new_user)
            continue
        if choice == "3":
            u = input("enter name user")
            id = input("enter your id ")
            book = input("enter the isbn of the book")
            b = None
            for i in library.books:
                if i.isbn == book:
                    b = i
            user = User(u,id)
            obj_b = Book(b.title,b.author,b.isbn)
            library.borrow_book(user, obj_b)
            continue
        if choice == "4":
            u = input("enter name user")
            id = input("enter your id ")
            book = input("enter the isbn of the book")
            b = None
            for i in library.books:
                if i.isbn == book:
                    b = i
            user = User(u, id)
            obj_b = Book(b.title, b.author, b.isbn)
            library.return_book(user,obj_b)
            continue

        if choice == "5":
            print( library.set_available_books())
            continue

        if choice == "6":
            author = input("enter name of author")
            library.search_book(author)

        elif choice == "7":
            break

        else:
            print("Invalid choice, try again.")

start()