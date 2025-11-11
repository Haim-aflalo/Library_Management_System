from classes.user import User
from classes.library import Library
from classes.book import Book




def start():
    l_a = Library()


    while True:

        print(
            "1. add book \n 2. add user \n 3. borrow book\n 4.return book \n 5. list available books \n 6. search book \n 7. save and Exit")
        choice = input("enter your choice..")
        if choice == "1":
            book_choice = input("enter name book")
            l_a.add_book(book_choice)

        elif choice == "2":
            name = input("enter your name")
            id = input("enter your id ")
            new_user = User(name, id)
            l_a.add_user(new_user)

        elif choice == "3":
            user = input("enter name user")
            book = input("enter name isbm the book")
            l_a.borrow_book(user, book)

        elif choice == "4":
            user = input("enter name user")
            book = input("enter name isbm the book")
            l_a.return_book(user, book)

        elif choice == "5":
            l_a.set_available_books()

        elif choice == "6":
            author = input("enter name of author")
            l_a.search_book(author)

        elif choice == "7":
            pass
            break
        else:
            print("Invalid choice, try again.")
print(start())