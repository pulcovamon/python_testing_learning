'''
Learning testing using this tutorial:
https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/
'''

import unittest
from program.formatting_name import formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        result = formatted_name('triss', 'merigold')
        self.assertEqual(result, 'Triss Merigold')

    def test_middle_name(self):
        result = formatted_name('cirilla', 'riannon', 'fiona elen')
        self.assertEqual(result, 'Cirilla Fiona Elen Riannon')