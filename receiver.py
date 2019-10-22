#!/usr/bin/python3
from socket import *
from _thread import *
import threading
import sys
import random
import time
import random
expectedseqnum = 0
serverName = '127.0.0.1'
serverPort = 12008
rsock = socket(AF_INET, SOCK_STREAM)
rsock.connect((serverName,serverPort))
rcvpkt = ""
sndpkt = "-1"
recv = []
def hasseqnum(rcvpkt):
	global recv
	recv = rcvpkt.split('\n')
	return str(recv[0])

def randomiser():
	r = random.randint(0,6)
	if r == 0:
		return False
	else:
		return True

def rdt_rcv():
	global rcv_sock, recv, expectedseqnum, sndpkt
	print('Data Received')
	while True:
		try :
			rcvpkt = rsock.recv(1024).decode()
		except BrokenPipeError:
			sys.exit()
		seqnum = hasseqnum(rcvpkt)
		if(seqnum == str(expectedseqnum)):
			print(recv[1])
			sndpkt = str(expectedseqnum)
			if randomiser():
				try:
					rsock.send(sndpkt.encode())
				except BrokenPipeError:
					sys.exit()
			expectedseqnum += 1
		else:
			if randomiser():
				try:
					rsock.send(sndpkt.encode())
				except BrokenPipeError:
					sys.exit()

if __name__ == '__main__':
	rdt_rcv()
