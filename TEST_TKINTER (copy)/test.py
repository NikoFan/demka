import unittest
import tkinter as tk
from unittest.mock import patch
from main2 import MyApp  # Предположим, что ваше приложение называется my_app.py


class TestMyApp(unittest.TestCase):
    def setUp(self):
        """Создаем приложение перед каждым тестом."""
        self.root = tk.Tk()
        self.app = MyApp(self.root)
        self.root.update()  # Обновляем интерфейс

    def tearDown(self):
        """Закрываем приложение после каждого теста."""
        self.root.destroy()

    def test_entry_text(self):
        """Проверяем, что текст правильно вводится в поле."""
        self.app.entry.insert(0, "Hello, World!")  # Вводим текст
        self.assertEqual(self.app.entry.get(), "Hello, World!")  # Проверяем текст

    def test_submit_button(self):
        """Проверяем работу кнопки Submit."""
        self.app.entry.insert(0, "Test")

        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.app.submit()  # Нажимаем кнопку Submit
            mock_showinfo.assert_called_with("Info", "You entered: Test")  # Проверяем вызов

    def test_empty_entry_warning(self):
        """Проверяем предупреждение при пустом вводе."""
        with patch('tkinter.messagebox.showwarning') as mock_showwarning:
            self.app.submit()  # Пытаемся отправить пустое поле
            mock_showwarning.assert_called_with("Warning", "Entry cannot be empty!")  # Проверяем вызов



if __name__ == "__main__":
    unittest.main()
