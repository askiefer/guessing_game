# Put your code here
name = raw_input("Welcome! What's your name?")

from random import randint
number = randint(1,100)

print "Howdy, %s! I'm thinking of a number between 1 and 100." %(str(name))

guess = int(raw_input("What's your guess?"))

while guess != number: 
    if guess > number:
        print "You guessed too high!"
        guess = int(raw_input("What's your guess?"))
    else:
        print "You guessed too low!"
        guess = int(raw_input("What's your guess?"))

if guess == number: 
    print "You guessed it! Good job!"