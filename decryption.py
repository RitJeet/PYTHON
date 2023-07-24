message=input("Enter the message for Decrypt : ")
print("\n")
print("Do you have any Decryption key???")
print("Enter the key : ")
key=input()
if(key=="I Love Jeet"):
    decrypt=True
else:
    raise ValueError("You Enter the Wrong Key!!!!!")
    print("You can not Decrypt any message\n")
    decrypt=False
messages=message.split()
mesage_list=[]
if (decrypt == True):
    for msg in messages :
        i=len(msg)        
        if(i>=31):           
             ex_msg=msg[13:-18]
             ex2_msg=msg[-5:-4]
             real_msg=ex2_msg+ex_msg             
             print(real_msg)            
        if(i<31):           
            temp_msg=msg[::-1]
            real_msg=temp_msg[:-7]
            print(real_msg)
        mesage_list.append(real_msg)
    print(" ".join(mesage_list))