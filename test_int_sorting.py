import unittest

import sorts

class TestIntSorting(unittest.TestCase):
    def test_degenerate_cases(self):
        datapoints = [([0, 0, 0], [0, 0, 0])]

        for ints, target in datapoints:
            self.assertEqual(sorts.ints_left_zero(ints), target)
