import socket
import sys


my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))


username = my_username.encode('utf-8')
username_header = f"{len(username)}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    message = input(f'{my_username} > ')
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message)}".encode('utf-8')
        client_socket.send(message_header + message)

    # try:
        # while True:
            # username_header = client_socket.recv(1024)

            # if not len(username_header):
                # print('Connection closed by the server')
                # sys.exit()

            # username_length = int(username_header.decode('utf-8').strip())

            # username = client_socket.recv(username_length).decode('utf-8')

            # message_header = client_socket.recv(1024)
            # message_length = int(message_header.decode('utf-8').strip())
            # message = client_socket.recv(message_length).decode('utf-8')

            # print(f'{username} > {message}')

