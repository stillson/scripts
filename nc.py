#!/usr/bin/env python3

import socket
import sys

def netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('pre connect')
    s.connect((host, int(port)))
    print('post connect')
    s.sendall(content.encode())
    s.sendall(b'\r\n\r\n\r\n')
    print('post send')
    s.shutdown(socket.SHUT_WR)
    print('post shutdown')
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(repr(data))
    print('out')
    s.close()

if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]

    host = socket.gethostbyname(host)
    content = ' '.join(sys.argv[3:])
    print('%s:%s' % (host,port))

    netcat(host, port, content)
