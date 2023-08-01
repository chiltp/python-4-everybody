#Importing the socket module:
#The socket module is used to create and interact with sockets, which are endpoints for communication between machines over a network.
import socket

#Creating a socket object and connecting to a server:
#Here, we create a socket object named mysock. The socket.AF_INET parameter specifies that we'll be using IPv4 for communication, and socket.SOCK_STREAM indicates that we'll use TCP for the communication protocol. We then connect the socket to the server data.pr4e.org on port 80, which is the default port for HTTP.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#Constructing and sending an HTTP GET request:
#In this part, we construct an HTTP GET request for the resource http://data.pr4e.org/intro-short.txt and encode it to bytes using encode() because the send() method expects bytes data. The \r\n\r\n at the end represents the end of the HTTP headers and an empty line.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

#Receiving and printing the server's response:
#In this part, we enter a loop to receive and process the response from the server. The recv() method is used to receive data from the server, and we pass 512 as the maximum number of bytes to receive at once. If the length of data is less than 1, it means there's no more data to receive, so we break out of the loop.
#The received data is in bytes, so we use decode() to convert it to a string and print it to the console. The end='' argument in print() is used to avoid adding an extra newline after each print() statement.
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

#Closing the socket:
#Finally, we close the socket using the close() method to free up resources and terminate the connection.
mysock.close()

