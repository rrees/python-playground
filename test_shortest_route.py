import unittest

import graphs

class TestShortestRoute(unittest.TestCase):
	def test_calculate_shortest_route(self):

		edges = {
			(0, 1): 5,
			(0, 2): 3,
			(0, 4): 1,
			(1, 3): 2,
			(2, 1): 1,
			(2, 3): 1,
			(3, 0): 1,
			(3, 7): 1,
			(4, 0): 1,
			(4, 8): 7,
			(5, 1): 3,
			(5, 6): 1,
			(6, 2): 3,
			(6, 8): 2,
			(7, 6): 2,
		}



		path, distance = graphs.shortest_route(0, 8, 9, edges)

		self.assertEqual(distance, 8)