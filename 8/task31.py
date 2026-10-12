# abc_2026
# Федосов Артем


# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.

# Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")



class Temperature:
    def __init__(self, celsius: float = 0.0):
        # Внутреннее хранение температуры только в Цельсиях
        self._celsius = float(celsius)

    @property
    def celsius(self) -> float:
        # Получаем температуру в Цельсиях
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        # Устанавливаем температуру в Цельсиях
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        # Получаем температуру в Фаренгейтах
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        # Устанавливаем температуру через Фаренгейты и конвертируем в Цельсии)
        self._celsius = (float(value) - 32) * 5 / 9

    @property
    def kelvin(self) -> float:
        # Получаем температуру в Кельвинах
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float):
        # Устанавливаем температуру через Кельвины и конвертируем в Цельсии
        if float(value) < 0:
            raise ValueError("Температура в Кельвинах не может быть ниже абсолютного нуля (0 K).")
        self._celsius = float(value) - 273.15


# Смотрим
if __name__ == "__main__":
    t = Temperature(25)
    print(f"{t.celsius}°C, {t.fahrenheit}°F, {t.kelvin} K")
    
    t.fahrenheit = 32
    print(f"После установки 32F: {t.celsius}°C")
    
    t.kelvin = 300
    print(f"После установки 300K: {t.celsius:.2f}°C, {t.fahrenheit:.2f}°F")
