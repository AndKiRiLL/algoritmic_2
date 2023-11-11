# Объявляем класс Automobile
class Automobile:

    # Инициализируем переменные
    def __init__(self, brand='', model='', year_of_issue=0, mileage=0):
        self.brand = brand
        self.model = model
        self.year_of_issue = year_of_issue
        self.mileage = mileage

    # Метод получения информации о машине
    def get_info(self):
        print('Информация о машине:')
        print(f'Марка: {self.brand}')
        print(f'Модель: {self.model}')
        print(f'Год выпуска: {self.year_of_issue}')
        print(f'Пробег: {self.mileage}')

    # Метод изменения информации о машине
    def set_info(self, new_brand, new_model, new_year_of_issue, new_mileage):
        print('Изменены следующие значения:')
        print(f'Марка: {self.brand} --> {new_brand}')
        self.brand = new_brand
        print(f'Модель: {self.model} --> {new_model}')
        self.model = new_model
        print(f'Год выпуска: {self.year_of_issue} --> {new_year_of_issue}')
        self.year_of_issue = new_year_of_issue
        print(f'Пробег: {self.mileage} --> {new_mileage}')
        self.mileage = new_mileage

# Задаём класс Automobile в переменную a
a = Automobile('Mercedes-Benz', 'E-Class', 2021, 3000)

# получаем информацию
a.get_info()
print()

# изменяем информацию
a.set_info('Audi', 'A-Class', 2022, 1000)
print()

# получаем информацию
a.get_info()