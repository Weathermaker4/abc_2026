# abc_2026
# Федосов Артем

#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

# Результат
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.


import os

filename = 'inverted_sort.txt'

# Делаем файлик
if not os.path.exists(filename):
    initial_text = (
        "Beautiful is better than ugly.\n"
        "Explicit is better than implicit.\n"
        "Simple is better than complex.\n"
        "Complex is better than complicated.\n"
    )
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(initial_text)
    print(f"Файла {filename} не было, но я его сделал")

# Читаем
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
