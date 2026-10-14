import random 
playing = True
number = str(random.randint(0,9))


print ("I will generrate a number from 0 to 9,and you have to guess the number one digit at a time")
while playing:
    guess = input("Give me your best guess! /n")
    if number == guess:
        print("you win the game")
        print("The number was",number) 
        break

    else:
        print("your guess isn't quite right,try again /n")