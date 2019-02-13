import socket

# Create  a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8080
IP = "212.128.253.72"

# Connect to the server
s.connect((IP, PORT))

while True:

    #Asking the user for a message
    sequence = input('Enter a sequence: ')

    # Sending message
    s.send(str.encode(sequence))

    #Receiving and decoding the message
    msg = s.recv(2048).decode('utf-8')
    print('MESSAGE FROM THE SERVER: ')
    print(msg)

    # Closing the file
    s.close()

