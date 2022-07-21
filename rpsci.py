import random

def rpsplay(x):
    user = input('Enter choice:(r for rock,p for paper,s for scissors')
    computer_guess = random.choice(['r','p','s'])

    if computer_guess == user:
        return 'tie'
    

def is_win()
    