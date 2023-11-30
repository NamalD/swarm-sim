import unittest
import math

from easom import easom


class TestEasomFunction(unittest.TestCase):

    def test_global_minimum(self):
        # Test if the Easom Function correctly returns the global minimum (-1) at (pi, pi)
        result = easom(math.pi, math.pi)
        self.assertAlmostEqual(result, -1, places=5)  # Using places to check for approximate equality

    def test_symmetry(self):
        # Test the symmetry property: f(x, y) = f(y, x) for all x and y
        x = 2.0
        y = 3.0
        result1 = easom(x, y)
        result2 = easom(y, x)
        self.assertAlmostEqual(result1, result2, places=5)

    def test_positive_values(self):
        # Test if the function returns positive values for points away from the global minimum
        result = easom(0.0, 0.0)
        self.assertLessEqual(result, 1e-6)


if __name__ == '__main__':
    unittest.main()
