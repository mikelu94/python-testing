"""Module for Polynomials."""
from collections.abc import Sequence
from numbers import Number
from typing import Union


class Polynomial:
    """Polynomial class."""

    def __init__(self, coefficients: Sequence[Number]) -> None:
        """Polynomial constructor."""
        self.coefficients = coefficients

    def __eq__(self, other: object) -> bool:
        """Polynomial equality comparison operator."""
        if isinstance(other, type(self)):
            return self.coefficients == other.coefficients
        return False

    def __add__(self, other: "Polynomial") -> "Polynomial":
        """Polynomial addition operator."""
        self_degree = len(self.coefficients)
        other_degree = len(other.coefficients)
        sum_coefficients = [0 for _ in range(max(self_degree, other_degree))]
        for i in range(max(self_degree, other_degree)):
            if i < self_degree:
                sum_coefficients[i] += self.coefficients[i]
            if i < other_degree:
                sum_coefficients[i] += other.coefficients[i]
        while len(sum_coefficients) > 1 and sum_coefficients[-1] == 0:
            sum_coefficients.pop()
        return Polynomial(coefficients=sum_coefficients)

    def __sub__(self, other: "Polynomial") -> "Polynomial":
        """Polynomial subtraction operator."""
        return self.__add__(other * -1)

    def __mul__(self, other: Union["Polynomial", Number]) -> "Polynomial":
        """Polynomial multiplication operator."""
        if isinstance(other, int):
            return Polynomial(coefficients=[c*other for c in self.coefficients])
        if isinstance(other, Polynomial):
            self_degree = len(self.coefficients)
            other_degree = len(other.coefficients)
            product_coefficients = [0 for _ in range(self_degree+other_degree-1)]
            for i in range(self_degree):
                for j in range(other_degree):
                    product_coefficients[i+j] += self.coefficients[i] * other.coefficients[j]
            return Polynomial(coefficients=product_coefficients)
        raise ValueError(f"Expected an int or {type(self)}")

    def _ith_monomial(self, i: int) -> str:
        """Polynomial private method for getting its ith monomial."""
        ith_coefficient = self.coefficients[i]

        if i == 0:
            if ith_coefficient > 0:
                return str(ith_coefficient)
            if ith_coefficient < 0:
                return f"- {abs(ith_coefficient)}"
            if len(self.coefficients) == 1:
                return "0"

        if ith_coefficient == 0:
            return ""

        ith_coefficient_str = ""
        if ith_coefficient == -1:
            ith_coefficient_str = "- "
        elif ith_coefficient < 0:
            ith_coefficient_str = f"- {abs(ith_coefficient)}"
        elif ith_coefficient > 1:
            ith_coefficient_str = str(ith_coefficient)

        exponent_str = f"^{i}" if i != 1 else ""
        return f"{ith_coefficient_str}x{exponent_str}"

    def __str__(self) -> str:
        """Polynomial string representation."""
        monomials = list(filter(len, map(self._ith_monomial, range(len(self.coefficients)-1, -1, -1))))
        polynomial_str = ""
        if not monomials:
            return polynomial_str
        polynomial_str = monomials[0]
        for monomial in monomials[1:]:
            if monomial[0] == "-":
                polynomial_str += f" {monomial}"
            else:
                polynomial_str += f" + {monomial}"
        return polynomial_str
