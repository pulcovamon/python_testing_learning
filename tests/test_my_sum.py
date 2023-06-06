'''
Learnign testing using this tutorial:
https://realpython.com/python-testing/
'''

import unittest
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

if __name__ == '__main__':
    unittest.main()