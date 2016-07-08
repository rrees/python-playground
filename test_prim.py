import unittest

import graph_prim

class TestPrimImplementation(unittest.TestCase):

	def test_example(self):

		edges = {
			(1,2): 2,
			(2,1): 2,
			(1,4): 1,
			(4,1): 1,
			(2,4): 2,
			(4,2): 2,
			(3,4): 3,
			(4,3): 3,
		}

		adjacency = {
			1: [2,4],
			2: [1,4],
			3: [4],
			4: [1,2,3]
		}

		cost = graph_prim.prim_mst(edges,adjacency, 4, 1)

		self.assertEqual(cost, 6)
