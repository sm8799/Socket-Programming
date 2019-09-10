from socket import *
import os
from _thread import *
import threading 
serverport = 8081
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(('', serverport))
serversocket.listen(40)

def clientfun(connectionsocket, addr):
	global serversocket
	conn = True
	while conn:
		message = connectionsocket.recv(4096).decode()
		print(message)
		req_list = message.split('\r\n')
		print('2')
		for i in req_list:
			print(i, end =" ")

while True:
	connectionsocket, addr = serversocket.accept()
	start_new_thread(clientfun, (connectionsocket, addr))
serversocket.close()
