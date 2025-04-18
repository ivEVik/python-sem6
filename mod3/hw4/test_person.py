import unittest

from datetime import datetime

from person import Person


class TestPerson(unittest.TestCase):
	def test_person_constructor_full(self):
		name = "Ivan"
		yob = 2000
		address = "31 Testing Street"

		per = Person(name, yob, address)

		self.assertEqual(per.name, name)
		self.assertEqual(per.yob, yob)
		self.assertEqual(per.address, address)

	def test_person_constructor_no_address(self):
		name = "Ivan"
		yob = 2000

		per = Person(name, yob)

		self.assertEqual(per.name, name)
		self.assertEqual(per.yob, yob)
		self.assertEqual(per.address, "")

	def test_person_get_age(self):
		name = "Ivan"
		yob = 2000
		address = "31 Testing Street"

		per = Person(name, yob, address)

		expected = datetime.now().year - yob
		self.assertEqual(expected, per.get_age())

	def test_person_get_name(self):
		name = "Ivan"
		yob = 2000
		address = "31 Testing Street"

		per = Person(name, yob, address)
		per.name = name

		self.assertEqual(name, per.get_name())

	def test_person_set_name(self):
		name = "Ivan"
		yob = 2000
		address = "31 Testing Street"

		per = Person(name, yob, address)

		expected = "Petr"
		per.set_name(expected)

		self.assertEqual(expected, per.name)

	def test_person_set_address(self):
		name = "Ivan"
		yob = 2000
		address = "31 Testing Street"

		per = Person(name, yob, address)

		expected = "11 Expected Street"
		per.set_address(expected)

		self.assertEqual(expected, per.address)

	def test_person_get_address(self):
		name = "Ivan"
		yob = 2000
		address = "31 Testing Street"

		per = Person(name, yob, address)
		per.address = address

		self.assertEqual(address, per.get_address())

	def test_person_is_homeless(self):
		name = "Ivan"
		yob = 2000

		per = Person(name, yob)

		self.assertEqual(True, per.is_homeless())


if __name__ == "__main__":
	unittest.main()

