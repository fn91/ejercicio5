import unittest

from operaciones import suma
from operaciones import resta
from operaciones import multi
from operaciones import division

class TestMatematico(unittest.TestCase):


    def test_operaciones(self):
       
        self.assertEqual(suma(3, 2),5) 
        self.assertEqual(suma(-1, 1),0) 
        self.assertEqual(suma(-1, -1),2)
        self.assertEqual(resta(-1, -99)-100)
        self.assertEqual(resta(99, 1),98)
        self.assertEqual(multi(1, 10),10)
        self.assertAlmostEqual(division(12,0),0)
        


    if __name__=="__main__":
        unittest.main()