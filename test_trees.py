import unittest

import trees

class TestTrees(unittest.TestCase):
	def test_tree_traversal(self):
		tree = trees.create_tree("html", [("html", "body"), ("html", "head")])

		tree_content = trees.bfs_content(tree)

		self.assertEqual(tree_content, ["html", "body", "head"])