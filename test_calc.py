import unittest
from unittest import result
import calc


class sumtest(unittest.TestCase):
    def test_Sum(self):
        result = calc.sum(3, 5)
        self.assertEquals(8, result)

    def test_minus(self):
        self.assertEquals(5, calc.minus(10, 5))
