import unittest

import reverse

class ReverseStringTest(unittest.TestCase):
	def test_reverse_string(self):
		s = "Hello"
		t = "olleH"

		self.assertEqual(reverse.a_string(s), t)
