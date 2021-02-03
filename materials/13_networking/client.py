import sys
import select
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 9090))
print("PRIPOJENY JAKO KLIENT..")

while True:
    socket_list = [sys.stdin, server]
    read_socket, write_socket, error_socket = select.select(socket_list, [], [])

    for sock in read_socket:
        if sock == server:
            msg = server.recv(1024)
            print(f"MESSAGE:{msg}")
        else:
            msg = sys.stdin.readline().strip()
            # if msg == "quit":
                # server.close()
                # break
            # else:
            server.send(bytes(msg, "utf8"))
            sys.stdout.write("<YOU>")
            #sys.stdout.write(msg)
            sys.stdout.flush()
server.close()

