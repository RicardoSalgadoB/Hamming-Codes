from Z2 import Z2

class VectorZ2:
    def __init__(self, vals):
        self.data = []
        if isinstance(vals, Z2):
            self.data = [vals]
        elif isinstance(vals, list) and isinstance(vals[0], Z2):
            self.data = [vals]
        elif isinstance(vals, list) and isinstance(vals[0], int):
            self.data = [Z2(v) for v in vals]
        else:
            raise "Vector over Z2"
        self.n = len(self.data)

    def __add__(self, other):
        if self.n != other.n:
            raise "Vectors are not the same size"
        new = [l+r for l, r in zip(self.data, other.data)]
        return VectorZ2(new)

    def __radd__(self, other):
        if self.n != other.n:
            raise "Vectors are not the same size"
        new = [l+r for l, r in zip(other.data, self.data)]
        return VectorZ2(new)

    def __rmul__(self, λ):
        if not (isinstance(λ, int) or isinstance(λ, float)):
            raise "λ must be integer or float"
        new = [Z2(λ)*e for e in self.data]
        return VectorZ2(new)

    def __neg__(self):
        return self

    def __str__(self):
        retS = ""
        for v in self.data:
            retS += str(v) + ", "
        return retS

    def __repr__(self):
        retS = ""
        for v in self.data:
            retS += str(v) + ", "
        return retS
