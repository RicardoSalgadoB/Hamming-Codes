class Matrix:
    def __init__(self, vals):
        for i in range(1, len(vals)):
            if len(vals[i-1]) != len(vals[i]):
                raise "Matrix shape must be consistent"
        self.vals = [[]]
        if isinstance(vals, list) and isinstance(vals[0], list):
            self.vals = vals
        else:
            raise "Matrix over Z2"
        self.h = len(self.vals)
        self.w = len(self.vals[0])

    def __add__(self, other):
        if self.h != other.h or self.w != other.w:
            raise "Matrices mut have same shape"
        new = [[l+r for l,r in zip(self.vals[row_i], other.vals[row_i])] for row_i in range(self.h)]
        return Matrix(new)

    def __radd__(self, other):
        if self.h != other.h or self.w != other.w:
            raise "Matrices mut have same shape"
        new = [[l+r for l,r in zip(other.vals[row_i], self.vals[row_i])] for row_i in range(self.h)]
        return Matrix(new)

    def __rmul__(self, other):
        if not isinstance(other, VectorZ2):
            raise "ERROR"

        if self.h != other.n:
            return "Shape mismatch"

        new = [[0 for i in range(self.w)]]
        for k in range(self.w):
            for r in range(other.n):
                new[0][k] = new[0][k] + (other.vals[r] * self.vals[r][k])
        return Matrix(new)

    def __str__(self):
        retS = ""
        for row in self.vals:
            for e in row:
                retS += str(e) + ", "
            retS += "\n"
        return retS

    def __repr__(self):
        retS = ""
        for row in self.vals:
            for e in row:
                retS += str(e) + ", "
            retS += "\n"
        return retS

    def item(self):
        if len(self.vals) == 1 and len(self.vals[0]) == 1:
            return self.vals[0][0]
