#!usr/bin/python3
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1234))
server_socket.listen(5)
print("Inicializace..")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Navazano spojeni od [{client_address}]")
    client_socket.send(bytes("Vitej na serveru", "utf-8"))
    client_socket.close()

