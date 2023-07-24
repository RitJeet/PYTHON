price=1000
listquetion=[" 1. What is the capital of India?" , " 2. What is capital of Spain?"]
listanswer=[" a. Delhi" , " b. Mumbai" , " c. Kolkata" , " d. Madrid"]
#b=1
def answer(a,price):
    for j in range(4):
        print(listanswer[j])
        print("\n")
    c=answeruser(a,price)
    return c
def funcquestion(a,listquetion,price):    
    print(listquetion[a])
    c=answer(a,price)
    return c
def answeruser(a,price):    
    print("Choose any option \n")
    print("option a.\noption b.\noption c.\noption d.")
    ans=input("Chose any option :")
    if a==0 :
        if ans=="a":
            price=10000            
            print("Your chose  answer is correct\n")
            print("Now your price is ",price)            
            #b=b+1
        else:          
            print("Your answer is wrong\n")
            c=2
            return c
           
   
    if a==1:
        if ans=="d":
            price=100000
            print("Your chose  answer is correct\n")
            print("Now your price is ",price)
            c=2
            return c
        else:
            c=2
            print("Your answer is wrong\n")
            return c
c=1
e=0
while c==1:
       for e in range(2):        
         c=funcquestion(e,listquetion,price)
         if c==2:
             break

    

