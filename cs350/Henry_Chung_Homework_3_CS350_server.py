"""Simple server application"""

import socket

#  server host (local machine)
host = 'localhost' 

#  machine port
port = 7000

#  CONNECTION tuple
conn = (host, port)

#  number of requests before need to thread...
backlog = 5

#  max length of data buffer (bytes) 
size = 1024

#  create a socket object. AF_INET = ipv4 addressing  SOCK_STREAM = transport protocol (tcp)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#  force server to release socket immediately if killed
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

#  bind the socket to connection
s.bind(conn) 

#  listen for events on the socket
s.listen(backlog)

#  poll for incoming connections then send response
while 1:
    print 'Server ready, willing and able!'

    # waits for connection then returns a tuple representing socket connection object
    client, address = s.accept()
 
    # reads in the payload sent by a client
    fd = client.recv(size)
    se = open(fd, 'r')
    data = se.read()
    if data:
        print 'Client at ', address[0], 'asked for ==> ', data
        #  send a message back to the client
        client.send(data)

    client.close() # close the connection with client
