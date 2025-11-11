import json
import pandas as pd



class SaveData:

    def __init__(self,books,users):
        self.books = books
        self.users = users

    @staticmethod
    def convert_books_lst(books):
        books_lst = []
        for k,v in books.items():
            book = {k.title:v}
            books_lst.append(book)
        return books_lst

    @staticmethod
    def convert_users_lst(users):
        books_lst = []
        for k, v in users.items():
            book = {k.name: v}
            books_lst.append(book)
        return books_lst

    def save_to_json(self):
       with open ("../data/data.json", "a") as f:
        books = self.convert_books_lst(self.books)
        users = self.convert_users_lst(self.users)
        json.dump(books,f)
        json.dump(users,f)

    # @staticmethod
    # def json_to_csv():
    #     with open("../data/data.json", encoding='utf-8') as inputfile:
    #         df = pd.read_json(inputfile)
    #
    #     df.to_csv("data.csv", encoding='utf-8', index=False)


#
# from book import Book
# from library import Library
# from user import User
#
#
# b1 = Book("hello","david",1234)
# b2 = Book("hello_p","david_p",12345)
# u1= User("leo",456)
# u2= User("leo_p",4567)
# l = Library()
# l.add_book(b1)
# l.add_book(b2)
# l.add_user(u1)
# l.add_user(u2)
# l.borrow_book(u1,b1)
# s = SaveData(l.books,l.users)
# s.save_to_json()
# # s.json_to_csv()