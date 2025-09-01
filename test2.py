from gf2 import GF2
import numpy as np

a = GF2([[1, 1, 1, 0]])
b = GF2([[0, 0], [1, 0], [0, 1], [1, 1]])
c = np.array([[1], [2]])

print((a @ b) @ c)
