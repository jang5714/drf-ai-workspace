import unittest
from admin.sorting.models_oop import Calculator

class TestOop(unittest.TestCase):
    def test_calculator(self):
        cal = Calculator()
        cal.num1 = 5
        cal.num2 = 8

        self.assertEqual(cal.divice(), 1.0)
        self.assertEqual(cal.add(), 13)
        self.assertEqual(cal.mulitple(), 8)
        self.assertEqual(cal.subtract(), -3)


if __name__ == '__main__':
    unittest.main()
