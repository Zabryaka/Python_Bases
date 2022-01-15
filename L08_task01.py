class EnterData:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_data(cls, datum):
        d, m, y = map(int, datum.split("-"))
        return cls(d, m, y)

    @staticmethod
    def data_valid(obj):
        if obj.day > 31:
            return f"С днём что-то не так"
        elif obj.month > 13:
            return f"С месяцем что-то не так"
        elif obj.year > 2021:
            return f"С годом что-то не так"
        else:
            return f"Дата похожа на правду"


data = input('Введите дату в формате DD-MM-YYYY: ')
new_data = EnterData.get_data(data)
print(new_data.year)
print(type(new_data.year))
print(EnterData.data_valid(new_data))
