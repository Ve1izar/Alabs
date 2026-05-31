import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user import User, Reader

class TestUser(unittest.TestCase):
    def setUp(self):
        self.reader = Reader(1, "Андрій", "andriy@email.com")

    def test_initial_state(self):
        """Перевірка правильної ініціалізації читача"""
        self.assertEqual(self.reader.user_id, 1)
        self.assertEqual(self.reader.name, "Андрій")
        self.assertEqual(self.reader.email, "andriy@email.com")
        self.assertFalse(self.reader.has_debt)

    @patch('builtins.print')
    def test_update_notifies_reader(self, mock_print):
        """Перевірка, що метод update генерує правильне повідомлення"""
        self.reader.update("Clean Code")
        # Перевіряємо, чи був викликаний print з правильним аргументом
        mock_print.assert_called_once_with("[Reader UI] Андрій, у нас новинка! Доступна книга: 'Clean Code'")

if __name__ == '__main__':
    unittest.main()