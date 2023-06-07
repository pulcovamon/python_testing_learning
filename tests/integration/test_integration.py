'''
I don't use any data and I don't have any App.
'''

import unittest

class TestBasic(unittest.TestCase):
    def setUp(self):
        '''
        Method for loading the test data from a fixture file
        and execute many tests against that data set.

        It cannot be executed, because I don't have any App,
        I am just learning, how to do it, if I had some App.
        '''
        self.app = App(database='fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer.name, 'Org XYZ')
        self.assertEqual(customer.asress, '10 Red Road, Reading')


class TestComplexData(unittest.TestCase):
    def setUp(self):
        '''
        Method for loading the test data from a fixture file
        and execute many tests against that data set.        
        '''
        self.app = App(database='fixtures/test_complex.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10000)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=9999)
        self.assertEqual(customer.name, u"バナナ")
        self.assertEqual(customer.adress, '10 Red Road, Akihabara, Tokyo')


if __name__ == '__main__':
    unittest.main()
