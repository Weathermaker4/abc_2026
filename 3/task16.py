# abc_2026
# Fedosov Artem


# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

#Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
#,первой букве логина, и заданной группе.

# Сперва вводится тип сортировки:
#1. По возрасту
#2. По первой букве
#3. По группе

# тип сортировки: 1

# Затем сообщение для ввода
# Введите критерии поиска: 16

# Результат:
# Пользователь: 'Piter' возраст 23 года , группа  "admin"
# Пользователь: 'Dasha' возраст 30 лет , группа  "master"


# Массив объектов пользователей
users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan',  'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"}
]

# Выбираем тип сортировки / фильтрации
print("Выберите тип сортировки:")
print("1. По возрасту")
print("2. По первой букве")
print("3. По группе")

sort_type = input("тип сортировки: ")

# Список, куда будем складывать подходящих пользователей
filtered_users = []

# Фильтруем данные в зависимости от выбора
if sort_type == "1":
    age_limit = int(input("Введите критерии поиска (минимальный возраст): "))
    for user in users:
        if user['age'] > age_limit:
            filtered_users.append(user)

elif sort_type == "2":
    letter = input("Введите критерии поиска (первая буква логина): ")
    for user in users:
        # user['login'][0] — это первая буква логина
        if user['login'][0] == letter:
            filtered_users.append(user)

elif sort_type == "3":
    group_name = input("Введите критерии поиска (группа): ")
    for user in users:
        if user['group'] == group_name:
            filtered_users.append(user)

else:
    print("Неверный тип сортировки!")

# Выводим результат
print("\nРезультат:")
for user in filtered_users:
    print("Пользователь:", f"'{user['login']}'", "возраст", user['age'], "группа", f"\"{user['group']}\"")
