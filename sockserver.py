import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print("Socket server created")
s.bind(('localhost',9991))
s.listen(1)
print("Waitng for connections")
while 1:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print(name)
    mesage=input("Enter message : ")
    c.send(bytes(mesage,'utf-8'))
    c.close