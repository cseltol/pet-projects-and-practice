import sys
import time
import random
import socket
import selectors
from threading import Thread


# def handle_connection(conn, addr):
#     print(f'Connected by {addr}')
#     with conn:
#         while True:
#             if not data:
#                 break
#             data = conn.recv(4096)
#             n = int(data.decode())
#             res = f'{n * 2}\n'.encode('utf-8')
#             conn.send(res)
#     print(f'Disconnected by {addr}')


def server(port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", port))
        s.listen(5)
        sel = selectors.DefaultSelector()
        sel.register(s, selectors.EVENT_READ)
        while True:
            for key, mask in sel.select():
                if key.fileobj is s:
                    conn, addr = s.accept()
                    print(f'Connected by {addr}')
                    conn.setblocking(False)
                    sel.register(conn, selectors.EVENT_READ, ('read', None))
                else:
                    conn = key.fileobj
                    op, arg = key.data
                    sel.unregister(conn)
                    if op == 'read':
                        data = conn.recv(4096)
                        if not data:
                            conn.close()
                            sel.unregister(conn)
                        n = int(data.decode())
                        res = f'{n * 2}\n'.encode('utf-8')
                        sel.register(conn, selectors.EVENT_WRITE,
                                     ('write', res))
                    elif op == 'write':
                        conn.send(arg)
                        sel.register(conn, selectors.EVENT_READ,
                                     ('read', None))
                    else:
                        assert False, op

            # try:
            #     conn, addr = s.accept()
            # except BlockingIOError:
            #     continue
            # # handle_connection(conn, addr)
            # t = Thread(target=handle_connection, args=(conn, addr))
            # t.start()


def client(port=8080):
    with socket.create_connection(('127.0.0.1', port)) as s:
        f = s.makefile(mode='rw', buffering=1, newline='\n')
        while True:
            n = random.randrange(10)
            f.write(f'{n}\n')
            print(n, f.readline().strip())
            time.sleep(random.random() * 2)


if __name__ == '__main__':
    if sys.argv[1] == 'server':
        server()
    else:
        assert sys.argv[1] == 'client'
        client()

