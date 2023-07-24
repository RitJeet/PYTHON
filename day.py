import time 
timestamp=time.strftime("%H:%M")
print(timestamp)
timestamp1=int(time.strftime("%H"))
if (timestamp1>3 and timestamp1<12):
    print("Good Mornig , Jeet")
elif(timestamp1>=12 and timestamp1<15):
    print("Good noon , Jeet")
elif(timestamp1>=15 and timestamp1<18):
    print("Good Afternoomn, Jeet")
elif(timestamp1>=18 and timestamp1<21):
    print("Good evening, Jeet")
elif(timestamp1>=21 and timestamp1<=23):
    print("Good night , Jeet")
else:
    print("This is midnight sir \n please stop your work \n and go to bed")        
