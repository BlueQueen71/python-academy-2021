import select
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1234))
server_socket.listen(5)
print("Inicializace")

sockets_list = [server_socket]                  # list socketu pro funkci select()
clients = {}                                    # socket-klic, header a data - hodnoty

print(f"Posloucham spojeni na adrese: {socket.gethostname()}:1234 ...")

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            print(f"Navazano spojeni od [{client_address}]")
            client_socket.send(bytes("Vitej na serveru", "utf-8"))

