import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from textwrap import wrap


from CONSTS import const

from frames.current_partner import Partner
from frames.partner_update_frame import UpdatePartnerForm
from db.db import Database


class PartnerForm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Placeholder for partner ID label
        self.partner_label = ttk.Label(self, font=const['label_font_title'])
        self.partner_label.grid(row=0, column=0, padx=const['label_normal_padY'],
                                pady=const['label_normal_padX'])

        # Define partner information fields
        self.partner_fields = [
            ("Тип партнера", ""),
            ("Наименование", ""),
            ("Директор", ""),
            ("Почта", ""),
            ("Телефон", ""),
            ("Юрид-й адрес", ""),
            ("ИНН", ""),
            ("Рейтинг", "")
        ]

        # Отображение полей партнера
        for i, (label_text, default_value) in enumerate(self.partner_fields, start=1):
            self.create_partner_info_label(label_text, default_value, i)

        # Buttons
        ttk.Button(self, text="Редактировать информацию",
                   command=lambda: controller.open_partner_update_form(Partner.get_name())
                   ).grid(row=9, column=0, padx=const['button_padX'], pady=const['button_padY'], sticky="w")

        ttk.Button(self, text="История партнера",
                   command=lambda: controller.open_history_frame()).grid(row=10, column=0, padx=const['button_padX'],
                                                                         pady=const['button_padY'], sticky="w")

        ttk.Button(self, text="На главную",
                   command=controller.open_main_frame).grid(row=11, column=0, padx=const['button_padX'],
                                                            pady=const['button_padY'], sticky="w")
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=10)
        self.rowconfigure(11, weight=70)

    # Вывод партнерской инфорации
    def set_partner_data(self):
        ''' Вывод информации о партнере '''
        self.partner_name = Partner.get_name()
        self.partner_label.config(text=f"Партнер {self.partner_name}")

        # Assuming get_partner_by_id fetches partner details
        partner_info = self.controller.database.get_partner_by_name(self.partner_name)
        print('Database call')
        print(partner_info)
        if partner_info:
            # Update displayed information with retrieved partner details
            fields = [
                ("Тип партнера", partner_info.get("type", "N/A").strip()),
                ("Наименование", partner_info.get("name", "N/A").strip()),
                ("Директор", partner_info.get("director", "N/A").strip()),
                ("Почта", partner_info.get("mail", "N/A").strip()),
                ("Телефон", partner_info.get("phone", "N/A").strip()),
                ("Юрид-й адрес", '\n'.join(wrap(partner_info.get("ur_addr", "N/A").strip(), int(100 / 2)))),
                ("ИНН", partner_info.get("inn", "N/A").strip()),
                ("Рейтинг", partner_info.get("rate", "N/A"))
            ]
            for i, (_, info_text) in enumerate(fields, start=1):
                self.create_partner_info_label(_, info_text, i)

    # Создание текстового поля с партнерской информацией
    def create_partner_info_label(self, info_name: str, info_text: str, text_row: int):
        ''' Создание текстового поля с информацией о партнере '''
        (ttk.Label(self, text=f"{info_name}: {info_text}", relief="solid", background="#f4e8d3",
                  font=const['label_font_normal'])

         .grid(row=text_row, column=0, sticky="we", padx=const['label_normal_padX'],
                                              pady=const['label_normal_padY'], ipadx=const['label_ipadX'],
                                              ipady=const['label_ipadY']))
