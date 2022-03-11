import random
chance=0
number=random.randint(1,9)
print("Guess a number between 1-9")
guess= int (input("type your guess: "))
g="t"
game=1
while chance<5:
    if(guess==number):
        print("You Won")
        break
    else:
        if(guess>number):
            print("Think of a number less than ",guess)
        else:
        
            print("Think of a number more than ",guess)
        guess= int (input("type your guess: "))
        chance+=1
if(chance==5):    
    print("Game Over The number was",number)

   
       
  
  