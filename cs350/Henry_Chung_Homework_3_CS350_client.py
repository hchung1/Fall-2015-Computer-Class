"""Simple client application"""

import socket

#  server host (local machine)
host = 'localhost' 

#  machine port
port = 7000

#  server info as tuple
SERVER = (host, port)

#  max length of data buffer (bytes) 
size = 1024
filename = raw_input("What is the name of the file to search in the server. >>")
#  create a socket AF_INET = ipv4 addressing SOCK_STREAM = transport protocol (tcp)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to a server 
s.connect(SERVER)

# send data to server 
s.send(filename)


# wait for/read in response from server
data = s.recv(size) 

# what'd we get?
print '\nServer RESPONSE:\n> ', data

# close connection
s.close()
