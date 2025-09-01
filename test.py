"""Function to perform unit tests with pytest"""

from random import randint
from utils import hamm

def test_hamm():
    msg = [0 for i in range(512)]

    n = randint(0, 511)
    msg[n] = int(not msg[n])
    res2 = hamm(msg)
    
    assert res2 == n