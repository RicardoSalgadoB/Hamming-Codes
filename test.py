from utils import hamm

if __name__ == "__main__":
    msg = [1, 1, 1, 1,
           1, 0, 1, 0,
           1, 1, 1, 1,
           1, 0, 1, 0]

    res1 = hamm(msg)
    print(f"This is the original message: {msg}")
    print(f"Error detected in position: {res1}")

    altered = msg
    altered[10] = int(not altered[10])
    res2 = hamm(altered)
    print(f"Oh no!!! The message has been altered, but where? {altered}")
    print(f"Error detected in position: {res2}")

    print("Oh... Thanks Hamming")
