message=input("Enter the message for Encrypt : ")
print("\n")
encrypt=True
messages=message.split()
mesage_list=[]
if (encrypt == True):
    for msg in messages :
        i=len(msg)        
        if(i>=3):
            rand1="Am@#4_*kliTms"
            rand2="Rthxshsi*&65k"
            new_msg=rand1+msg[1:]+rand2+msg[0]+"1245"        

        if(i<3):
            rand3="@#4uyeg"
            new_msg=rand3+msg[::-1]
        mesage_list.append(new_msg)
    print(" ".join(mesage_list))
            
            
