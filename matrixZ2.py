from Z2 import Z2
from vectorZ2 import VectorZ2
from matrix import Matrix

class MatrixZ2 (Matrix):
    def __init__(self, vals):
        for i in range(1, len(vals)):
            if len(vals[i-1]) != len(vals[i]):
                raise "Matrix shape must be consistent"
        self.data = [[]]
        if isinstance(vals, list) and isinstance(vals[0], list):
            if isinstance(vals[0][0], Z2):
                self.data = vals
            else:
                self.data = [[Z2(v) for v in vals[row_i]] for row_i in range(len(vals))]
        else:
            raise "Matrix over Z2"
        self.h = len(self.data)
        self.w = len(self.data[0])

    def __add__(self, other):
        new = super().__add__(self, other)
        return MatrixZ2(new.vals)

    def __radd__(self, other):
        new = super().__radd__(self, other)
        return MatrixZ2(new)

#    def __mul__(self, other):
#        if self.w != other.h:
#            return "Shape mismatch"
#
#        new = [[Z2(0) for j in range(other.w)] for i in range(self.h)]
#        for j in range(self.h):
#            for k in range(other.w):
#                for r in range(self.w):
#                    new[j][k] = new[j][k] + (self.data[j][r] * other.data[r][k])
#        return MatrixZ2(new)

    def __rmul__(self, other):
        if not isinstance(other, VectorZ2):
            raise "ERROR"

        if self.h != other.n:
            return "Shape mismatch"

        new = [[Z2(0) for i in range(self.w)]]
        for k in range(self.w):
            for r in range(other.n):
                new[0][k] = new[0][k] + (other.data[r] * self.data[r][k])
        return MatrixZ2(new)
