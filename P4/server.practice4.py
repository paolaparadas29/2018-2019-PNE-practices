import socket
import termcolor

# Change this IP to yours!!!!!
IP = "212.128.253.84"
PORT = 8089
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Separating the message in parts

    parts = msg.split(' ')

    # Taking the second part to know what resource must be used

    type = parts[1]

    # Deciding depending on the resource what html code must be used

    if type == '/':
        resource = 'index.html'
    elif type == '/blue':
        resource = 'blue.html'
    elif type == '/pink':
        resource = 'pink.html'
    else:
        resource = 'error.html'

    # Opening the respective code

    with open(resource, 'r') as a:
        content = a.read()

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # Create the status_line

    status_line = "HTTP/1.1 200 OK\r\n"

    # Create a header

    header = 'Content-type: text/html\r\n'
    header += 'Content-Lenght: {}\r\n'.format(len(str.encode(content)))

    # Create a response

    response_msg = status_line + header + '\r\n' + content

    # Send the response

    cs.send(str.encode(response_msg))

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
    # Accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
