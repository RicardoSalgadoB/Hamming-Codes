from random import choice
from custom_channels import unreliable_channel
from utils import hamm, encode, decode

def main(show: bool = False):
    unreliable = unreliable_channel()                           # Declarar objeto para alterar los mensajes
    terminators = ["Arnold Schwarzenegger", "Robert Patrick"]   # Nombres de los actores de los terminators que corregiran los mensajes
    msg = [choice([0,1]) for i in range(26)]                    # Crear mensaje aleatoriamente

    # Opcionalmente, mostrar mensaje original
    if show:
        print(f'[Mensaje Original: {msg}]\n')
        
    # Codificar mensaje y opcionalmente mostrarlo
    encoded_msg = encode(msg)
    if show:
        print(f'[Mensaje codificado: {encoded_msg}]\n')
        
    # Enviar mensaje donde puede ser alterado. Opcionalmente, imprimir mensaje recibido
    unreliable.send(encoded_msg)
    received_msg = unreliable.receive()
    if show:
        print(f'[Mensaje recibido: {received_msg}]\n')
        
    # Utilizar los códigos de hamming para identificar y corregir el error si lo hay. Opcionalmente, mostrar corrección
    n = hamm(received_msg)
    if n == 0:
        print("Mensaje recibido perfectamente\n")
    else:
        print(f"Oh no... hay un error el posicion {n} del mensaje codificado. Enviando a {choice(terminators)} al pasado para corregirlo.\n")
        received_msg[n] = (received_msg[n]+1)%2     # Corregir error :)
        print("Mensaje corregido. Gracias por confiar en Cyberdine Systems AC de CV (made in Apodaca)\n")
    if show:
        print(f"[Mensaje Corregido: {received_msg}]\n")
        
    # Descodificar el mensaje a su estado natural y opcionalmente mostrarlo
    decoded_msg = decode(encoded_msg)
    if show:
        print(f"[Mensaje decodificado: {decoded_msg}]\n")
    
    
if __name__ == '__main__':
    main()