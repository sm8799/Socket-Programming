from socket import *
from _thread import *
import threading
serverPort = 12010
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(40)

def decrypt(sentence, key):
    key_length = len(key)
    d = []
    print(sentence)
    sentence = list(sentence)
    print(key)
    for i in range(key_length):
        d.append((int(key[i]), i, str(key_length - i), str(i)))
    half = key_length * (key_length + 1) // 2
    encrypted_a = sentence[0:half]
    encrypted_b = sentence[half:]
    print(d)
    d_copy = sorted(d)
    matrix = {}
    print(d_copy)
    cnt_1 = cnt_2 = 0 
    for i in d_copy:
        l = []
        a = int(i[2])
        b = int(i[3])
        matrix[b] = encrypted_b[cnt_2:cnt_2 + b] + encrypted_a[cnt_1:cnt_1 + a]
        cnt_1 = cnt_1 + a
        cnt_2 = cnt_2 + b
    s = ''
    for i in sorted(matrix.keys()):
        print(''.join(matrix[i]))
        s = s + ''.join(matrix[i])
    print(s)
    s = s.rstrip('0')
    msg = ''
    q = len(s) // 7
    r = len(s) % 7
    print(len(s))
    for i in range(q):
        bintext = s[i * 7 : (i + 1) * 7]
        msg = msg + chr(int(bintext, 2))
    if r != 0:
        bintext = s[q * 7 : ]
        for i in range(7 - r):
            bintext = bintext + '0'
        msg = msg + chr(int(bintext, 2))
    return msg

def clientfun(connectionSocket, addr):
	conn = True
	message = 'reply "close" to disconnect from server'
	check = 'close'
	connectionSocket.send(message.encode())
	while True:
		key_n_sentence = connectionSocket.recv(1024).decode()
		key_n_sentence = key_n_sentence.split(' ')
		key = key_n_sentence[0]
		sentence = key_n_sentence[1]
		msg = decrypt(sentence, key)
		print(msg)
		
while True:
	connectionSocket, addr = serverSocket.accept()
	print('new client connected, reply "ok" to disconnect anytime')
	clientfun(connectionSocket, addr)
	break
connectionSocket.close()
serverSocket.close()
