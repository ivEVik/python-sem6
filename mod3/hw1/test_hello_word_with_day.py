from datetime import datetime
import unittest

from hello_word_with_day import hello_world


WEEKDAYS = ("го понедельника", "го вторника", "й среды", "го четверга", "й пятницы", "й субботы", "го воскресенья")


class TestHelloWorldWithDay(unittest.TestCase):
	def test_hello_world(self):
		name = "Иван"
		expected = f"Привет, {name}. Хороше{WEEKDAYS[datetime.today().weekday()]}!"
		self.assertEqual(expected, hello_world(name))

	def test_hello_world_empty(self):
		name = ""
		expected = f"Привет, {name}. Хороше{WEEKDAYS[datetime.today().weekday()]}!"
		self.assertEqual(expected, hello_world(name))

if __name__ == "__main__":
	unittest.main()

