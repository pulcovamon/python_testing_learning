# without any test runner or with pytest

def test_sum_list():
    assert sum([1, 2, 3]) == 6

def test_sum_tuple():
    assert sum((1, 1, 1)) == 3

# with unittest

import unittest

class TestSum(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum([1, 2, 3]), 6)

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 1, 1)), 3)


if __name__ == '__main__':
    # without any test runner
    test_sum_list()
    test_sum_tuple()
    print('Everything passed')

    # with unittest
    unittest.main()