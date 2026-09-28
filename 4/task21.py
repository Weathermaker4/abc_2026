# abc_2026
# Федосов Артем

#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?

# Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?

# Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?

# Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?


import os

# Текст исходника , если файла нет
default_template = """# Конфигурация приложения:
# app_name    = ?
# version     = ?
# debug       = ?

# Настройки базы данных:
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?

# Настройки API:
# api_key     = ?
# api_secret  = ?
# base_url    = ?

# Пути:
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?"""

# Проверяем, существует ли config_default.txt. Если нет - создадим новый
if not os.path.exists("config_default.txt"):
    with open("config_default.txt", "w", encoding="utf-8") as file:
        file.write(default_template)
    print("Исходный файл config_default.txt не был найден и создан автоматически.")

# Данные для подстановки
config_data = {
    "app_name": "MyCoolApp",
    "version": "1.0.4",
    "debug": "True",
    "db_host": "localhost",
    "db_port": "5432",
    "db_name": "main_db",
    "db_user": "admin",
    "db_password": "super_secret_password",
    "api_key": "xyz123abc",
    "api_secret": "secret_key_here",
    "base_url": "https://example.com",
    "log_file": "/var/log/app.log",
    "data_dir": "./data",
    "temp_dir": "/tmp"
}

# Лямбда-функция для замены символов "?" на значения из словаря
fill_line = lambda line, data: next(
    (line.replace("?", data[key]) for key in data if key in line), 
    line
)

# Читаем созданный или уже существующий файл
with open("config_default.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Генератор списка (list comprehension) для обработки строк
final_lines = [
    fill_line(line, config_data) if "?" in line and "=" in line else line 
    for line in lines
]

# Записываем результат в config.txt
with open("config.txt", "w", encoding="utf-8") as file:
    file.writelines(final_lines)

print("Проверь файл config.txt! Результат там!")
