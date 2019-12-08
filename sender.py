#!/usr/bin/python3
from socket import *
from _thread import *
import threading
import sys
import random
import time
serverport1 = 12008
serversocket1 = socket(AF_INET, SOCK_STREAM)
serversocket1.bind(('', serverport1))
serversocket1.listen(40)
lasttime = time.time()
base = 0
nextseqnum = 0
N = 0
string = []
rcvpkt = ""
ACK = False
TIMEOUT = False
CONN = True
def ack(ssock, addr):
	global rcvpkt, ACK, TIMEOUT, lasttime, CONN
	while CONN:
		rcvpkt = ssock.recv(1024).decode()
		lasttime = time.time()
		ACK = True
		
def timeout():
	global lasttime, TIMEOUT, ACK
	if (time.time() - lasttime) > 10:
		TIMEOUT = True
	elif (time.time() - lasttime) < 10:
		TIMEOUT = False
	return TIMEOUT

def start_timer():
	global lasttime
	lasttime = time.time()
	
def randomiser():
	r = random.randint(0,6)
	if r == 0:
		return False
	else:
		return True
	 
def make_pkt(nextseqnum, data):
	sndpacket = str(nextseqnum) + '\n' + data
	return sndpacket
	
def rdt_send(ssock, addr, string):
	conn = True
	start = 0
	sndpacket = []
	global base, nextseqnum, N, rcvpkt, TIMEOUT, ACK
	while conn:
		if nextseqnum < len(string):
			if(nextseqnum < base + N):
				sndpacket.append(make_pkt(nextseqnum, string[nextseqnum]))
				if randomiser() and nextseqnum < len(string):
					ssock.send(sndpacket[nextseqnum].encode())
				if (base == nextseqnum):
					start_timer()
				print('sender: sending packet ' + str(nextseqnum))
				nextseqnum += 1
				time.sleep(1)
		else:
			pass
		if(start == 0):
			start_new_thread(ack, (ssock, addr))
			start = 1
		timeout()
		if ACK:
			print('sender: Received Ack for packet  ' + rcvpkt)
			base = int(rcvpkt) + 1
			if ( base == len(string)):
				conn = False
			ACK = False
			time.sleep(1)
		elif TIMEOUT:
			print('sender: Timed out on ACK for packet ' + str(base))
			i = base
			start_timer()
			while i < nextseqnum and i <= len(string) - 1:
				if randomiser():
					ssock.send(sndpacket[i].encode())
				print('sender: sending packet ' + str(i))
				i = i + 1
				time.sleep(1)
			TIMEOUT = False
def packets(N):
    l = []
    for i in range(N):
        for j in range(4):
            temp = random.randint(97, 122)
            ch = chr(temp)
            l.append(ch)
    return l	
def main():
	global N
	global string
	N = int(input('Enter N:'))
	string = packets(N)
	ssock, addr = serversocket1.accept()
	rdt_send(ssock, addr, string)
	ssock.close()
	serversocket1.close()

if __name__ == '__main__':
	main()


