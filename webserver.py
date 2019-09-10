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
'''
def numbers_to_strings(argument): 
	switcher = { 
		0: "zero", 
		1: "one", 
		2: "two", 
	} 

	# get() method of dictionary data type returns 
	# value of passed argument if it is present 
	# in dictionary otherwise second argument will 
	# be assigned as default value of passed argument 
	return switcher.get(argument, "nothing") 

# Driver program 
if __name__ == "__main__": 
	argument=0
	c = numbers_to_strings(argument)
print(c)
'''
