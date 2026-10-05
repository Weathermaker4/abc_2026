# abc_2026
# Федосов Артем


#todo: Допишите для игры "Поле чудес" функции сохранения и загрузки игры через сериализацию.
# Данные сериализации записываются и сохраняются в файле.

import os
import pickle
import random

SAVE_FILE = "save.pickle"

_dict = {
    'False': 'Логическое значение',
    'None': 'Пустое значение'
}


class Game:
    # Класс, хранящий текущее состояние и логику игры
    def __init__(self):
        keys = list(_dict.keys())
        self.secret = random.choice(keys)
        self.mask = [' * '] * len(self.secret)

    def show_describe(self):
        # Выводим описание слова
        print(f"\nПодсказка: {_dict[self.secret]}")

    def show_secret(self):
        # Выводим загаданное слово с открытыми буквами
        print("Загаданное слово: ", end="")
        for val in self.mask:
            print(val, end="")
        print()

    def check_letter(self, letter):
        # Проверяем наличие буквы в слове
        for ind, val in enumerate(self.secret):
            if val.upper() == letter.upper():
                self.mask[ind] = f" {val} "

    def is_finished(self):
        # Проверяем, отгадано ли слово целиком
        return " * " not in self.mask


def save_game(game_instance):
    # Сериализуем и сохраняем объект игры в бинарник
    try:
        with open(SAVE_FILE, "wb") as f:
            pickle.dump(game_instance, f)
        print("\n[!] Игра успешно сохранена!")
    except Exception as e:
        print(f"\n[!] Ошибка при сохранении: {e}")


def load_game():
    # Загружаем и десериализуем объект игры из бинарника
    try:
        with open(SAVE_FILE, "rb") as f:
            game_instance = pickle.load(f)
        print("\n[!] Предыдущая игра успешно загружена!")
        return game_instance
    except Exception as e:
        print(f"\n[!] Ошибка при загрузке сохранения: {e}")
        return None


def get_letter():
    # Запрашиваем ввод у игрока на букву или сэйв
    return input("\nВведите букву (или 'сохранить' / 'save' для записи игры): ").strip()


def start():
    # Главная функция запуска игры
    game = None

    # Проверяем наличие файла сохранения
    if os.path.exists(SAVE_FILE):
        choice = input("Найдена сохраненная игра. Загрузить? (да/нет): ").strip().lower()
        if choice in ['да', 'd', 'yes', 'y']:
            game = load_game()

    # Если игра не была загружена - создаем новую
    if game is None:
        game = Game()

    # Основной игровой цикл
    while not game.is_finished():
        game.show_describe()
        game.show_secret()

        user_input = get_letter()

        # Команда сохранения
        if user_input.lower() in ['сохранить', 'save']:
            save_game(game)
            continue

        if user_input:
            game.check_letter(user_input[0]) # Берем только первый символ

    # Победа
    game.show_secret()
    print("\nЭто победа!")

    # Удаляем файл сохранения после победы
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)


# Вызов главной функции
start()
