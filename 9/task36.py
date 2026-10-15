# abc_2026
# Федосов Артем


# Создайте класс User(email, password). Свойство email должно позволять чтение и запись, а при присваивании строки без @ вызывать ValueError, сохраняя прежний адрес.
# Та же проверка действует при создании пользователя.

# Свойство password разрешает только запись: чтение вызывает AttributeError. 
# Храните хеш пароля, можно использовать hash(). Метод check_password(password) возвращает True для текущего пароля и False для другого.

# Добавьте пример с адресом test@example.com и паролем secret: выведите адрес и результаты проверки secret и wrong.

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    # email: чтение и запись
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # нет символа @ — ошибка
        if "@" not in value:
            raise ValueError("Email должен содержать @")
        self._email = value

    # password: только запись
    @property
    def password(self):
        # чтение запрещено
        raise AttributeError("Чтение пароля запрещено")

    @password.setter
    def password(self, value):
        # храним хэш, а не пароль
        self._password_hash = hash(value)

    # чек пароля
    def check_password(self, password):
        # Сравниваем хэш введённого пароля с сохранённым
        return hash(password) == self._password_hash


# смотрим
u = User("test@example.com", "secret")
print(u.email)
print(u.check_password("secret"))
print(u.check_password("wrong"))
