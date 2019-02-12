# client.py
"""
This code was taken from the assignment and modified to work for submission
"""

# import socket
import socket

# create a socket object using defaults
s = socket.socket()

# define the port
port = 9500

# connect to the server on local computer
# looking to make this fail because we aren't sending "Hello"
s.connect(('localhost', port))
s.send(b'Other data')

# recieve data from the server
print(s.recv(1024))

# close the connection
s.close()
