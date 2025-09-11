import numpy as np
from random import choice
from custom_channels import unreliable_channel
from utils import hamm, encode

unreliable = unreliable_channel()

#x = [choice([0,1]) for i in range(10)]
x = [1, 1, 0, 0, 1, 1, 1, 1, 1, 1]

print(x)
encoded_msg = encode(x)
sent_msg = []
unreliable.send(encoded_msg)
sent_msg.append(unreliable.receive())

print(encoded_msg)
#print(sent_msg[0])
#n = hamm(sent_msg[0])
print([1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1])
n = hamm([1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1])

print(n)