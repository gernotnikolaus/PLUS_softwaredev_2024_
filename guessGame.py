##################################
#### STILL UNDER CONSTRUCTION ####
##################################

import random

print("HELLO!! WELCOME TO OUR LITTLE GAME")
print("I think about a number and you have to guess it")

mistakes = 3
len = 5
guess = 0

#get random number
rdn_num = random.randint(1, len)
print(rdn_num)


print("while")
if(guess != rdn_num):
    print("What is your guess?")
    guess = input("guess")
    check(guess)
else:
    print("You are out!")
    
def check(input):
    if(input == rdn_num):
        print("You are right!")
    else:
        mistakes = mistakes - 1
        print("You have " + mistakes + " tries left!")
    
