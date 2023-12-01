
"""
performing a unit test so we import the unittest module

"""
import unittest

from mymodule import square,double

class TestSquare(unittest.TestCase):
    """
    creating a class
    """
    def test1(self):
        """
        coming up with a function that performs the testing
        
        """

        self.assertEqual(square(2), 4)
        self.assertEqual(square(3.0), 9.0)
        self.assertNotEqual(square(-3), -9)

class TestDouble(unittest.TestCase):
    """
    Creating class for Double
     
    """
    def test1(self):
        """
        creating a function to perform the testing for the double function 
        created in mymodule.py
        """
        self.assertEqual(double(2), 4)
        self.assertEqual(double(3.1), 6.2)
        self.assertNotEqual(double(-6), 9)
        self.assertEqual(double(-6), -12)

unittest.main()