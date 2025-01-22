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

	def test_complex_permutations(self):
		array = [1, 2, 3]

		permutations = [[1,2,3], [2,1,3], [3,1,2], [1,3,2], [3,2,1], [2,3,1]]

		self.assertCountEqual(hp.permutations(array), permutations)