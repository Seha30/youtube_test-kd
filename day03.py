print("Welcome!To Guess the number game")
print("I'm thinking a number between 1 and 20,You have Five chances to win")

import random

#Generate a random number
random_number = random.randint(1,20)

#track inserted numbers
count=0
guesess=[]

#Allow up to 5 attempts
while(count<5):
    
        num=int(input(f"Take a guess:"))
        count+=1
        guesess.append(num)
        
        if num==random_number:
             print("Congratulations!Your guess is correct") 
             break
        elif num < random_number:
             print("Your guess is too low")
        else:   
            print("Your guess is too high")
            
if count==5 and num!=guesess:
    print("Sorry,You've run out of tries.The secret number was ",random_number)