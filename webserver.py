#!/usr/bin/python
from socket import *
import thread
serverport = 8080
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(('', serverport))
serversocket.listen(40)

def clientfun(connetctionsocket, addr):
	global serversocket
	conn = True
	print('Serving HTTP on 127.0.0.1 port 8080(http://127.0.0.1:8080/)')
	sentence = connectionsocket.recv(1024).decode()
	print(sentence)
	connectionsocket.close()

while True:
	connectionsocket, addr = serversocket.accept()
	thread.start_new_thread(clientfun, (connectionsocket, addr))
serversocket.close()
