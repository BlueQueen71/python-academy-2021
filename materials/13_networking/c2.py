import socket
import pickle


HEADER = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 9090))

while True:
    cela_zprava = b""

    while (nova_zprava := True):
        zprava = s.recv(16)
        if nova_zprava:
            print(f"NOVA ZPRAVA DELKY: {zprava[:HEADER]}")
            delka_zpravy = zprava[:HEADER]
            nova_zprava = False

        print(f"DELKA ZPRAVY: {delka_zpravy}")
        cela_zprava += zprava

        if len(cela_zprava) - HEADER == delka_zpravy:
            print("OBDRZENA CELA ZPRAVA")
            print(cela_zprava[HEADER:])
            print(pickle.loads(cela_zprava[HEADER:]))
            nova_zprava = True
            cela_zprava = b""


