import unittest

from src import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_init(self):
        f = Polynomial([3, 2, 1])
        self.assertEquals(f.coefficients, [3, 2, 1])

    def test_eq(self):
        f = Polynomial([3, 2, 1])
        g = Polynomial([3, 2, 1])
        self.assertEquals(f, g)

    def test_add(self):
        f = Polynomial([3, 2, 1])
        g = Polynomial([1, 2, 3])
        f_plus_g = Polynomial([4, 4, 4])
        self.assertEquals(f+g, f_plus_g)

    def test_add_different_degrees(self):
        f = Polynomial([0, 0, 1])
        g = Polynomial([1])
        f_plus_g = Polynomial([1, 0, 1])
        self.assertEquals(f+g, f_plus_g)
        self.assertEquals(g+f, f_plus_g)

    def test_add_reduce_degree(self):
        f = Polynomial([1, 1])
        g = Polynomial([1, -1])
        f_plus_g = Polynomial([2])
        self.assertEquals(f+g, f_plus_g)

    def test_minus(self):
        f = Polynomial([3, 2, 1])
        g = Polynomial([1, 2, 3])
        negative_g = Polynomial([-1, -2, -3])
        self.assertEquals(f-g, f+negative_g)

    def test_mul_int(self):
        f = Polynomial([3, 2, 1])
        f_times_3 = Polynomial([9, 6, 3])
        self.assertEquals(f*3, f_times_3)

    def test_mul_polynomial(self):
        f = Polynomial([-1, 1])
        g = Polynomial([1, 1, 1])
        f_times_g = Polynomial([-1, 0, 0, 1])
        self.assertEquals(f*g, f_times_g)

    def test_mul_invalid(self):
        f = Polynomial([3, 2, 1])
        with self.assertRaises(ValueError):
            f * "a string"

    def test_empty_polynomial(self):
        f = Polynomial([])
        self.assertEquals(str(f), "")

    def test_positive_constant_polynomial(self):
        f = Polynomial([1])
        self.assertEquals(str(f), "1")

    def test_negative_constant_polynomial(self):
        f = Polynomial([-1])
        self.assertEquals(str(f), "- 1")

    def test_zero_polynomial(self):
        f = Polynomial([0])
        self.assertEquals(str(f), "0")

    def test_binomial(self):
        f = Polynomial([1, 1])
        self.assertEquals(str(f), "x + 1")

    def test_cyclotomic_polynomial(self):
        f = Polynomial([1, 1, 1, 1, 1])
        self.assertEquals(str(f), "x^4 + x^3 + x^2 + x + 1")

    def test_large_monomial(self):
        f = Polynomial([0, 0, 0, 0, 4])
        self.assertEquals(str(f), "4x^4")

    def test_negative_polynomial_coefficient(self):
        f = Polynomial([-4, -3, -2, -1])
        self.assertEquals(str(f), "- x^3 - 2x^2 - 3x - 4")
