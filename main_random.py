from random import choice
from custom_channels import unreliable_channel
from utils import hamm, encode, decode

def main(show: bool = False):
    unreliable = unreliable_channel()                           # Declare object to simulate message transmission
    terminators = ["Arnold Schwarzenegger", "Robert Patrick"]   # Names of the terminators that can be sent to the past
    msg = [choice([0,1]) for i in range(26)]                    # Create message randomly

    # Optionally, show orignal message
    if show:
        print(f'[Original: {msg}]\n')
        
    # Encode message & optionally print it
    encoded_msg = encode(msg)
    if show:
        print(f'[Encoded: {encoded_msg}]\n')
        
    # Send message, it can be altered. Optionally, show altered message
    unreliable.send(encoded_msg)
    received_msg = unreliable.receive()
    if show:
        print(f'[Received: {received_msg}]\n')
        
    # Use Hamming codes to detect and correct the message. Optionally, show the corrected message
    n = hamm(received_msg)
    if n == 0:
        print("Message received perfectly\n")
    else:
        print(f"Oh no... there's an error at positon {n}. Sending {choice(terminators)} to the past to fix it.\n")
        received_msg[n] = (received_msg[n]+1)%2     # Correct Error :)
        print("Error Corrected. Thank you for trusting Cyberdine Systems AC de CV (made in Apodaca)\n")
    if show:
        print(f"[Corrected: {received_msg}]\n")
        
    # Decodify the message, removing parity bits &, optionally, show it
    decoded_msg = decode(encoded_msg)
    if show:
        print(f"[Decodified: {decoded_msg}]\n")
    
    
if __name__ == '__main__':
    main()