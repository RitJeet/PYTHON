import socket
import threading
import os
import time
print("--------------------------------") 
print("|Message is not encrypted|")
print("--------------------------------")
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("192.168.56.1",4455))
print("Connnected with Jeet")
timea = time.strftime("%H:%M")
def send():
   while True:
      m_sg=input()
      if m_sg == "quit":
         print("Connection end with Jeet")
         m_sg=m_sg.encode()
         c.send(m_sg)
         os.system("clear")
         time.sleep(2)
         print("---------------------------")
         print("This Project Made By Jeet And His Wife Rittwika")
         print("-----------------------------")
         time.sleep(2)
         print("Thanks For Using This Project")
         print("***********    ***********")
         
      else:
         msg="[Rit] - "+m_sg
         msg=msg.encode()
         c.send(msg)   

def recieve():
   while True:
      msg_r=c.recv(1024)
      msg_r1=msg_r.decode()
      print(f"{msg_r1}  {[timea]}")
t1=threading.Thread(target=send)
t1.start()
recieve()

            
