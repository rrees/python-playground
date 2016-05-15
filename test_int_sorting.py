import unittest

import sorts

class TestIntSorting(unittest.TestCase):
    def test_degenerate_cases(self):
        datapoints = [([0, 0, 0], [0, 0, 0]),
            ([1, 2, 3], [1, 2, 3])]

        for ints, target in datapoints:
            self.assertEqual(sorts.ints_left_zero(ints), target)

    def test_left_zero_sort(self):

        datapoints = [([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),]

        for ints, target in datapoints:
            self.assertEqual(sorts.ints_left_zero(ints), target, msg = ints)
