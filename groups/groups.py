from numbers import Integral


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

    
class CyclicGroup:
    def __init__(self, order):
        self.order = order

    def _validate(self, value):
        if not isinstance(value, Integral):
            raise TypeError(f"Value must be an integer, not a {type(value).__name__}")
            
        elif not 0 <= value < self.order:
            raise ValueError(f"Value must be an integer in the range [0, {self.order}) ")

    def operation (self, a, b):
        return (a + b) % self.order

    def __call__(self, value):
        return Element(self, value)

    def __str__(self):
        return f"Z/{self.order}Z"

    def __repr__(self):
        return f"{type(self).__name__}({self.value})"
    