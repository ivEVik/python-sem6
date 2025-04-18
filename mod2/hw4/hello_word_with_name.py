"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from datetime import datetime

from flask import Flask


app = Flask(__name__)

WEEKDAYS = ("го понедельника", "го вторника", "й среды", "го четверга", "й пятницы", "й субботы", "го воскресенья")



@app.route("/hello-world/<name>")
def hello_world(name):
	return f"Привет, {name}. Хороше{WEEKDAYS[datetime.today().weekday()]}!"


if __name__ == "__main__":
	app.run(debug=True, host = "0.0.0.0")

