import unittest

import power_sums

class TestPowerSums(unittest.TestCase):
	def test_initial_sums(self):
		for n, sum in [(1, 1), (2, 3), (3, 7)]:
			self.assertEqual(power_sums.of_two(n), sum)