import unittest
import heap_permutations as hp

class TestPermutations(unittest.TestCase):
	def test_no_permutations(self):
		array = [1]
		self.assertEqual(hp.permutations(array), array)