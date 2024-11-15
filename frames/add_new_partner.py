# Библиотеки
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Классы
from db.db import Database
from CONSTS import const

'''
-> Класс AddPartnerForm организует работу функционала по добавлению нового партнера
    Класс предоставляет возможность для занесения данных и отправки их на регистрацию
'''


class AddPartnerForm(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        # Инициализация контроллера
        self.controller = controller

        # Инициализация класса БД
        self.db = Database()

        # Контейнер для информации о партнёре
        container = ttk.Frame(self, padding=(20, 20))
        container.grid(row=0, column=0, sticky="nsew")

        # Заголовок
        title_label = ttk.Label(container, text="ДОБАВИТЬ ПАРТНЕРА", font=const['label_font_title'])
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Подсказка для ввода Наименования партнера (Хранится в container)
        ttk.Label(container, text="Наименование партнера:").grid(row=1, column=0, sticky="e", padx=5, pady=5)

        # Поле для ввода Наименования партнера (Хранится в container)
        self.name_entry = ttk.Entry(container, width=30)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Подсказка для ввода Адреса
        ttk.Label(container, text="Адрес:").grid(row=2, column=0, sticky="e", padx=5, pady=5)

        # Поле для ввода Адреса
        self.address_entry = ttk.Entry(container, width=30)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5)

        # Подсказка для ввода Телефона
        # Телефон в бд Хранится как 999 999 99 99 -> Телефон не должен иметь приставку
        ttk.Label(container, text="Телефон: +7").grid(row=3, column=0, sticky="e", padx=5, pady=5)

        # Поле для ввода Телефона
        self.phone_entry = ttk.Entry(container, width=30)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5)

        # Подсказка для ввода Почты
        ttk.Label(container, text="Почта:").grid(row=4, column=0, sticky="e", padx=5, pady=5)

        # Поле для ввода Почты
        self.email_entry = ttk.Entry(container, width=30)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5)

        # Подсказка для ввода ИНН
        ttk.Label(container, text="ИНН:").grid(row=5, column=0, sticky="e", padx=5, pady=5)

        # Поле для ввода ИНН
        self.inn_entry = ttk.Entry(container, width=30)
        self.inn_entry.grid(row=5, column=1, padx=5, pady=5)

        # Подсказка для ввода Рейтинга
        ttk.Label(container, text="Рейтинг (1 - 10):").grid(row=6, column=0, sticky="e", padx=5, pady=5)

        # Поле для ввода Рейтинга
        self.rate_entry = ttk.Entry(container, width=30)
        self.rate_entry.grid(row=6, column=1, padx=5, pady=5)

        # Подсказка для ввода Типа предприятия партнера (ЗАО ОАО ООО ПАО)
        ttk.Label(container, text="Тип:").grid(row=7, column=0, sticky="e", padx=5, pady=5)

        # Поле для ввода Типа предприятия партнера
        self.type_entry = ttk.Entry(container, width=30)
        self.type_entry.grid(row=7, column=1, padx=5, pady=5)

        # Подсказка для ввода Директора предприятия
        ttk.Label(container, text="Директор:").grid(row=8, column=0, sticky="e", padx=5, pady=5)

        # Поле для ввода Директора предприятия
        self.director_entry = ttk.Entry(container, width=30)
        self.director_entry.grid(row=8, column=1, padx=5, pady=5)

        # Поле для кнопки
        # Columnspan=n -> Растягивает объект на n колонок
        add_frame = ttk.Frame(container)
        add_frame.grid(row=9, column=0, columnspan=2, pady=(20, 0))

        # Кнопка "Добавить"
        # Выполняет команду -> self.add_new_partner
        ttk.Button(add_frame, text="Добавить", command=self.add_new_partner).pack(side="right", padx=5)

        # Поле для кнопки
        button_frame = ttk.Frame(container)
        button_frame.grid(row=10, column=0, columnspan=2, pady=(20, 0))

        # Кнопка "На Главную"
        # Выполняет команду -> controller.open_main_frame
        ttk.Button(button_frame, text="На Главную", command=controller.open_main_frame).pack(side="right", padx=5)

    # Очистка полей для ввода данных на нового партнера
    def clear_form_fields(self):
        ''' Очистка полей формы добавления нового партнера '''
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.director_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.inn_entry.delete(0, tk.END)

    # Добавление нового партнера
    def add_new_partner(self):
        ''' Проверка инфомрации и добавления патнера '''
        try:
            # Создание словаря с данными
            res = {
                'type': self.type_entry.get(),
                'name': self.name_entry.get(),
                'director': self.director_entry.get(),
                'mail': self.email_entry.get(),
                'ur_addr': self.address_entry.get(),
                'rate': self.rate_entry.get(),
                'inn': self.inn_entry.get(),
                'phone': self.phone_entry.get()
            }
            # Отправка данных на регистрацию
            if self.db.add_partner(res):
                # Регистрация успешна
                messagebox.showinfo("Информация", "Партнер успешно сохранен")
                return
            # Регистрация отклонена
            messagebox.showwarning("Внимание", "Неправильно заполнены данные")

        except:
            # Ошибка обработки данных
            messagebox.showerror("Ошибка", "Неправильно заполнены данные")
