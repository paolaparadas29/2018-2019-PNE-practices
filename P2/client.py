#importing package socket
import socket

#importing class Seq
from Seq import Seq

PORT = 8081
IP = "212.128.253.72"

while True:

    #Asking the user for a message
    sequence = input('Enter a sequence: ')

    # Create  a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((IP, PORT))

    # Introducing the parameter 'sequence' to the object
    s1= Seq(sequence)

    #Reversing the sequence
    s2=s1.reverse()

    #Calculating the complement of the reverse
    s3=s2.complement()

    # Sending message
    s.send(str.encode(s3.strbases))

    #Receiving and decoding the message
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER: ')
    print(msg)

    # Closing the file
    s.close()

