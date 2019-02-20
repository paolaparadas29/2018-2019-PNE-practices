import socket

#Client IP and PORT

IP='127.0.0.1'
PORT=8080

# User's message
response1 = 'act\npercA'

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(response1))

# Receive the servers response
response = s.recv(2048).decode()

# Print the server's response
print('Response: ', response)

# Close socket
s.close()

