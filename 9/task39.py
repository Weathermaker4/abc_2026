# abc_2026
# Федосов Артем


# Создайте в одном скрипте классы Product(name, price) и Order().
# У товара свойства name и price позволяют чтение и запись, отрицательная цена заменяется нулём.

# Заказ хранит список экземпляров товаров в products.
# Метод add_product(product) добавляет товар, remove_product(product) удаляет одно его вхождение, если оно есть.
# Свойство total_price доступно для чтения и каждый раз вычисляет сумму текущих цен товаров.
# Пустой заказ стоит 0.

# Добавьте пример: положите в заказ книгу за 10 и ручку за 2, выведите общую стоимость.


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
        # отрицательная цена заменяется нулем
        self._price = 0 if value < 0 else value


class Order:
    def __init__(self):
        # список товаров в заказе
        self.products = []

    def add_product(self, product):
        # добавляем товар в конец списка
        self.products.append(product)

    def remove_product(self, product):
        # удаляем одно вхождение, если оно есть
        if product in self.products:
            self.products.remove(product)

    @property
    def total_price(self):
        # сумма текущих цен всех товаров. для пустого вернет 0
        return sum(p.price for p in self.products)


# смотирим
book = Product("Book", 10)
pen = Product("Pen", 2)

order = Order()
order.add_product(book)
order.add_product(pen)

print(order.total_price)
