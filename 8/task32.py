# abc_2026
# Федосов Артем


# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

# Пример использования
# user = User("test@example.com", "secret")
# print(user.email)  # test@example.com
# print(user.password) # AttributeError
# print(user.check_password("secret"))  # True
# print(user.check_password("wrong"))   # False


class User:
    def __init__(self, email: str, password: str):
        self.email = email  # Вызываем сеттер для проверки email
        self.password = password  # Вызываем сеттер для хэширования пароля

    @property
    def email(self) -> str:
        # Получаем email юзера 
        return self._email

    @email.setter
    def email(self, value: str):
        # Устанавливаем email с чеком на наличие символа '@'
        if "@" not in value:
            raise ValueError("Некорректный формат email: отсутствует символ '@'")
        self._email = value

    @property
    def password(self):
        # Запрещаем прямой доступ к просмотру пароля или его хэша
        raise AttributeError("Доступ к свойству 'password' запрещен.")

    @password.setter
    def password(self, value: str):
        self._password_hash = hash(value)

    def check_password(self, password: str) -> bool:
        return self._password_hash == hash(password)


# Смотрим
user = User ("test@example.com", "secret")

print(user.email)

try:
    print(user.password)
except AttributeError as e:
    print(f"Ошибка: {e}")

print(user.check_password("secret"))
print(user.check_password("wrong"))
