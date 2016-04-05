# Put your code here
name = raw_input("Welcome! What's your name?")

from random import randint

#greeting 
print "Howdy, %s! I'm thinking of a number between 1 and 100." %(str(name))

#function that chooses a number between 1 and 100
def pick_number():
    number = randint(1,100)
    return number

number = pick_number()

#function that asks for a guess and checks whether it's an integer 
def new_guess():
    while True:
        try:
            guess = int(raw_input("What's your guess? "))
            break
        except ValueError:
            print "Dummy! That's not an integer! Try again."
    return guess 

#feedback on guesses until game is won
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
        play_again = raw_input("Would you like to play again? y/n: ")
        if play_again == 'y':
            print "I've picked a new number."
            number = pick_number()
        else:
            print "Thanks for playing!"
            break