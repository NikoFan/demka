import tkinter as tk
from tkinter import messagebox


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("300x200")

        # Создаем фрейм для главного окна
        self.main_frame = MainFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Поле ввода
        self.entry = tk.Entry(self)
        self.entry.pack(pady=20)

        # Кнопка для перехода ко второму окну
        self.button = tk.Button(self, text="Go to Second Window", command=self.go_to_second_window)
        self.button.pack(pady=10)

    def go_to_second_window(self):
        # Получаем текст из поля ввода
        text = self.entry.get()
        if text:
            second_window = SecondWindow(self.master, text)
            self.pack_forget()  # Скрываем текущее окно
        else:
            messagebox.showwarning("Warning", "Please enter some text.")


class SecondWindow(tk.Toplevel):
    def __init__(self, master, text):
        super().__init__(master)
        self.title("Second Window")
        self.geometry("300x200")

        # Отображаем текст из первого окна
        label = tk.Label(self, text=f"You entered: {text}")
        label.pack(pady=20)

        # Кнопка для возврата к главному окну
        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.destroy()  # Закрываем текущее окно
        self.master.main_frame.pack(fill=tk.BOTH, expand=True)  # Показываем главное окно снова


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
