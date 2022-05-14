import random

print("Welcome to Password Generator")

cherecters_for_Genarating_password = ("1234567890qwertyuiopasdfghjklzxcvnmQWERTYUIOPASDFGHJKLZXCVNM*&%$#@!")

    
NUM_PASSWORDS = int(input("How many passwords you have to create:- "))
    
#print(NUM_PASSWORDS)
    
Length_of_password = int(input("What should be the lenth of your password:- "))
    
print("So these are your passwords:- ")
#main code
for passw in range(NUM_PASSWORDS):
    password = ""
    for should_apply in range (Length_of_password):
        password += random.choice(cherecters_for_Genarating_password)
    print(password)
print("Are these passwords satisfying you Y/N")
satisfing = str(input())
        
if satisfing == "Y" or satisfying == "y":
    print("Ok sir Thanks")
elif satisfing == "N" or satisfying == "n":
    print("So these are your passwords Again:- ")
    for passw in range(NUM_PASSWORDS):
        password = ""
        for should_apply in range (Length_of_password):
            password += random.choice(cherecters_for_Genarating_password)
        print(password)
else:
    print("incorrect input")
      
      
