import socket
from Seq import Seq

PORT = 8080
IP = '127.0.0.1'
MAX_OPEN_REQUESTS = 5

sequenceproof = 'ACTG'

functions = ['len','complement','reverse','countA','countC','countG','countT','percA','percC','percG','percT']


def process_client(cs):

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Separate string by '\n'

    response1 = msg.split('\n')


    header = response1[0].upper()


    for i in header:

        if header == '\n':
            response = 'Alive'

        elif i not in sequenceproof:
            response = 'Error\n'

        else:
            response= 'OK\n'

    del response1[0]

    response= response + str(recognize(header,response1))

    # Sending message
    cs.send(str.encode(response))

    # Close the socket
    cs.close()



def recognize(s,g):

    functions = ['len','complement','reverse','countA','countC','countG','countT','percA','percC','percG','percT']

    # Loop to recognize if the function name coincide with the functions that my program can perform
    respu=''
    for i in range(0,len(g)-1):

        if g[i] in functions:

            resp = function(g[i],s)
            respu= respu + str(resp) + '\n'

        else:
            respu = respu + 'Error\n'

    return respu

def function(d, t):
    # Function which perfom the task that the client is asking for

    s1 = Seq(t)

    if d == 'len':
        s2 = s1.len()
        return s2
    elif d == 'complement':
        s2 = s1.complement()
        return s2.strbases
    elif d == 'reverse':
        s2 = s1.reverse()
        return s2.strbases
    elif d == 'countA':
        s2 = s1.count('A')
        return s2.strbases
    elif d == 'countC':
        s2 = s1.count('C')
        return s2.strbases
    elif d == 'countT':
        s2 = s1.count('T')
        return s2.strbases
    elif d == 'countG':
        s2 = s1.count('G')
        return s2.strbases
    elif d == 'percA':
        s2 = s1.perc('A')
        return s2.strbases
    elif d == 'percC':
        s2 = s1.perc('C')
        return s2.strbases
    elif d == 'percT':
        s2 = s1.perc('T')
        return s2.strbases
    elif d == 'percG':
        s2 = s1.perc('G')
        return s2.strbases


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
