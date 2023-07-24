import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',9991))
while 1:
    mesage=input("Enter message : ")
    c.send(bytes(mesage,'utf-8'))
    print(c.recv(2048).decode())