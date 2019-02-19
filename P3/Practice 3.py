import socket
import termcolor

PORT = 8080
IP = '172.17.0.1'
MAX_OPEN_REQUESTS = 5

# Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

