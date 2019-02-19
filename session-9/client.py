import socket
import termcolor

# SERVER IP, PORT
IP = '172.17.0.1'
PORT = 8080


while True:

    #Ask for message
    msg = input("> ")

    #Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP,PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    #Changing color of the message
    # Print the server's response
    print('Response: ')
    termcolor.cprint(response,'blue')

    s.close()