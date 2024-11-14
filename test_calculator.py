import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 2),1)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-1, 2), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-3, 7), -21)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2)
        self.assertRaises(ValueError, self.calc.divide, 5, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(10, 5), 0)
        self.assertEqual(self.calc.modulo(5, 10), 5)
        self.assertRaises(ValueError, self.calc.modulo, 5, 0)

if __name__ == '__main__':
    unittest.main()