import socket


username = input("Vloz uziv.jmeno:")
username_header = f"{len(username):<10}"

client_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)
client_socket.connect((socket.gethostname(), 9090))
client_socket.send(
    bytes(username_header + username, "utf-8")
)

while True:
    message = input(f"{username}> ")
    message_header = f"{len(message):<10}"
    client_socket.send(
        bytes(message_header + message, "utf-8")
    )

