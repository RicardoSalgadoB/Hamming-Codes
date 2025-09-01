from matrixZ2 import MatrixZ2
from matrix import Matrix

class MatrixZ2ToReal(Matrix):
    def __init__(self, vals):
        super().__init__(vals)

    def __rmul__(self, other):
        if not isinstance(other, MatrixZ2):
            raise "Only transforms Z2 matices"

        new = [[0 for j in range(self.w)] for i in range(other.h)]
        for j in range(other.h):
            for k in range(self.w):
                for r in range(other.w):
                    new[j][k] = new[j][k] + (other.data[j][r].n * self.data[r][k])
        return Matrix(new)
