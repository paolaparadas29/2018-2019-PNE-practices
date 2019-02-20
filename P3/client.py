import socket

#Client IP and PORT

IP='212.128.253.78'
PORT=8081


# User can write a message
response1 = 'atttc'+'\n'+'len'+'\n'+'complement'



# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(response1))

# Receive the servers response
response = s.recv(2048).decode()

# Changing color of the message
# Print the server's response
print('Response: ', response)

s.close()

