#ECHO CLIENT
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
	c.connect((HOST, PORT))
	c.sendall(b'Hello?')
	data = c.recv(1024)

print('Received', repr(data))