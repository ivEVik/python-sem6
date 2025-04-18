import unittest

import accounting
from accounting import add
from accounting import calculate_year
from accounting import calculate_month


class TestAccounting(unittest.TestCase):
	def test_accounting_add(self):
		accounting.storage = { 2024: { 4: { 2: 22, 3: 46, 8: 22}, 1: { 8: 33}} }
		date = "20211123"
		add(date, 33)
		self.assertEqual(33, accounting.storage[2021][11][23])

	def test_accounting_add_short_date(self):
		accounting.storage = { 2024: { 4: { 2: 22, 3: 46, 8: 22}, 1: { 8: 33}} }
		date = "202111"
		with self.assertRaises(AssertionError):
			add(date, 33)

	def test_accounting_add_long_date(self):
		accounting.storage = { 2024: { 4: { 2: 22, 3: 46, 8: 22}, 1: { 8: 33}} }
		date = "202111891258153189535"
		with self.assertRaises(AssertionError):
			add(date, 33)

	def test_accounting_add_not_date(self):
		accounting.storage = { 2024: { 4: { 2: 22, 3: 46, 8: 22}, 1: { 8: 33}} }
		date = "asfwaaaa"
		with self.assertRaises(AssertionError):
			add(date, 33)

	def test_accounting_calculate_year(self):
		accounting.storage = { 2024: { 4: { 2: 22, 3: 46, 8: 22}, 1: { 8: 33} } }
		year = 2024
		self.assertEqual("123", calculate_year(year))

	def test_accounting_calculate_year_empty(self):
		accounting.storage = {}
		year = 2024
		self.assertEqual("0", calculate_year(year))

	def test_accounting_calculate_month(self):
		accounting.storage = { 2024: { 4: { 2: 22, 3: 46, 8: 22}, 1: { 8: 33}} }
		year = 2024
		month = 4
		self.assertEqual("90", calculate_month(year, month))

	def test_accounting_calculate_month_small(self):
		accounting.storage = { 2024: { 4: { 2: 22, 3: 46, 8: 22}, 1: { 8: 33}} }
		year = 2024
		month = -1
		with self.assertRaises(AssertionError):
			calculate_month(year, month)

	def test_accounting_calculate_month(self):
		accounting.storage = { 2024: { 4: { 2: 22, 3: 46, 8: 22}, 1: { 8: 33}} }
		year = 2024
		month = 33
		with self.assertRaises(AssertionError):
			calculate_month(year, month)

	def test_accounting_calculate_month_empty(self):
		accounting.storage = {}
		year = 2024
		month = 4
		self.assertEqual("0", calculate_year(year))


if __name__ == "__main__":
	unittest.main()

