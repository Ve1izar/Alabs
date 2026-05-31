import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        # Ініціалізація об'єкта перед кожним тестом
        self.book = Book("978-0134494166", "Clean Architecture", 3)

    def test_initial_state(self):
        """Перевірка початкового стану нової книги"""
        self.assertEqual(self.book.isbn, "978-0134494166")
        self.assertEqual(self.book.title, "Clean Architecture")
        self.assertEqual(self.book.available_copies, 3)

    def test_decrease_available_success(self):
        """Перевірка успішного зменшення кількості книг"""
        self.book.decrease_available()
        self.assertEqual(self.book.available_copies, 2)

    def test_decrease_available_zero(self):
        """Перевірка, що кількість не може бути меншою за 0"""
        self.book.available_copies = 0
        self.book.decrease_available()
        self.assertEqual(self.book.available_copies, 0)

    def test_increase_available(self):
        """Перевірка збільшення доступних копій (повернення книги)"""
        self.book.increase_available()
        self.assertEqual(self.book.available_copies, 4)

    def test_multiple_operations(self):
        """Перевірка серії операцій взяття та повернення"""
        self.book.decrease_available()
        self.book.decrease_available()
        self.book.increase_available()
        self.assertEqual(self.book.available_copies, 2)

if __name__ == '__main__':
    unittest.main()