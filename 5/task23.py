# abc_2026
# Федосов Артем


# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов


from flask import Flask

app = Flask(__name__)

# Имитируем базу данных со списком постов
posts_db = [
    {"id": 1, "title": "Что-то делали в Python", "views": 100},
    {"id": 2, "title": "А что такое Flask", "views": 330},
    {"id": 3, "title": "Надо бы переписать программу", "views": 1}
]

# Главная страница
@app.route("/")
def index():
    return "<h1>Главная страница</h1><p>Здравствуйте!</p>"

# О компании
@app.route("/about")
def about():
    return "<h1>О компании</h1><p>Мы тут учим Python и Flask.</p>"

# Контакты
@app.route("/contacts")
def contacts():
    return "<h1>Контакты</h1><p>Email: weathermaker4@gmail.com<br>Телефон: +7 (800) 555-35-35</p>"

# Список постов
@app.route("/posts")
def get_posts():
    # Используем генератор списка для превращения словарей в HTML-строки
    posts_li = [f"<li><strong>{post['title']}</strong> (Просмотров: {post['views']})</li>" for post in posts_db]
    
    # Собираем всё в один HTML-список
    html_response = f"<h1>Список постов</h1><ul>{''.join(posts_li)}</ul>"
    return html_response

if __name__ == "__main__":
    # Запуск сервера
    app.run(debug=True)
