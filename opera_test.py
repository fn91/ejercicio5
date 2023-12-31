import unittest

from operaciones import suma
from operaciones import resta
from operaciones import multi
from operaciones import division

class TestMatematico(unittest.TestCase):


    def test_operaciones(self):
       
        self.assertEqual(suma(3, 2),5) 
        self.assertEqual(suma(-1, 1),0) 
        self.assertEqual(suma(-1, -1), -2)
        self.assertNotEqual(resta(-100, -50),-150)
        self.assertEqual(resta(99, 1),98)
        self.assertEqual(multi(10, 10),100)
        self.assertAlmostEqual(multi(10,5),50)
        self.assertAlmostEqual(division(10,2),5)
        self.assertNotAlmostEqual(division(100,10),1)

    if __name__=="__main__":
        unittest.main()