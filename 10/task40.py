# abc_2026
# Федосов Артем


# Создайте базовый класс LearningMaterial(title, author, duration_minutes) и его наследников.
# Метод display_info() выводит название, автора и длительность через |.
# Метод get_difficulty() базового класса возвращает Средняя.
# Параметры конструкторов храните в атрибутах с теми же именами.

# VideoLesson(title, author, duration_minutes, video_quality, subtitles_available) хранит качество и наличие субтитров, сложность — Средняя.
# Article(title, author, duration_minutes, word_count, reading_level) хранит число слов и уровень чтения.
# Менее 1000 слов — Лёгкая, с 1000 по 3000 включительно — Средняя, больше 3000 — Сложная.
# Quiz(title, author, duration_minutes, questions_count, passing_score) хранит число вопросов и проходной процент.
# Проходной процент больше 80 — Высокая, иначе Средняя.
# Добавьте пример с видео «Python ООП» (автор Иван Иванов, 45 минут, качество 1080p, есть субтитры)
# статьёй «Глубокое обучение» (автор Анна Петрова, 10 минут, 1200 слов, уровень advanced)
# и тестом «Проверка знаний» (автор Платформа, 20 минут, 10 вопросов, проходной процент 75).
# В этом порядке выведите название и сложность каждого материала в формате
# Название: Сложность.


class LearningMaterial:
    def __init__(self, title, author, duration_minutes):
        self.title = title
        self.author = author
        self.duration_minutes = duration_minutes

    def display_info(self):
        # название | автор | длительность
        print(f"{self.title} | {self.author} | {self.duration_minutes}")

    def get_difficulty(self):
        # по умолчанию — средняя
        return "Средняя"


class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_minutes,
                 video_quality, subtitles_available):
        super().__init__(title, author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available

    def get_difficulty(self):
        # видео всегда средняя
        return "Средняя"


class Article(LearningMaterial):
    def __init__(self, title, author, duration_minutes,
                 word_count, reading_level):
        super().__init__(title, author, duration_minutes)
        self.word_count = word_count
        self.reading_level = reading_level

    def get_difficulty(self):
        # сложность зависит от числа слов
        if self.word_count < 1000:
            return "Лёгкая"
        elif self.word_count <= 3000:
            return "Средняя"
        else:
            return "Сложная"


class Quiz(LearningMaterial):
    def __init__(self, title, author, duration_minutes,
                 questions_count, passing_score):
        super().__init__(title, author, duration_minutes)
        self.questions_count = questions_count
        self.passing_score = passing_score

    def get_difficulty(self):
        # проходной процент более 80 - высокая, нет - средняя
        return "Высокая" if self.passing_score > 80 else "Средняя"


# смотрим
materials = [
    VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
    Article("Глубокое обучение", "Анна Петрова", 10, 1200, "advanced"),
    Quiz("Проверка знаний", "Платформа", 20, 10, 75),
]

for m in materials:
    print(f"{m.title}: {m.get_difficulty()}")
