'''

Task1

'''


import socket

Host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((Host, port))
    data, addr = s.recvfrom(4096)
    if data:
        print('Connected', addr)
        s.sendto(data, addr)



