from typing import List
import numpy as np

from gf2 import GF2

def getBin(n, l) -> List[int]:
    """Gets the binary representation of a number n with l digits

    Returns:
        A list of 0s and 1s with the binary representation
    """
    ret = []
    for _ in range(l):
        ret.append(n % 2)
        n //= 2
    return ret

def create_helper_matrices(n: int):
    """Create helper matrices to perform the Hamming parity checks.

    Args:
        n (int): Size of the message being sent, must be a power of 2.

    Returns:
        GF2: Matrix with the binary representation of 0 and each positive integer in each row.
        np.array: Matrix with [[1], ..., [l]], l is the log_2 of n
    """
    l = np.ceil(np.log2(n)).astype(int)    # Max number of digits in the binary representation of indexes
    bin = [getBin(i, l) for i in range(n)]
    real = [[2**i] for i in range(l)]
    return GF2(bin), np.array(real)     # Gets lists into arrays

def hamm(msg) -> int:
    """Allows checking if a message has been altered according to Hamming codes.

    Args:
        msg (List[int]): A list of 0s and 1s containing the 'message' that is being transmitted.

    Returns:
        int: index that indicates the position where the message has been altered, 0 if it hasn't.
    """
    msg = GF2([msg])        # Transform the message into a GF2 matrix
    #if msg.size not in [2**i for i in range(100)]:
    #    raise ValueError("Length of message must be a power of 2")
    bin, integers = create_helper_matrices(msg.size)
    res_m = (msg @ bin) @ integers  # Index inside an array
    return res_m.item()             # Index as a stand alone integer


def encode(prev) -> List[int]:
    """Encodes a message with parity elements in a fshion that allows for Hamming code correction

    Args:
        msg (List[int]): A list of 0s and 1s representing the message to be encoded

    Returns:
        List[int]: The encoded message with the necessary parity checks
    """
    msg = prev.copy()   # Crear copia
    parities = [0]
    msg.insert(0, 0)
    i = 1
    while len(msg) > i:
        parities.append(i)
        msg.insert(i, 0)
        i *= 2

    binary_activations = []
    for i in range(len(msg)):
        activations = []
        if i == 0:
            activations = [0 for j in range(len(msg))]
        elif i in parities:
            for j in range(len(msg)):
                activations += [1] if i&j == i else [0]
        else:
            activations = [0 for j in range(len(msg))]
            activations[i] = 1
        binary_activations.append(activations)
    
    bin_act = GF2(binary_activations).transpose()
    msg = GF2([msg])
    
    return (msg @ bin_act).astype(int).tolist()[0]


def decode(encoded_msg) -> List[int]:
    """Decodes a message. It removes its parity bits

    Args:
        encoded_msg (List[int]): The encoded message

    Returns:
        List[int]: The decoded message, no more parity bits
    """
    msg = encoded_msg.copy()    # Crear copia
    msg.pop(0)
    i = 0
    while 2**i-i < len(msg):
        msg.pop(2**i-i-1)
        i += 1
    return msg