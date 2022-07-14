#snake water gun or rock paper scissors

import random

def gameWin(comp, you):
    #If two values are equal, declare a tie!
    if comp == you:
        return None

    #check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    #check for all possibilities when computer chose w
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    #check for all possibilities when computer chose w
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False

#computer's input using random
print("computer Turn: Snake(1) Water(2) or Gun(3)? ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'
    
#players input
you = input("Your Turn: Snake(s) Water(w) or Gun(g)? ")
a = gameWin(comp, you)

#final stats
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("You won the game!")
else:
    print("You lose")