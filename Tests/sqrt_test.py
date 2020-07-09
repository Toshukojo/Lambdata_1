# import the unit test package and the functions we want to test

import unittest
from sqrt import newton_sqrt, newton_sqrt2, lazy_sqrt, squared

class sqrtTests(unittest.TestCase):
    """obligatory doc string, test square root functions!~~~~"""   
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)
        
    def test_sqrt2(self):
        self.assertAlmostEqual(lazy_sqrt(2)**2, 2)
        
if __name__ == '__main__':
    unittest.main()

