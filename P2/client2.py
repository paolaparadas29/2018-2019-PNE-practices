#Importing package socket

import socket


PORT = 8080
IP = "212.128.253.72"

while True:

    #Asking the user for a message
    sequence = input('Enter a sequence: ')

    # Create  a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((IP, PORT))

    # Sending message
    s.send(str.encode(sequence))

    #Receiving and decoding the message
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER: ')
    print(msg)

    s.close()
