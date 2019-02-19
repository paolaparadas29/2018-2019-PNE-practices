import socket
import sys
import termcolor

PORT = 8080
IP = '172.17.0.1'
MAX_OPEN_REQUESTS = 5

def process_client(cs):

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    #Changing the color of the message
    # Print the received message, for debugging
    print("Message from the client: ")
    termcolor.cprint(msg, 'magenta')

    if msg=='EXIT':
        sys.exit(0)

    else:

        # Sending the message back to the client
        # because we are a echo.server
        cs.send(str.encode(msg))

        # Close the socket
        cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)

    clientsocket.close()