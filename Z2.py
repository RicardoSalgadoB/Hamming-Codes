
class Z2:
    def __init__(self, n: int):
        self.n = n % 2

    def __add__(self, other):
        if isinstance(other, Z2):
            return Z2(self.n ^ other.n)
        return Z2(self.n + other)

    def __radd__(self, other):
        if isinstance(other, Z2):
            return other + self
        return Z2(self.n + other)

    def __mul__(self, other):
        if isinstance(other, Z2):
            return Z2(self.n & other.n)
        return Z2(self.n * other)

    def __rmul__(self, other):
        if isinstance(other, Z2):
            return Z2(self.n & other.n)
        return Z2(self.n * other)

    def __neg__(self):
        return self

    def __sub__(self, other):
        return self + other

    def __rsub__(self, other):
        return other + self

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return repr(self.n)

