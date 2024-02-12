import unittest

from mymodule import square, double

class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2), 4) # test when 2 is given as input, the output is 4
        self.assertEqual(square(3.0), 9.0) # test when 3.0 is given as input, the output is 9.0
        self.assertEqual(square(-3), -9) # test when -3 is given as input, the output is -9

class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2), 4) # test when input is 2, output is 4
        self.assertEqual(double(-3.1), -6.2) # test when input is -3.1, output is -6.2
        self.assertEqual(double(0), 0) # test when input is 0, output is 0

unittest.main()
