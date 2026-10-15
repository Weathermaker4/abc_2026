# abc_2026
# Федосов Артем


# Создайте класс Product(name, price) со свойствами name и price для чтения и записи
# При отрицательной цене устанавливайте 0, в том числе при создании товара.
# Добавьте пример: создайте Product('Book', 10), выведите цену, присвойте цене -5 и выведите её снова.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # name: чтение и запись
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # price: чтение и запись с защитой от отрицательных значений
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # отрицательная цена в 0
        if value < 0:
            self._price = 0
        else:
            self._price = value


# смотрим
p = Product("Book", 10)
print(p.price)

p.price = -5
print(p.price)
