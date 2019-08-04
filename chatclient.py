#!/usr/bin/python
from socket import *
serverName = '127.0.0.1'
serverPort = 12009
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
conn = True
check = 'ok'
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
while conn:
	sentence = raw_input('Enter Message:')
	clientSocket.send(sentence.encode())
	modifiedSentence = clientSocket.recv(1024)
	print(modifiedSentence.decode())
	if modifiedSentence == check :
		conn = False
clientSocket.close()

