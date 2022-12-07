import socket
import time
import datetime
import struct

TCP_IP = '127.0.0.1'
TCP_PORT = 3000

# Connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((TCP_IP, TCP_PORT))

# Start an HTTP request
s.send(b'GET / HTTP/1.1\r\n\
Host: example.com\r\n\
\r\n')
# response = s.recv(4096)
# s.close()
# print(response.decode())
# time.sleep(0.1)

# RST the socket without reading the response
# See https://stackoverflow.com/a/6440364/68051 for context
s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
s.close()
print('reset...', datetime.datetime.now())