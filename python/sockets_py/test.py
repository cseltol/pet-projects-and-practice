import socket

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 8080))
    server_sock.listen()

    while True:
        client_socket, address = server_sock.accept()
        req = server_sock.recv(1024)
        print(f'Request is {req}')
        print(f'Address is {address}')

        res = '<h1>мышыч гений</h1>'

        client_socket.sendall(res)

if __name__ == '__main__':
    main()
