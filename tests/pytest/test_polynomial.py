import pytest

from src import Polynomial


def test_init():
    f = Polynomial([3, 2, 1])
    assert f.coefficients == [3, 2, 1]


def test_eq():
    f = Polynomial([3, 2, 1])
    g = Polynomial([3, 2, 1])
    assert f == g


def test_add():
    f = Polynomial([3, 2, 1])
    g = Polynomial([1, 2, 3])
    f_plus_g = Polynomial([4, 4, 4])
    assert f+g == f_plus_g


def test_add_different_degrees():
    f = Polynomial([0, 0, 1])
    g = Polynomial([1])
    f_plus_g = Polynomial([1, 0, 1])
    assert f+g == f_plus_g
    assert g+f == f_plus_g


def test_add_reduce_degree():
    f = Polynomial([1, 1])
    g = Polynomial([1, -1])
    f_plus_g = Polynomial([2])
    assert f+g == f_plus_g


def test_minus():
    f = Polynomial([3, 2, 1])
    g = Polynomial([1, 2, 3])
    negative_g = Polynomial([-1, -2, -3])
    assert f-g == f+negative_g


def test_mul_int():
    f = Polynomial([3, 2, 1])
    f_times_3 = Polynomial([9, 6, 3])
    assert f*3 == f_times_3


def test_mul_polynomial():
    f = Polynomial([-1, 1])
    g = Polynomial([1, 1, 1])
    f_times_g = Polynomial([-1, 0, 0, 1])
    assert f*g == f_times_g


def test_mul_invalid():
    f = Polynomial([3, 2, 1])
    with pytest.raises(ValueError):
        f * "a string"


def test_empty_polynomial():
    f = Polynomial([])
    assert str(f) == ""


def test_positive_constant_polynomial():
    f = Polynomial([1])
    assert str(f) == "1"


def test_negative_constant_polynomial():
    f = Polynomial([-1])
    assert str(f) == "- 1"


def test_zero_polynomial():
    f = Polynomial([0])
    assert str(f) == "0"


def test_binomial():
    f = Polynomial([1, 1])
    assert str(f) == "x + 1"


def test_cyclotomic_polynomial():
    f = Polynomial([1, 1, 1, 1, 1])
    assert str(f) == "x^4 + x^3 + x^2 + x + 1"


def test_large_monomial():
    f = Polynomial([0, 0, 0, 0, 4])
    assert str(f) == "4x^4"


def test_negative_polynomial_coefficient():
    f = Polynomial([-4, -3, -2, -1])
    assert str(f) == "- x^3 - 2x^2 - 3x - 4"
