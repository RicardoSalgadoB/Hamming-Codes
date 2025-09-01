from utils import hamm
from random import randint

if __name__ == "__main__":
    msg = [0 for i in range(16)]

    res1 = hamm(msg)
    print(f"This is the original message: {msg}")
    print(f"Error detected in position: {res1}")

    n = randint(0, 15)
    msg[n] = int(not msg[n])
    res2 = hamm(msg)
    print(f"Oh no!!! The message has been altered, but where? {msg}")
    print(f"Error detected in position: {res2}")

    print("Oh... Thanks Hamming")
