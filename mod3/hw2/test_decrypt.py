import unittest

from decrypt import decrypt




class TestDecrypt(unittest.TestCase):
	def test_decrypt_1(self):
		input = "абра-кадабра."
		expected = "абра-кадабра"
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_2(self):
		input = "абраа..-кадабра"
		expected = "абра-кадабра"
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_3(self):
		input = "абраа..-.кадабра"
		expected = "абра-кадабра"
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_4(self):
		input = "абра--..кадабра"
		expected = "абра-кадабра"
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_5(self):
		input = "абрау...-кадабра"
		expected = "абра-кадабра"
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_6(self):
		input = "абра........"
		expected = ""
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_7(self):
		input = "абр......а."
		expected = "а"
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_8(self):
		input = "1..2.3"
		expected = "23"
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_9(self):
		input = "."
		expected = ""
		self.assertEqual(expected, decrypt(input))

	def test_decrypt_10(self):
		input = "1......................."
		expected = ""
		self.assertEqual(expected, decrypt(input))


if __name__ == "__main__":
	unittest.main()

