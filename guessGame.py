import random

print("HELLO!! WELCOME TO OUR LITTLE GAME")
print("I think about a number and you have to guess it")

mistakes = 3
len = 5
guess = 0

#get random number
rdn_num = random.randint(0, len)

while(guess != rdn_num):
    print("What is your guess?")
    guess = input("guess")
    
    if(guess == rdn_num):
        print("You are right!")
