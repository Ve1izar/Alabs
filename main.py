from library import Library
from book import Book
from user import Reader
from notifications import NotificationService


def main():
    print("=== Ініціалізація системи ===")
    lib = Library()

    # Створюємо користувачів та сервіси
    reader_andriy = Reader(1, "Андрій", "andriy@email.com")
    reader_olena = Reader(2, "Олена", "olena@email.com")
    email_alert = NotificationService()

    # Підписуємо їх як спостерігачів (Dependency Injection)
    lib.attach(reader_andriy)
    lib.attach(reader_olena)
    lib.attach(email_alert)
    print("Підписано: Андрій, Олена, NotificationService")

    print("\n=== Демонстрація роботи ===")
    book1 = Book("978-0134494166", "Clean Architecture - Robert Martin", 3)
    lib.add_book(book1)

    print("\n[Відписуємо Олену від сповіщень]")
    lib.detach(reader_olena)

    book2 = Book("978-0201633610", "Паттерни проєктування (GoF)", 5)
    lib.add_book(book2)


if __name__ == "__main__":
    main()