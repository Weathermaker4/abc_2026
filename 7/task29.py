# abc_2026
# Федосов Артем

#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.


cipher_text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

# Перебираем все возможные сдвиги от 0 до 25
for shift in range(26):
    decrypted_chars = []
    
    for char in cipher_text:
        # Проверяем, является ли символ строчной буквой
        if 'a' <= char <= 'z':
            # Сдвигаем букву назад по алфавиту
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_chars.append(new_char)
        else:
            # Оставляем знаки препинания, пробелы и апострофы без изменений
            decrypted_chars.append(char)
            
    # Собираем символы обратно в строку
    decrypted_text = "".join(decrypted_chars)
    
    # Выводим результат для сдвига, равного...
    print(f"Сдвиг равен {shift:2d}: {decrypted_text}")
