# Put your code here
name = raw_input("Welcome! What's your name?")

from random import randint
number = randint(1,100)

print "Howdy, %s! I'm thinking of a number between 1 and 100." %(str(name))

def new_guess():
    while True:
        try:
            guess = int(raw_input("What's your guess?"))
            break
        except ValueError:
            print "Dummy! That's not an integer! Try again."
    return guess 

while True: 
    guess = new_guess()
    if guess < 1 or guess > 100:
        print "You are dumb. Try again." 
    elif guess > number:
        print "You guessed too high!"
    elif guess < number:
        print "You guessed too low!"
    else:
        print "You guessed it! Good job!"
        break