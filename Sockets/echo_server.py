# ECHO SERVER

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	con, addr = s.accept()
	with con:
		print('Connected by: ', addr)
		while True:
			data = con.recv(1024)
			if not data:
				break
			con.sendall(data)
