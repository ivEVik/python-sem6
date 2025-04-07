from datetime import datetime
from datetime import timedelta
import os
import random
import re

from flask import Flask


app = Flask(__name__)


def read_file(path):
	file = open(path, mode = "r", encoding = "utf-8")
	text = file.read()
	file.close()
	return text

def words_from_file(path):
	result = set(re.split(r"[\W]+", read_file(path)))
	result.discard("")
	result = tuple(result)
	return result


@app.route("/hello_world")
def ep_hello_world():
	return "Привет, мир!"


cars = [
	"Chevrolet",
	"Renault",
	"Ford",
	"Lada"
]

@app.route("/cars")
def ep_cars():
	return ", ".join(cars)


cats = [
	"корниш-рекс",
	"русская голубая",
	"шотландская вислоухая",
	"мейн-кун",
	"манчкин"
]

@app.route("/cats")
def ep_cats():
	return random.choice(cats)


@app.route("/get_time/now")
def ep_now():
	current_time = datetime.now()
	return f"Точное время: {current_time}"


FUTURE_OFFSET = timedelta(hours = 1)

@app.route("/get_time/future")
def ep_future():
	time = datetime.now() + FUTURE_OFFSET
	return f"Точное время через час будет {time}"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, "war_and_peace.txt")

words = words_from_file(BOOK_FILE)

@app.route("/get_random_word")
def ep_get_random_word():
	return random.choice(words)


counter_page_opens = 0

@app.route("/counter")
def ep_counter():
	global counter_page_opens
	counter_page_opens += 1
	return str(counter_page_opens)


if __name__ == "__main__":
	app.run(debug=True)
