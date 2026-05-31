from interfaces import Subject, Observer
from book import Book

class Library(Subject):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._observers = []
            cls._instance.books = []
            cls._instance.name = "Центральна Бібліотека"
        return cls._instance

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, book_title: str) -> None:
        for obs in self._observers:
            obs.update(book_title)

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"\n---> Системне повідомлення: Книгу '{book.title}' додано до каталогу.")
        self.notify(book.title)