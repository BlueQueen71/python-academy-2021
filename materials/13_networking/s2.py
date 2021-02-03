import sys
import socket
import pickle


ZPRAVA = sys.argv[1]
HEADER = 10
PREVED_ZPR = pickle.dumps(ZPRAVA)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9090))
s.listen(5)

while True:
    socket_klienta, adresa_klienta = s.accept()
    print(f"NAVAZANO SPOJENI S: {adresa_klienta}")
    cela_zprava = bytes(f"{len(PREVED_ZPR):<{HEADER}}", "utf-8") + PREVED_ZPR
    socket_klienta.send(cela_zprava)

