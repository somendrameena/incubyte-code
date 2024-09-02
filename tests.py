import unittest

from utils import add


class AddTestCase(unittest.TestCase):
    """
    Test cases for add function
    """

    # def test_blank_string(self):
    #     result = add("")
    #     self.assertEqual(result, 0)
    
    def test_zero(self):
        result = add("0")
        self.assertEqual(result, 0)
    
    def test_zeroes(self):
        result = add("0,0,0")
        self.assertEqual(result, 0)