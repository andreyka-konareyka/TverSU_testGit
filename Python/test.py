import unittest
from main import is_prime


class TestPrime(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_prime(1), True)

    def test2(self):
        self.assertEqual(is_prime(2), True)

    def test3(self):
        self.assertEqual(is_prime(3), True)

    def test4(self):
        self.assertEqual(is_prime(4), False)

    def test5(self):
        self.assertEqual(is_prime(5), True)

    def test6(self):
        self.assertEqual(is_prime(6), False)

    def test7(self):
        self.assertEqual(is_prime(7), True)

    def test8(self):
        self.assertEqual(is_prime(8), False)

    def test9(self):
        self.assertEqual(is_prime(9), False)

    def test10(self):
        self.assertEqual(is_prime(10), False)

    def test11(self):
        self.assertEqual(is_prime(11), True)

    def test12(self):
        self.assertEqual(is_prime(12), False)

    def test13(self):
        self.assertEqual(is_prime(13), True)


if __name__ == "__main__":
    unittest.main()
