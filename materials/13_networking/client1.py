#!usr/bin/python
import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))

msg = client_socket.recv(1024)
print(msg.decode("utf-8"))
welcome_msg = client_socket.send(bytes("Pozdrav na server!", "utf-8"))

