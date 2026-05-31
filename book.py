class Book:
    def __init__(self, isbn: str, title: str, available_copies: int = 1):
        self.isbn = isbn
        self.title = title
        self.available_copies = available_copies

    def decrease_available(self) -> None:
        if self.available_copies > 0:
            self.available_copies -= 1

    def increase_available(self) -> None:
        self.available_copies += 1