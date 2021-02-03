import socket


my_username = input("Username:")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 1234))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<10}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    message = input(f'{username} > ')
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<10}".encode('utf-8')
        client_socket.send(message_header + message)

