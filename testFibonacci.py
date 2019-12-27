import unittest
from fibonacci import fib


class TestFibonacciNumbers(unittest.TestCase):
    def testItStartFromZero(self):
        self.assertEqual(0, fib(0))

    def testItFirstFiveNumbers(self):
        for n, fib_n in (1, 1), (2, 1), (3, 2), (4, 3), (5, 5):
            with self.subTest(i=n):
                self.assertEqual(fib_n, fib(n))

    def testBigNumber(self):
        self.assertEqual(55, fib(10))

    def testIfNegativeThenRaiseExep(self):
        with self.subTest(i=1):
            self.assertRaises(ArithmeticError, fib, -1)
        with self.subTest(i=2):
            self.assertRaises(ArithmeticError, fib, -10)

    def test_fractionfl(self):
        self.assertRaises(ArithmeticError, fib, 3.4)

if __name__ == '__main__':
    unittest.main()
