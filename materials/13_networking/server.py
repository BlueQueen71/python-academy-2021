import sys
import socket
from _thread import start_new_thread

list_of_clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((socket.gethostname(), 9090))
server.listen(100)
print("SPOUSTIM SERVER..")


def client_thread(conn, addr) -> None:
    name = conn.recv(1024).decode("utf8")
    welcome = f"VITEJ {name}, POKUD CHCES UKONCIT CHAT, NAPIS 'quit'"
    conn.send(bytes(welcome, "utf8"))

    while True:
        message = conn.recv(1024)
        if message:
            print(f"<{addr[0]}> {name}:{message}")
            message_to_send = f"<{addr[0]}> {name}:{message}"
            broadcast(message_to_send, conn)
        else:
            # conn.send(bytes("quit", "utf8"))
            # conn.close()
            remove(conn)
            # broadcast(f"{name} opustil konverzaci", conn)
            # break


def broadcast(msg: str, conn) -> None:
    for client in list_of_clients:
        if client != conn:
            try:
                client.send(bytes(msg, "utf8"))
            except:
                client.close()
                remove(client)


def remove(conn) -> None:
    if conn in list_of_clients:
        list_of_clients.remove(conn)


while True:
    client, address = server.accept()
    list_of_clients.append(client)
    print(f"{address[0]} je pripojeny")
    client.send(bytes("VITEJ V NASEM CHATU!", "utf8"))
    start_new_thread(client_thread, (client, address))
    # client_thread(client, address)
    # ACCEPT_THREAD = threading.Thread(target=client_thread, args=(client, address))
    # ACCEPT_THREAD.start()
    # ACCEPT_THREAD.do_run = False
    # ACCEPT_THREAD.join()


client.close()
server.close()

