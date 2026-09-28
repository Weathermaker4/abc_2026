# abc_2026
# Федосов Артем

#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

#algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
            # "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
            # "Наивный байесовский классификатор", "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
#1) "C4.5"
#2) "k - means"



import csv

# Исходный список алгоритмов
algoritm = [
    "C4.5", "k - means", "Метод опорных векторов", "Apriori", "EM", 
    "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"
]

# Открываем файл для записи, encoding для кодировки
with open('algoritm.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    
    # Записываем заголовки столбов
    writer.writerow(['id)', 'значение из списка algoritm'])
    
    # Цикл for + форматируем 
    for index, name in enumerate(algoritm, start=1):
        row_id = f"{index})"
        writer.writerow([row_id, name])

print("Файл algoritm.csv создан")
