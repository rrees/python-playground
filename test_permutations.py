import unittest
import heap_permutations as hp

class TestPermutations(unittest.TestCase):
	def test_no_permutations(self):
		array = [1]
		self.assertEqual(hp.permutations(array), [array])

	def test_simple_permutations(self):
		array = [1, 2]

		permutations = [[1,2], [2,1]]

		self.assertEqual(hp.permutations(array), permutations)