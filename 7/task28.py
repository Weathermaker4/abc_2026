# abc_2026
# Федосов Артем

#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

# Шифруем текст в цифры из примера
text = "8 5 12 12 15 , 0 23 15 18 12 4 !"

words = text.split()
result = ""
# Добавляем из примера проверку на ноль и меняем его на пробел
for word in words:
    if word == "0":
        result = result + " "
    elif word.isdigit():
        result = result + chr(int(word) + 96)
    else:
        result = result + word

print(result)
