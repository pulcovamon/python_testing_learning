'''
Learnign testing using this tutorial:
https://realpython.com/python-testing/
'''

import unittest
from fractions import Fraction
from program.my_sum import sum_of_mine

class TestSum(unittest.TestCase):
    def test_list_int(self):
        '''
        Test if it can sum integers
        '''
        # 1. create inputs
        data = [1, 2, 3]
        # 2. execute the code
        result = sum_of_mine(data)
        # 3. compare the output with an expected output
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        '''
        Test is it can sum fractions
        '''
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum_of_mine(data)
        self.assertEqual(result, Fraction(9, 10))

    def test_bad_type(self):
        '''
        Test if it fails with bad input
        '''
        data = 'banana'
        with self.assertRaises(TypeError):
            result = sum_of_mine(data)

if __name__ == '__main__':
    unittest.main() # command line entry point