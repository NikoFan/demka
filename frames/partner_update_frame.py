import tkinter as tk
from operator import index
from tkinter import ttk
from tkinter import messagebox

from db.db import Database
from frames.current_partner import Partner
from CONSTS import const


class UpdatePartnerForm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.db = Database()
        # Контейнер для информации о партнёре
        container = ttk.Frame(self, padding=(20, 20))
        container.grid(row=0, column=0, sticky="nsew")

        # Заголовок
        title_label = ttk.Label(container, text="ОБНОВЛЕНИЕ ИНФОРМАЦИИ", font=const['label_font_title'])
        title_label.grid(row=0, column=0, columnspan=3, pady=const['label_title_padY'])

        # Поле Наименования предприятия
        ttk.Label(container, text="Наименование партнера:").grid(row=1, column=0, sticky="e",
                                                                 padx=const['label_normal_padX'],
                                                                 pady=const['label_normal_padY'])
        self.name_entry = ttk.Entry(container, width=30)
        self.name_entry.grid(row=1, column=1, padx=const['entry_padX'], pady=const['entry_padY'],
                             ipadx=const['entry_ipadX'], ipady=const['entry_ipadY'])


        # Поле Юридический адрес предприятия
        ttk.Label(container, text="Адрес:").grid(row=2, column=0, sticky="e", padx=const['label_normal_padX'],
                                                 pady=const['label_normal_padY'])
        self.address_entry = ttk.Entry(container, width=30)
        self.address_entry.grid(row=2, column=1, padx=const['entry_padX'], pady=const['entry_padY'],
                                ipadx=const['entry_ipadX'], ipady=const['entry_ipadY'])


        # Поле Телефон предприятия
        ttk.Label(container, text="Телефон: +7").grid(row=3, column=0, sticky="e", padx=const['label_normal_padX'],
                                                      pady=const['label_normal_padY'])
        self.phone_entry = ttk.Entry(container, width=30)
        self.phone_entry.grid(row=3, column=1, padx=const['entry_padX'], pady=const['entry_padY'],
                              ipadx=const['entry_ipadX'], ipady=const['entry_ipadY'])


        # Поле Почта предприятия
        ttk.Label(container, text="Email:").grid(row=4, column=0, sticky="e", padx=const['label_normal_padX'],
                                                 pady=const['label_normal_padY'])
        self.email_entry = ttk.Entry(container, width=30)
        self.email_entry.grid(row=4, column=1, padx=const['entry_padX'], pady=const['entry_padY'],
                              ipadx=const['entry_ipadX'], ipady=const['entry_ipadY'])


        # Поле ИНН предприятия
        ttk.Label(container, text="ИНН:").grid(row=5, column=0, sticky="e", padx=const['label_normal_padX'],
                                               pady=const['label_normal_padY'])
        self.inn_entry = ttk.Entry(container, width=30)
        self.inn_entry.grid(row=5, column=1, padx=const['entry_padX'], pady=const['entry_padY'],
                            ipadx=const['entry_ipadX'], ipady=const['entry_ipadY'])


        # Поле Рейтинг предприятия
        ttk.Label(container, text="Рейтинг:").grid(row=6, column=0, sticky="e", padx=const['label_normal_padX'],
                                                   pady=const['label_normal_padY'])
        self.rate_entry = ttk.Entry(container, width=30)
        self.rate_entry.grid(row=6, column=1, padx=const['entry_padX'], pady=const['entry_padY'],
                             ipadx=const['entry_ipadX'], ipady=const['entry_ipadY'])

        # Поле Тип предприятия
        ttk.Label(container, text="Тип:").grid(row=7, column=0, sticky="e", padx=const['label_normal_padX'],
                                               pady=const['label_normal_padY'])
        self.type_entry = ttk.Entry(container, width=30)
        self.type_entry.grid(row=7, column=1, padx=const['entry_padX'], pady=const['entry_padY'],
                             ipadx=const['entry_ipadX'], ipady=const['entry_ipadY'])

        # Поле Директор
        ttk.Label(container, text="Директор:").grid(row=8, column=0, sticky="e", padx=const['label_normal_padX'],
                                                    pady=const['label_normal_padY'])
        self.director_entry = ttk.Entry(container, width=30)
        self.director_entry.grid(row=8, column=1, padx=const['entry_padX'], pady=const['entry_padY'],
                                 ipadx=const['entry_ipadX'], ipady=const['entry_ipadY'])

        # Кнопка "Сохранить"
        add_frame = ttk.Frame(container)
        add_frame.grid(row=9, column=0, columnspan=2, pady=(20, 0))

        ttk.Button(add_frame, text="Сохранить", command=self.update).pack(side="right", padx=5)


        button_frame = ttk.Frame(container)
        button_frame.grid(row=10, column=0, columnspan=2, pady=(20, 0))

        # Кнопка "Назад"
        ttk.Button(button_frame, text="Назад", command=lambda name=Partner.get_name():controller.open_partner_form(name)).pack(side="right", padx=5)

    def set_partner_update_data(self):
        self.partner_name = Partner.get_name()
        self.partner_list: dict = self.db.get_partner_by_name(self.partner_name)

        # Установка данных в поля для ввода
        self.name_entry.delete(0, 'end')
        self.name_entry.insert(tk.END, self.partner_list['name'].strip())

        self.address_entry.delete(0, 'end')
        self.address_entry.insert(tk.END, self.partner_list['ur_addr'].strip())

        self.phone_entry.delete(0, 'end')
        self.phone_entry.insert(tk.END, self.partner_list['phone'].strip())

        self.email_entry.delete(0, 'end')
        self.email_entry.insert(tk.END, self.partner_list['mail'].strip())

        self.inn_entry.delete(0, 'end')
        self.inn_entry.insert(tk.END, self.partner_list['inn'].strip())

        self.rate_entry.delete(0, 'end')
        self.rate_entry.insert(tk.END, self.partner_list['rate'])

        self.type_entry.delete(0, 'end')
        self.type_entry.insert(tk.END, self.partner_list['type'].strip())

        self.director_entry.delete(0, 'end')
        self.director_entry.insert(tk.END, self.partner_list['director'].strip())

    def take_partner_info(self):
        ''' Получение информации о партнере '''
        print(Partner.get_name())
        print(self.db.get_partner_by_name(Partner.get_name()))
        return self.db.get_partner_by_name(self.partner_name)

    def clear_form_fields(self):
        """Очищает все поля формы."""
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def update(self):
        try:
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
            if self.db.update_partners_data(res):
                # После измеения ИМЕНИ партнера, оно меняется и в БД ->
                # Следует поменять его и в статическом классе
                Partner.set_name(res["name"])

                messagebox.showinfo("Информация", "Партнер успешно Обновлен")
                return
            messagebox.showwarning("Внимание", "Неправильно заполнены данные")

        except:

            messagebox.showerror("Ошибка", "Неправильно заполнены данные")
