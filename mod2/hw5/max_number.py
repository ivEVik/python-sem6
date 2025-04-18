"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""


import sys

from flask import Flask


app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers):
	numbers = numbers.split("/")
	max_number = -sys.maxsize

	for n in numbers:
		if not n.isdigit():
			continue
		if max_number > int(n):
			continue
		max_number = int(n)

	return str(max_number)


if __name__ == "__main__":
	app.run(debug=True, host = "0.0.0.0")

