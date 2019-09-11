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
'''import os
element = '/home/student'
dir_list = os.listdir(element)
#print(os.listdir(element))
for i in dir_list:
	if i.startswith('.'):
		print(i)
		dir_list.remove(i)

#for i in dir_list:
#	print(i)'''
'''
<!DOCTYPE html>
<html>
<body>
>An Unordered HTML List</h2>

<u<l
<h2i><a href = "https://www.w3schools.com/html/">Coffee<a></li>
  l>
  <li>Tea</li>
  <li>Milk</li>
</ul>  

<h2>An Ordered HTML List</h2>

<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol> 

</body>
</html>
'''
'''
       general-header = Cache-Control            ; Section 14.9
                      | Connection               ; Section 14.10
                      | Date                     ; Section 14.18
                      | Pragma                   ; Section 14.32
                      | Trailer                  ; Section 14.40
                      | Transfer-Encoding        ; Section 14.41
                      | Upgrade                  ; Section 14.42
                      | Via                      ; Section 14.45
                      | Warning                  ; Section 14.46
'''
