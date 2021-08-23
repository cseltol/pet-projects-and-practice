import socket


def main():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost', 8080))
    socket_server.listen()

    while True:
        print('\nBefore .accept()')
        client_socket, address = socket_server.accept()
        print(f'\nConnection from {address}')

        while True:
            print('\nBefore .recv()')
            req = client_socket.recv(1024)
            
            if not req:
                break
            else:
                res = b'\n Hi there!'
                client_socket.send(res)

        print('Outside inner loop')
        client_socket.close()

if __name__ == '__main__':
    main()
