from typing import List

from vectorZ2 import VectorZ2
from matrixZ2 import MatrixZ2
from matrixReal import MatrixZ2ToReal
from math import log2

from gf2 import GF2
import numpy as np

def getBin(n, l):
    ret = []
    for _ in range(l):
        ret.append(n % 2)
        n //= 2
    return ret

def create_helper_mat(n: int):
    l = int(log2(n))
    bin = [getBin(i, l) for i in range(n)]
    real = [[2**i] for i in range(l)]
    return GF2(bin), np.array(real)

def hamm(msg):
    msg = GF2([msg])
    if msg.size not in [2**i for i in range(100)]:
        raise ValueError("Length of message must be a power of 2")
    m1, m2 = create_helper_mat(msg.size)
    res_m = msg @ m1 @ m2
    return res_m.item()
