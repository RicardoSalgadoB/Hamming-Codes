from gf2 import GF2
import numpy as np

def getBin(n, l):
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
    l = int(np.log2(n))     # Max number of digits in the binary representation of indexes
    bin = [getBin(i, l) for i in range(n)]
    real = [[2**i] for i in range(l)]
    return GF2(bin), np.array(real)     # Gets lists into arrays

def hamm(msg):
    """Allows checking if a message has been altered according to Hamming codes.

    Args:
        msg (List[int]): A list of 0s and 1s containing the 'message' that is being transmitted.

    Raises:
        ValueError: Raised if the length of the message is not a power of 2.

    Returns:
        int: index that indicates the position where the message has been altered.
    """
    msg = GF2([msg])        # Transform the message into a GF2 matrix
    if msg.size not in [2**i for i in range(100)]:
        raise ValueError("Length of message must be a power of 2")
    m1, m2 = create_helper_matrices(msg.size)
    res_m = np.matmul(msg, m1) @ m2   # Index inside an array
    return res_m.item()     # Index as a stand alone integer
