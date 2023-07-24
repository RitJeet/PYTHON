import socket
import threading 
import os
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket created")
s.bind(("127.0.0.1",9999))

s.listen(1)
c , addr=s.accept()
print("Connected")
print(addr)
timea=time.strftime("%H:%M")
def send():
    while True:  
        msg="[Jeet] - "+input()
        msg=msg.encode()
        c.send(msg)

def recieve():
    while True:
        msg_r=c.recv(1024)
        msg_r=msg_r.decode()
        print(f"{msg_r}  {[timea]}")
            #s.close()
t1=threading.Thread(target=send)
t1.start()
#t2.start()
recieve()