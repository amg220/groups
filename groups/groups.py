from numbers import Integral
import numpy as np
from numpy.linalg import det


class Element:
    def __init__(self, group, value):
        group._validate(value)
        self.group = group
        self.value = value

    def __mul__(self, other):
        return Element(
            self.group,
            self.group.operation(self.value, other.value)
        )

    def __str__(self):
        return f"{self.value}_{self.group}"

    def __repr__(self):
        return f"{type(self).__name__}({self.group}, {self.value})"


class Group:
    def __init__(self, n):
        self.n = n

    def __call__(self, value):
        return Element(self, value)

    def __repr__(self):
        return f"{type(self).__name__}({self.n})"

    def __str__(self):
        return f"{self.symbol}{self.n}"


class CyclicGroup(Group):
    symbol = 'Z'

    def _validate(self, value):
        if not isinstance(value, Integral):
            raise TypeError(f"Value must be an integer,"
                            f" not a {type(value).__name__}")

        elif not 0 <= value < self.n:
            raise ValueError(f"Value must be an integer in the"
                             f"range [0, {self.n}) ")

    def operation(self, a, b):
        return (a + b) % self.n


class GeneralLinearGroup(Group):
    symbol = "GL"

    def _validate(self, value):
        if not isinstance(value, np.ndarray):
            raise TypeError(f"Value must be an array,"
                            f" not a {type(value).__name__}")

        elif not value.shape == (self.n, self.n):
            raise ValueError(f"Value must be an {self.n}x{self.n} matrix")

        elif det(value) == 0:
            raise ValueError("Matrix has to be invertible")

    def operation(self, a, b):
        return a @ b
