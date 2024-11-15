# Библиотеки
import tkinter as tk
from tkinter import ttk

# Классы
from .add_new_partner import AddPartnerForm
from CONSTS import const

'''
-> Класс MainFrame используется как Главное окно, которе содержит в себе
    * карточки партнеров - self.partner_card_frame
    * кнопку добавления нового партнера - add_new_partner_btn
    
-> Класс генерирует Карточки товара, в соответствии с количеством записей в БД
'''

class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        # super().__init__(parent)
        tk.Frame.__init__(self, parent)
        # Инициализация Контроллера из родительского класса
        # Контроллер используется для перехода между окнами
        self.controller = controller

        # Инициализация класса БД
        self.db = controller.database

        # Получение списка всех партнеров
        # self.partners_dict_data_from_db = self.db.get_partners()
        # print("Partner:", self.partners_dict_data_from_db)

        # Создание вертикального фрейма для центрирования всего контента
        main_frame = ttk.Frame(self)

        # Размещение фрейма
        # Expand=True : Виджет занимает все пространство контейнера
        # fill = both : Виджет растягивается по вертикали и горизонтали
        main_frame.pack(expand=True, fill="both")

        # Заголовок "Главное окно"
        window_title_label = tk.Label(main_frame, text="Главное окно", font=const['label_font_title'])
        window_title_label.pack(pady=const['label_title_padY'])

        # Создание Canvas для хранения карточек партнеров
        self.canvas = tk.Canvas(main_frame)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Создание ползунка для прокрутки
        # self.canvas.yview : Вертикальная полоса прокрутки
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Привязка ползунка к Canvas
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Создание фрейма, который содержит данные карточки Партнера
        self.partner_card_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.partner_card_frame, anchor="nw")

        # Заполнение фрейма данными о партнере
        self.update_partner_display()

        # Обновляем область прокрутки
        self.partner_card_frame.bind("<Configure>", self.on_frame_configure)

        # Кнопка для добавления нового партнера
        add_new_partner_btn = ttk.Button(main_frame, text="Добавить партнера", command=self.add_partner)
        add_new_partner_btn.pack(pady=const['button_padY'])

    # Принудительная выгрузка всей информации о партнерах из БД
    def set_all_partners_data(self):
        ''' Вызов информации о партнерах для карточек '''
        # self.partners_dict_data_from_db = self.db.get_partners()
        # print(self.partners_dict_data_from_db)
        pass

            # Переход на окно добавления нового партнера
    def add_partner(self):
        ''' Открытие фрейма добавления нового партнера'''
        self.controller.show_frame(AddPartnerForm)

    def take_discount(self, partner_name: str):
        ''' Рассчет скидки '''
        # Получение суммы продаж партнера
        count: int = self.db.get_sum_sales(partner_name)[0]['count']
        if (count == None):
            return 0
        if (count > 300000):
            return 15
        elif (count > 50000):
            return 10
        elif (count > 10000):
            return 5
        return 5

    # Заполнение фрейма данными о партнере
    def update_partner_display(self):
        ''' Функция заполнения фрейма данными о партнерах '''
        # Очищаем текущие фреймы
        for widget in self.partner_card_frame.winfo_children():
            # Уничтожение того, что находится в Frame
            widget.destroy()

        print("FOR")
        # Отображение информации о каждом партнере
        for partner in self.db.get_partners():
            # Создание карточки Партнера
            partner_frame = ttk.Frame(self.partner_card_frame, padding=[8, 10], borderwidth=1, relief="solid")

            # Создание текстовых полей с информацией
            ttk.Label(partner_frame, text=f"{partner['type'].strip()} | {partner['name'].strip()}").pack(anchor="w")
            ttk.Label(partner_frame, text=f"{self.take_discount(partner['name'])}%").pack(anchor="e")
            ttk.Label(partner_frame, text=f"Директор: {partner['director'].strip()}").pack(anchor="w")
            ttk.Label(partner_frame, text=f"Тел.: +7 {partner['phone'].strip()}").pack(anchor="w")
            ttk.Label(partner_frame, text=f"Рейтинг: {str(partner['rate']).strip()}").pack(anchor="w")

            # Создание кнопки 'Подробнее'
            self.detail_btn = (ttk.Button(partner_frame, text="Подробнее",
                                          command=lambda p=partner: self.controller.open_partner_form(p["name"])).
                               pack(anchor="w",
                                    pady=const[
                                        'button_padY']))
            # Размещение карточки партнера в Canvas с карточками
            partner_frame.pack(fill="x", pady=5, padx=10)

    # Обновление размера Canvas для корректной работы ползунка ScrollBar
    def on_frame_configure(self, event=None):
        ''' Обновление размера Canvas для корректной прокрутки '''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
