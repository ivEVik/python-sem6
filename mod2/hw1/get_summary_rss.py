"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""

import os


BASE_PATH = os.path.dirname(os.path.abspath(__name__))


def get_summary_rss(ps_output_file_path):
	file = open(path, mode = "r", encoding = "utf-8")
	lines = file.readlines()[1:]
	sum = 0

	for line in lines:
		columns = line.split()
		sum += int(columns[5])

	size = 0
	while sum // 1024 > 0 and size < 4:
		sum /= 1024.0
		size += 1

	match size:
		case 1:
			return f"{sum:.3f} KB"
		case 2:
			return f"{sum:.3f} MB"
		case 3:
			return f"{sum:.3f} GB"
		case 4:
			return f"{sum:.3f} TB"
	return f"{sum:.3f} B"


if __name__ == "__main__":
	path = os.path.join(BASE_PATH, "output_file.txt")
	summary_rss = get_summary_rss(path)
	print(summary_rss)

