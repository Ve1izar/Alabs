from interfaces import Observer

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

class Reader(User, Observer):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name, email)
        self.has_debt = False

    def update(self, book_title: str) -> None:
        print(f"[Reader UI] {self.name}, у нас новинка! Доступна книга: '{book_title}'")