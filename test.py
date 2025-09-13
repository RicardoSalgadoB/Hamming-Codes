""" Function to perform unit tests with pytest. """

import copy

from random import randint, choice
from utils import hamm, encode, decode
from gf2 import GF2

def test_gf2_addition():
    assert GF2([0]) + GF2([0]) == GF2([0])
    assert GF2([1]) + GF2([0]) == GF2([1])
    assert GF2([0]) + GF2([1]) == GF2([1])
    assert GF2([1]) + GF2([1]) == GF2([0])
    
    
def test_gf2_multiplication():
    assert GF2([0]) * GF2([0]) == GF2([0])
    assert GF2([1]) * GF2([0]) == GF2([0])
    assert GF2([0]) * GF2([1]) == GF2([0])
    assert GF2([1]) * GF2([1]) == GF2([1])

  
def test_gf2_additive_conmutativity():
    assert GF2([0]) + GF2([0]) == GF2([0]) + GF2([0])
    assert GF2([1]) + GF2([0]) == GF2([0]) + GF2([1])
    assert GF2([1]) + GF2([1]) == GF2([1]) + GF2([1])

  
def test_gf2_multiplicative_conmutativity():
    assert GF2([0]) * GF2([0]) == GF2([0]) * GF2([0])
    assert GF2([1]) * GF2([0]) == GF2([0]) * GF2([1])
    assert GF2([1]) * GF2([1]) == GF2([1]) * GF2([1])


def test_gf2_additive_associativity():
    assert GF2([0]) + (GF2([0]) + GF2([0])) == (GF2([0]) + GF2([0])) + GF2([0])
    assert GF2([1]) + (GF2([0]) + GF2([0])) == (GF2([1]) + GF2([0])) + GF2([0])
    assert GF2([0]) + (GF2([1]) + GF2([0])) == (GF2([0]) + GF2([1])) + GF2([0])
    assert GF2([1]) + (GF2([1]) + GF2([0])) == (GF2([1]) + GF2([1])) + GF2([0])
    assert GF2([0]) + (GF2([0]) + GF2([1])) == (GF2([0]) + GF2([0])) + GF2([1])
    assert GF2([1]) + (GF2([0]) + GF2([1])) == (GF2([1]) + GF2([0])) + GF2([1])
    assert GF2([0]) + (GF2([1]) + GF2([1])) == (GF2([0]) + GF2([1])) + GF2([1])
    assert GF2([1]) + (GF2([1]) + GF2([1])) == (GF2([1]) + GF2([1])) + GF2([1])


def test_gf2_multiplicative_associativity():
    assert GF2([0]) * (GF2([0]) * GF2([0])) == (GF2([0]) * GF2([0])) * GF2([0])
    assert GF2([1]) * (GF2([0]) * GF2([0])) == (GF2([1]) * GF2([0])) * GF2([0])
    assert GF2([0]) * (GF2([1]) * GF2([0])) == (GF2([0]) * GF2([1])) * GF2([0])
    assert GF2([1]) * (GF2([1]) * GF2([0])) == (GF2([1]) * GF2([1])) * GF2([0])
    assert GF2([0]) * (GF2([0]) * GF2([1])) == (GF2([0]) * GF2([0])) * GF2([1])
    assert GF2([1]) * (GF2([0]) * GF2([1])) == (GF2([1]) * GF2([0])) * GF2([1])
    assert GF2([0]) * (GF2([1]) * GF2([1])) == (GF2([0]) * GF2([1])) * GF2([1])
    assert GF2([1]) * (GF2([1]) * GF2([1])) == (GF2([1]) * GF2([1])) * GF2([1])

   
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
    
def test_encode():
    # Generate message
    length = randint(1, 1000)
    msg = [choice([0, 1]) for i in range(length)]
    
    # Encode message
    encoded_msg = encode(msg)
    
    # Decode encoded message
    decoded_msg = decode(encoded_msg)
    
    # Assert
    assert decoded_msg == msg