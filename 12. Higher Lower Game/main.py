import art
from game_data import data
import random
from clear import clean

def data_maker():
    '''Retrieves and arranges data taken from data file''' 
    A = random.choice(data)
    B = random.choice(data)
    if A == B:
        B = random.choice(data)
    
    return [f"{A['name']}, {A['description']}, from {A['country']}", f"{B['name']}, {B['description']}, from {B['country']}", A['follower_count'], B['follower_count']]

def compare(user_inp, A, B, score):
    ''' Checks the user input '''
    if user_inp == 'A':
        if A>B:
            return score+1
        else:
            return score-1
    elif user_inp == 'B':
        if B>A:
            return score+1
        else:
            return score-1
    else:
        print("You gave an invalid input, didn't you? Guess the game's over for you😡")
        return 420


def game():
    ''' Starts the game instance'''
    print(art.logo)
    score = 0
    game_on = True
    while game_on:
        A, B, A_counter, B_counter = data_maker()
        print(f"Compare A: {A}")
        print(art.vs)
        print(f"Against B: {B}")
        choosen = input("Who has more followers? Type 'A' or 'B': ").upper()
        new_score = compare(choosen, A_counter, B_counter, score)
        if score-1==new_score:
            game_on = False
            clean()
            print(f"Uh oh! You've guessed it wrong. Your score is {score}")
        elif new_score==420:
            game_on=False
        else:
            clean()
            score = new_score
            print(f"You've guessed it correctly! Your score: {score}")

game()
while input("Do you want to play 'Higher Lower' again? Type 'yes' or 'no': ")=='yes':
    clean()
    game()
print("Thanks for playing this game :)")