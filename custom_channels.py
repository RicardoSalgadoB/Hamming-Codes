import random
import time
import sys

class unreliable_channel:
    def __init__(self, warnings=True):
        self.sended = False
        self.warnings = warnings

    def send(self, msg):
        funny_messages = [
            "Enviando el Mensaje...",
            "Luchando con los aliens por la integridad del mensaje...",
            "Casi ahogándose en un río porque pisó mal...",
            "Conociendo al amor de su vida camino a entregar el mensaje..."
        ]

        if self.warnings:
            print("\nIniciando Transmisión Ultracifrada...\n")
    
        total_time = 1 #15
        bar_length = total_time
        interval = 1  # update every 0.5 seconds
        steps = int(total_time / interval)

        for i in range(steps + 1):
            progress = i / steps
            bar = "#" * int(bar_length * progress)
            space = " " * (bar_length - len(bar))
            msg_index = (i // 2) % len(funny_messages)
            if self.warnings:
                sys.stdout.write(f"\r[{bar}{space}] {funny_messages[msg_index]}")
                sys.stdout.flush()
            time.sleep(interval)

        if self.warnings:
            print("\n\nMensaje enviado, gracias por confiar en Cyberdine Systems AC de CV (made in Apodaca)\n")
        self.sended = [int(x) for x in msg]
    
    def receive(self):

        if not self.sended:
            raise Exception("Inbox is empty!")

        if len(self.sended) > 0:
            idx_to_change = random.randint(0, len(self.sended) - 1)
            self.sended[idx_to_change] = (1-int(self.sended[idx_to_change]))%2 #change the bit
    
        altered_msg = self.sended
        self.sended = False
        return altered_msg