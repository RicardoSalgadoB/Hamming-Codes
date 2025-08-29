from typing import List

from vectorZ2 import VectorZ2
from matrixZ2 import MatrixZ2
from matrixReal import MatrixZ2ToReal
from math import log2

def getBin(n, l):
    ret = []
    for i in range(l):
        ret.append(n % 2)
        n //= 2
    return ret

def create_helper_mat(n: int):
    l = int(log2(n))
    bin = [getBin(i, l) for i in range(n)]
    real = [[2**i] for i in range(l)]
    return MatrixZ2(bin), MatrixZ2ToReal(real)

def hamm(msg: List[int]):
    msg = VectorZ2(msg)
    if msg.n not in [2**i for i in range(100)]:
        raise "Length of message must be a power of 2"
    m1, m2 = create_helper_mat(msg.n)
    res_m = msg*m1*m2
    return res_m.item()
