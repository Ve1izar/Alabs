import unittest
from unittest.mock import Mock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library import Library  # noqa: E402
from book import Book  # noqa: E402
from interfaces import Observer  # noqa: E402


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.mock_observer1 = Mock(spec=Observer)
        self.mock_observer2 = Mock(spec=Observer)
        self.book = Book("111", "Паттерни проєктування", 5)

    def tearDown(self):
        """Скидаємо синглтон після кожного тесту"""
        Library._instance = None
        if hasattr(Library, '_observers'):
            Library._observers = []

    def test_singleton_instance(self):
        """Перевірка унікальності екземпляра Singleton"""
        lib2 = Library()
        self.assertIs(self.library, lib2)

    def test_attach_observer(self):
        """Перевірка підписки спостерігача"""
        self.library.attach(self.mock_observer1)
        self.assertIn(self.mock_observer1, self.library._observers)

    def test_detach_observer(self):
        """Перевірка відписки спостерігача"""
        self.library.attach(self.mock_observer1)
        self.library.detach(self.mock_observer1)
        self.assertNotIn(self.mock_observer1, self.library._observers)

    @patch('builtins.print')
    def test_add_book_notifies_observers(self, mock_print):
        """Перевірка, що додавання книги викликає update() у підписаних спостерігачів"""
        self.library.attach(self.mock_observer1)
        self.library.attach(self.mock_observer2)

        self.library.add_book(self.book)

        # Перевіряємо, чи додалась книга в список
        self.assertIn(self.book, self.library.books)

        # Перевіряємо, чи сповіщено обох спостерігачів (Mock)
        self.mock_observer1.update.assert_called_once_with("Паттерни проєктування")
        self.mock_observer2.update.assert_called_once_with("Паттерни проєктування")


if __name__ == '__main__':
    unittest.main()
