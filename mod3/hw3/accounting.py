"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""


from flask import Flask


app = Flask(__name__)


storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
	assert len(date) >= 7 and len(date) <= 8 and date.isdigit(), "Invalid date."

	year = int(date[:4])
	month = int(date[4:-2])
	day = int(date[-2:])

	storage.setdefault(year, {}).setdefault(month, {})

	storage[year][month][day] = number
	return f"{day}.{month}.{year} += {number}"

@app.route("/calculate/<int:year>")
def calculate_year(year: int):
	sum = 0

	storage.setdefault(year, {})

	for month in storage[year]:
		for day in storage[year][month]:
			sum += storage[year][month][day]

	return str(sum)


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
	assert month >= 1 and month <= 12

	sum = 0

	storage.setdefault(year, {}).setdefault(month, {})

	for day in storage[year][month]:
		sum += storage[year][month][day]

	return str(sum)


if __name__ == "__main__":
	app.run(debug=True, host = "0.0.0.0")

