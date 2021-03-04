import unittest
import func


class FuncTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(func.add(3, 2), 5)
        self.assertEqual(func.add(9, 8), 17)
        self.assertEqual(func.add(6, -6), 0)

    def test_subtraction(self):
        self.assertEqual(func.subtract(4, 2), 2)
        self.assertEqual(func.subtract(10, 0), 10)
        self.assertEqual(func.subtract(-2, 2), -4)
        self.assertEqual(func.subtract(2, -2), 4)
        self.assertEqual(func.subtract(2, 2), 0)

    def test_multiplication(self):
        self.assertEqual(func.multiply(3, 2), 6)
        self.assertEqual(func.multiply(3, 3), 9)
        self.assertEqual(func.multiply(3, 0), 0)
        self.assertEqual(func.multiply(3, -2), -6)

    def test_power(self):
        self.assertEqual(func.power(3, 2), 9)
        self.assertEqual(func.power(3, 0), 1)
        self.assertEqual(func.power(1, 4), 1)
        self.assertEqual(func.power(0, 2), 0)
        self.assertEqual(func.power(0, 0), 1)

    def test_division(self):
        self.assertEqual(func.divide(3, 1), 3)
        self.assertEqual(func.divide(3, 3), 1)
        self.assertEqual(func.divide(3, -3), -1)
        self.assertEqual(func.divide(-3, -3), 1)

    def test_is_even(self):
        self.assertTrue(func.is_even(2))
        self.assertFalse(func.is_even(5))

    def test_fibonacci(self):
        self.assertEqual(func.fibonacci(1), 1)

if __name__ == '__main__':
    unittest.main()