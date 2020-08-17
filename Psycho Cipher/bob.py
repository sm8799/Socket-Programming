from socket import *
import random
import numpy as np
def extract_key(sentence):
    total_length = len(sentence)
    total_length = total_length * 7
    key_length = int(np.sqrt(total_length)) + 1
    total_key = []
    if key_length > 10:
        q = key_length // 10
        r = key_length % 10
        l = [0,1,2,3,4,5,6,7,8,9]
        partial_key = []
        for i in range(10):
            rand_int = random.choice(l)
            l.remove(rand_int)
            partial_key.append(rand_int)
        for i in range(q):
            total_key = total_key + partial_key
        total_key = total_key + partial_key[0:r]
        total_key = list(map(str, total_key))
        total_key = ''.join(total_key)
    else:
        l = [0,1,2,3,4,5,6,7,8,9]
        partial_key = []
        for i in range(key_length):
            rand_int = random.choice(l)
            l.remove(rand_int)
            partial_key.append(rand_int)
        total_key = partial_key
        total_key = list(map(str, total_key))
        total_key = ''.join(total_key)
    return total_key

def fit(sentence, key):
    key_length = len(key)
    matlen = key_length ** 2
    bitify = ''
    for i in sentence:
        bitify = bitify + '{0:07b}'.format(ord(i))
    bitlist = list(bitify)
    bitlen = len(bitlist)
    if bitlen < matlen:
        while bitlen < matlen:
            bitlist.append('0')
            bitlen += 1
    d = []
    for i in range(key_length):
        d.append((int(key[i]), bitlist[i * key_length : (i + 1) * key_length]))
    return d


def layer_A(matrix):
    a = ''
    b = ''
    switch1 = []
    switch2 = []
    key_length = len(matrix)
    for i in range(key_length):
        print(''.join(matrix[i][1]))
        l = matrix[i][1][i:]
        l = ''.join(l)
        switch1.append((matrix[i][0], i, l))
        l = matrix[i][1][:i]
        l = ''.join(l)
        switch2.append((matrix[i][0], l))
    switch1 = sorted(switch1)
    switch2 = sorted(switch2)
    for i in range(len(switch1)):
        a = a + switch1[i][2]
        b = b + switch2[i][1]
    return a, b



if __name__ == "__main__":
    serverName = '127.0.0.1'
    serverPort = 12010
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    conn = True
    check = 'ok'
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())
    while conn:
        
        # take input from the sender
        sentence = input('Enter Message:')

        # extract key out of the sentence
        key = extract_key(sentence)

        # fitting sentence in a matrix : Layer 1
        matrix = fit(sentence, key)

        # Layer 2
        encrypted_message_a, encrypted_message_b = layer_A(matrix)

        # Layer 2 complete
        encrypted_message = encrypted_message_a + encrypted_message_b
        # msg = decrypt(encrypted_message, key)
        # print(msg)
        key_n_message = key + ' ' + encrypted_message
        
        clientSocket.send(key_n_message.encode())
    clientSocket.close()