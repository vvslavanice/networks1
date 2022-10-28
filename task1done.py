import socket


Host = '127.0.0.1'
Port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((Host, Port))
    sent_message = input('Enter your message here: ')
    s.sendall(sent_message.encode('utf-8'))
    recv_message = s.recv(4096)

    print('Recieved:', recv_message)