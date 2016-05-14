import unittest

import words

class TestReversingWordOrder(unittest.TestCase):
    def test_simple_case(self):
        s = "hello world"
        t = "world hello"

        self.assertEqual(words.reverse(s), t)
