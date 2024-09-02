import unittest

from utils import add


class AddTestCase(unittest.TestCase):
    """
    Test cases for add function
    """

    def test_blank_string(self):
        result = add("")
        self.assertEqual(result, 0)
    
    def test_zero(self):
        result = add("0")
        self.assertEqual(result, 0)
    
    def test_zeroes(self):
        result = add("0,0,0")
        self.assertEqual(result, 0)
    
    def test_nums_1(self):
        result = add("0,1,2")
        self.assertEqual(result, 3)
    
    def test_nums_2(self):
        result = add("1,2,3,4")
        self.assertEqual(result, 10)
    
    def test_nums_3(self):
        result = add("3,14,7,42,71")
        self.assertEqual(result, 137)
    
    def test_large_nums_1(self):
        result = add("221,446,163,94")
        self.assertEqual(result, 924)
    
    def test_large_nums_2(self):
        result = add("3134,495,99412,9834")
        self.assertEqual(result, 112875)
    
    def test_negative_nums(self):
        self.assertRaises(Exception, add, "21,55,-22,45")
    
    def test_new_line(self):
        result = add("1\n2,3")
        self.assertEqual(result, 6)
    
    def test_new_delimiter(self):
        result = add("//;\n1;2\n3")
        self.assertEqual(result, 6)