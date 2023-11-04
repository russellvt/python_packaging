'''
Simple Test Example (placeholder)
'''

import unittest

from packaging_geekoncall.example import add_one


class TestSimple(unittest.TestCase):
    '''Simple Example Tests'''

    def test_add_one(self):
        '''Test add_one Example'''
        self.assertEqual(add_one(5), 6)


if __name__ == '__main__':
    unittest.main()
