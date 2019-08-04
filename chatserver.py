#!/usr/bin/python
from socket import *
import thread
serverPort = 12009
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(40)
def clientfun(connectionSocket, addr) :
	conn = True
	message = 'reply "close" to disconnect from server'
	check = 'close'
	connectionSocket.send(message.encode())
	while conn:
		sentence = connectionSocket.recv(1024).decode()
		if sentence != check : 
			print(sentence)
		else :
			conn = False
		from_server = raw_input('reply:')
		connectionSocket.send(from_server.encode())
		
while True:
	connectionSocket, addr = serverSocket.accept()
	print('new client connected, reply "ok" to disconnect anytime')
	thread.start_new_thread(clientfun, (connectionSocket, addr))
connectionSocket.close()
serverSocket.close()
