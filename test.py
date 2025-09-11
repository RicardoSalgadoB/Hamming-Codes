""" Function to perform unit tests with pytest. """

from random import randint, choice
from utils import hamm, encode

def test_hamm():
    msg = [0 for i in range(512)]

    n = randint(0, 511)
    msg[n] = int(not msg[n])
    res2 = hamm(msg)
    
    assert res2 == n
    
    
def test_full():
    # Generate message
    length = randint(1, 1000)
    msg = [choice([0, 1]) for i in range(length)]
    
    # Encode message
    encoded_msg = encode(msg)
    n = randint(0, len(encoded_msg)-1)
    encoded_msg[n] = int(not encoded_msg[n])
    
    # Hamm
    res2 = hamm(encoded_msg)
    
    # Assert
    assert res2 == n
    
    
def test_nothing():
    # Generate message
    length = randint(1, 1000)
    msg = [choice([0, 1]) for i in range(length)]
    
    # Encode message
    encoded_msg = encode(msg)
    
    # Hamm
    res2 = hamm(encoded_msg)

    # Assert
    assert res2 == 0
    