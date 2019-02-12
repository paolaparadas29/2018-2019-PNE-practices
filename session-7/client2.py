# Creating a client program which sends >1

import socket

# Create  a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8081
IP = "212.128.253.64"

# Connect to the server
s.connect((IP, PORT))

while True:

    #Asking the user for a message
    message = input('Enter a message: ')

    # Sending message
    s.send(str.encode(message))

    #Receiving and decoding the message
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER: ')
    print(msg)

    # Closing the file
    s.close()

print('The end')