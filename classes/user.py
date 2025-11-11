class User:

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def __str__(self):
        return f"user:{self.name}, id:{self.user_id}: {self.borrowed_books}"
