# abc_2026
# Федосов Артем


# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

# Пример использования
# book = Product("Book", 10)
# pen = Product("Pen", 2)
# order = Order()
# order.add_product(book)
# order.add_product(pen)
# print(f"Общая стоимость: {order.total_price}")  # 12


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price  # Вызываем сеттер для чека цены

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            self._price = 0.0
        else:
            self._price = float(value)


class Order:
    def __init__(self):
        # Внутренний список для хранения объектов класса Product
        self._products = []

    def add_product(self, product: Product):
        # Добавляем товар в заказ
        if isinstance(product, Product):
            self._products.append(product)
        else:
            raise TypeError("Можно добавить только объект класса Product")

    def remove_product(self, product: Product):
        # Удаляем товар из заказа. Если товара нет, ничего не происходит
        if product in self._products:
            self._products.remove(product)

    @property
    def total_price(self) -> float:
        # Возвращаем общую стоимость всех товаров
        return sum(product.price for product in self._products)


# Смотрим
if __name__ == "__main__":
    book = Product("Book", 10)
    pen = Product("Pen", 2)
    
    order = Order()
    order.add_product(book)
    order.add_product(pen)
    
    # Считаем суммы
    print(f"Общая стоимость: {order.total_price}")
    
    # Удаляем ручку
    order.remove_product(pen)
    print(f"После удаления ручки: {order.total_price}")

