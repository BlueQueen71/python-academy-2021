import socket
import select


clients = {}
server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)
server_socket.bind((socket.gethostname(), 9090))
server_socket.listen()
print("Cekam na pripojeni klienta..")
socket_list = [server_socket]


def receive_message(client_socket):
    message_header = client_socket.recv(10)
    if not message_header:
        return False
    message_length = int(message_header.decode("utf-8"))
    return {
        "header": message_header,
        "data": client_socket.recv(message_length)
    }


while True:
    read_sockets, _, except_sockets = select.select(
        socket_list, [], socket_list
    )
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            print(f"Pripojeny klient: {client_address}")

            user = receive_message(client_socket)
            if not user:
                continue
            clients[client_socket] = user
            socket_list.append(client_socket)
            print(f"Nove pripojeni: {client_address}, \
uzivatel: {user['data'].decode('utf-8')}")

        else:
            message = receive_message(notified_socket)
            if not message:
                socket_list.remove(notified_socket)
                print(f"{clients[notified_socket]['data'].decode('utf-8')} \
ukoncil spojeni")
                clients.pop(notified_socket)
                continue

            user = clients[notified_socket]
            print(f"Zprava od {user['data'].decode('utf-8')}: \
{message['data'].decode('utf-8')}")






