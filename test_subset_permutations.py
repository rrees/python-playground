import unittest

import my_permutations

class SubsetPermutations(unittest.TestCase):

	def test_simple_case(self):

		my_set = [1,2,3]
		target_subsets = [[1,2], [1,3], [2,1], [2,3], [3,1], [3,2]]

		self.assertCountEqual(my_permutations.subsets(my_set, 2), target_subsets)