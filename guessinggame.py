import random

name = input("What is your name? ")
print(f"Welcome to the number guessing game!{name}\n")


def guess(x):
    rand_num = random.randint(1, x)
    guess_int = 0
    while guess_int != rand_num:
        guess_int = int(input("Guess a number between 1 and " + str(x) + ": "))
        if guess_int > rand_num:
            print("Too high!")
        elif guess_int < rand_num:
            print("Too low!")
        else:
            print(f"You guessed {guess_int} correctly!")
#

guess(10)

def guessagain(x):
    feedback = input("Would you like to play again? (y/n) ")
    if feedback == "y":
        rand_num = random.randint(1, x)
        guess_int = 0
        while guess_int != rand_num:
            guess_int = int(input("Guess a number between 1 and " + str(x) + ": "))
            if guess_int > rand_num:
                print("Too high!")
            elif guess_int < rand_num:
                print("Too low!")
            else:
                print(f"You guessed {guess_int} correctly!") 
    else:
        print("Thanks for playing!")

guessagain(10)

def letmeguess(x):
    low = 0
    high = x
    feedback = ''
    while feedback != "correct" and low != high:
        guess = random.randint(low, high)
        feedback = input(f"Is my number {guess}? (high/low/correct)".lower())
        if feedback == "high":
            high = guess - 1
        elif feedback == "low":
            low = guess + 1
       
    print("Yay! I guessed your number!")

letmeguess(100)