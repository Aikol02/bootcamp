"""
http
tcp - 
ip - ip address
ip-address:port(8000) -> socket -> client, server
"""

import socket

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()

    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)
        print()
        print(address)

        client_socket.sendall('Hello, Makers!'.encode('utf-8'))
        client_socket.close()


if __name__ == '__main__':
    run()




