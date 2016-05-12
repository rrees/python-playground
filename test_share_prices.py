import unittest

import share_prices

class TestMargins(unittest.TestCase):

	def test_simple_interval(self):
		prices = [1, 2, 3]
		expected_margin = 2

		self.assertEqual(share_prices.calculate_margin(prices), expected_margin)
