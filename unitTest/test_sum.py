import unittest

from sum import add

"""
This class test the result to add input variables
"""
class TestSum(unittest.TestCase):
    """
    This function returns the assert output
    """
    def test1(self):
        self.assertEqual(add(2,4), 6) # test when inputs are 2 and 4, output is 6
        self.assertEqual(add(0,0), 0) # test when 0, 0 are given as input, the output is 0
        self.assertEqual(add(2.3, 3.6), 5.9) # test when 2,3 and 3.6 are given as inputs, the output is 5.9
        self.assertEqual(add('hello', 'world'), 'helloworld') # test when 'hello' and 'world' are given as input and the output is 'helloworld'
        self.assertEqual(add(2.3000, 4.300), 6.6) # test when inputs are 2.3000 and 4.300, output is 6.6
        self.assertNotEqual(add(-2, -2), 0) # test when inputs are -2 and -2, output is not 0

unittest.main()
