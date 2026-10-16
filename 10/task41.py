# abc_2026
# Федосов Артем



# Реализуйте базовый класс NotificationSender с методом send(message, user) и наследников EmailSender, SMSSender, PushSender.
# Они изображают отправку выводом в консоль.

# Форматы строк:

# Email для ИМЯ | Образовательная платформа | СООБЩЕНИЕ
# SMS для ИМЯ | СООБЩЕНИЕ
# Push для ИМЯ | 🎓 СООБЩЕНИЕ
# В SMS оставьте первые 50 символов сообщения, в email и push — весь текст.
# Класс User(name, preferred_notifications) хранит имя и список объектов отправителей в атрибутах с теми же именами.
# Функция notify_user(user, message) вызывает send каждого выбранного отправителя в порядке списка.
# Используйте полиморфный вызов метода, чтобы можно было добавить другой отправитель.

# Добавьте пример с Марией, каналами email и push, сообщением «Блок аналитики начинается с 27 октября!».


class NotificationSender:
    def send(self, message, user):
        raise NotImplementedError


class EmailSender(NotificationSender):
    def send(self, message, user):
        # email для имени | Образовательная платформа | СООБЩЕНИЕ
        print(f"Email для {user.name} | Образовательная платформа | {message}")


class SMSSender(NotificationSender):
    def send(self, message, user):
        # смс для имени | первые 50 символов сообщения
        print(f"SMS для {user.name} | {message[:50]}")


class PushSender(NotificationSender):
    def send(self, message, user):
        # пуш для имени | 🎓 пуш
        print(f"Push для {user.name} | 🎓 {message}")


class User:
    def __init__(self, name, preferred_notifications):
        # атрибуты с теми же именами,что и параметры
        self.name = name
        self.preferred_notifications = preferred_notifications


def notify_user(user, message):
    for sender in user.preferred_notifications:
        sender.send(message, user)


# смотрим
maria = User("Мария", [EmailSender(), PushSender()])
notify_user(maria, "Блок аналитики начинается с 27 октября!")
