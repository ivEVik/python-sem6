"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output):
	if len(ls_output) == 0:
		return 0

	sum = 0
	for line in ls_output:
		columns = line.split()
		if not columns[4].isdigit():
			continue
		sum += int(columns[4])

	return sum / len(ls_output)


if __name__ == '__main__':
	data = sys.stdin.readlines()[1:]
	mean_size = get_mean_size(data)
	print(mean_size)
