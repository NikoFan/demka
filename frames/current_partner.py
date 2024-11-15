

'''
Статический класс для хранения Имени партнера
'''
class Partner:
    name = None

    @staticmethod
    def get_name():
        return Partner.name

    @staticmethod
    def set_name(name: str):
        Partner.name = name.strip()
