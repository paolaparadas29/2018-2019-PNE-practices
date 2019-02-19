import socket

#Client IP and PORT

IP='172.17.0.1'
PORT=8080

response=''
while True:
    s= response
    msg= input('Enter the sequence and then the functions: ')
    if msg!='\n':
        response=msg+s

    else:

        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((IP, PORT))

        # Send the request message to the server
        s.send(str.encode(msg))

        # Receive the servers response
        response = s.recv(2048).decode()

        # Changing color of the message
        # Print the server's response
        print('Response: ', response)

        s.close()

