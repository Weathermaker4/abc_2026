# abc_2026
# Федосов Артем


# Создайте класс Temperature(celsius) со свойствами celsius, fahrenheit и kelvin для чтения и записи.
# Внутри экземпляра храните только температуру в градусах Цельсия; значения других шкал вычисляйте.

# Формулы: F = C·9/5 + 32, K = C + 273.15.
# Изменение любого свойства должно сразу отражаться в двух остальных.

# Добавьте пример: создайте температуру 25 °C, выведите значения Цельсия, Фаренгейта и Кельвина, установите 32 °F и снова выведите Цельсии.
# Выводите только числа, разделяя их пробелами или переводами строк.

class Temperature:
    def __init__(self, celsius=0):
        # храним только температуру в цельсиях
        self._celsius = celsius

    # цельсий: чтение и запись
    @property
    def celsius(self):
        # отдаём внутреннее значение
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        # запись напрямую в хранимое поле
        self._celsius = value

    # фаренгейт: чтение и запись
    @property
    def fahrenheit(self):
        # F = C * 9/5 + 32
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        # Обратный пересчёт: C = (F - 32) * 5/9
        self._celsius = (value - 32) * 5 / 9

    # кельвин: чтение и запись
    @property
    def kelvin(self):
        # K = C + 273.15
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value):
        # обратный пересчёт: C = K - 273.15
        self._celsius = value - 273.15


# смотрим
t = Temperature(25)
print(t.celsius, t.fahrenheit, t.kelvin)

t.fahrenheit = 32
print(t.celsius)
