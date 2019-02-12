# server.py
"""
This code was taken from the assignment for a base and then modified to meet the requirements of
the assignment.
"""

import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket successfully created')
except socket.error as err:
    print('socket creation failed with error {}'.format(err))

# default port for socket
port = 9500

# bind to the port
s.bind(('localhost', port))
print('socket bound to {}'.format(port))

# put socket in listening mode
s.listen(5)
print('socket is listening...')

while True:
    # establish connection with client
    c, addr = s.accept()
    print('got connection from {}'.format(addr))

    # determine the output we are going to send back
    # recv() and send() require binary data to be sent and not string
    # if you want me to import struct to convert between types, I can do that
    # but the assignment said that advanced error checking wasn't necessary.
    # I didn't deem the b in the message to be an error
    if c.recv(1024) == b"Hello":
        c.send(b'Hi')
    else:
        c.send(b'Goodbye')

    # Close the connection
    c.close()
