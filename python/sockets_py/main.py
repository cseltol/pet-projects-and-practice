import socket
import views

URLS = {
    '/': views.index,
    '/blog': views.index,
}


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    elif code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    else:
        return URLS[url]()


def generate_headers(method, url):
    if not method == 'GET':
        return 'HTTP/1.1 405 Method not allowed\n\n', 405
    elif url not in URLS:
        return 'HTTP/1.1 404 Not found\n\n', 404
    else:
        return 'HTTP/1.1 200 OK\n\n', 200


def parse_req(req):
    parsed = req.split(' ')
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_res(req):
    method, url = parse_req(req)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)

    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8080))
    server_socket.listen()

    while True:
        client_socket, address = server_socket.accept()
        req = client_socket.recv(1024)
        print(f'\nRequest is: {req}')
        print(f'\nAddress of client socket is: {address}')

        res = generate_res(req.decode('utf-8'))

        client_socket.sendall(res)
        client_socket.close()


if __name__ == '__main__':
    run()
