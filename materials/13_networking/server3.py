import socket
import select


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1234))
server_socket.listen(5)
print("Inicializace")

sockets_list = [server_socket]                  # list socketu pro funkci select()
clients = {}                                    # socket-klic, header a data - hodnoty


def receive_message(client_socket):
    if len(msg_header := client_socket.recv(10)):
        msg_length = int(msg_header.decode("utf-8").strip())
        return {"header": msg_header, "data": client_socket.recv(msg_length)}
    return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            print(f"Navazano spojeni od [{client_address}]")

            if not (user := receive_message(client_socket)):
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f"Nove spojeni:{client_address}, uzivatel:{user['data'].decode('utf-8')}")

        else:
            if not (message := receive_message(notified_socket)):
                sockets_list.remove(notified_socket)
                print(f"Spojeni ukonceni: {clients[notified_socket]['data'].decode('utf-8')}")
                clients.pop(notified_socket)
                continue

            user = clients[notified_socket]
            print(f"Zprava od: {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

