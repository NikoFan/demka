# Библиотеки
from tkinter import *

# Классы
from db.db import Database
from frames.add_new_partner import AddPartnerForm
from frames.main_frame import MainFrame
from frames.partner_form import PartnerForm
from frames.historyframe import HistoryFrame
from frames.current_partner import Partner
from frames.partner_update_frame import UpdatePartnerForm

'''
-> Класс MainWindow выступает в роли маршрутизатора,
    задача которого переносить пользователя между окнами.
-> По кнопке перехода происходит обращение к выбранному фрейму,
    после чего начинается процесс открытия фрейма и
    загрузки в него всей требуемой информации из БД
'''

class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        ''' Создание формы главного окна '''
        # Название окна
        self.title("Мастре пол")

        # Инициализация класса БД
        self.database = Database()
        self._frame = None

        # Установка фотографии
        icon = PhotoImage(file="icons/app_icon_png.png")
        self.iconphoto(False, icon)
        # Установка стартовых значений W/H и их пределов редактирования
        self.geometry("600x600")
        self.minsize(550, 450)
        self.maxsize(650, 800)


        # Контейнер для фреймов
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Словарь для хранения фреймов
        self.frames = {}

        # Инициализация фреймов с передачей контроллера
        for F in (PartnerForm, MainFrame, HistoryFrame,AddPartnerForm, UpdatePartnerForm):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainFrame)

    # Отображение фреймов
    def show_frame(self, cont, **kwargs):
        ''' Метод для переключения между окнами '''
        frame = self.frames[cont]
        # Если есть метод update_data -> вызвать его
        if hasattr(frame, 'update_data') and kwargs:
            frame.update_data(**kwargs)
        frame.tkraise()

    # Открытие окна PartnerForm
    def open_partner_form(self, partner_name: str=None):
        ''' Открытие окна PartnerForm
        partner_name: str -> Имя интересующего партнера'''
        # Запись в статический класс имени партнера
        if partner_name:
            Partner.set_name(partner_name)
        # Выбор из списка фреймов - требуемый фрейм
        partner_form = self.frames[PartnerForm]

        # Вызов функции для установки данных в окне
        partner_form.set_partner_data()

        # Открытие окна
        self.show_frame(PartnerForm)

    # Открытие окна обновления информации о партнере
    def open_partner_update_form(self, partner_name: str=None):
        ''' Открытие окна UpdatePartnerForm '''
        # Сохранение в статическом классе имени обрабатываемого партнера
        if partner_name:
            Partner.set_name(partner_name)

        # Выбор из списка фреймов - требуемый фрейм
        update_frame = self.frames[UpdatePartnerForm]

        # Запуск функции выгрузки инфомрации про пользователя
        update_frame.set_partner_update_data()

        # Открытие окна
        self.show_frame(UpdatePartnerForm)

    # Открытие окна Истории продаж партнера
    def open_history_frame(self):
        ''' Открытие окна HistoryFrame '''
        history_frame = self.frames[HistoryFrame]
        history_frame.load_sales_data()
        # Открытие окна
        self.show_frame(HistoryFrame)

    # Переход на главное окно
    def open_main_frame(self):
        ''' Открытие окна MainFrame '''
        set_partners_data = self.frames[MainFrame]

        # Вызов принудительного обновления Дата фрейма с партнерской информацией
        set_partners_data.update_partner_display()

        # Открытие фрейма с карточками партнеров
        self.show_frame(MainFrame)



if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()
