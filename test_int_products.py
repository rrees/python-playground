import unittest

import int_products

class TestProducts(unittest.TestCase):
	def test_products(self):
		input = [1,2,3]
		output = [6,3,2]
		self.assertEqual(int_products.calculate(input), output)

	def test_zeroes(self):
		input = [1,0,3,4]
		output = [0,12,0,0]
		self.assertEqual(int_products.calculate(input), output)
