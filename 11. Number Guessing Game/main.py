import random # For choosing random number between 1 to 100
from art import logo # Imports logo from art file
from clear import clean # For cleaning the console
EASY_LEVEL_LIVES = 10 # Constant
HARD_LEVEL_LIVES = 5 # Constant

def checker(lives, guess, number):
    ''' Checks whether you're guessing correctly'''
    
    if guess == number:
        print(f"Congrats!🥳 You've guessed it right with {lives} lives remaining. You genius!")
    elif guess>number-10 and guess<number:
        print("You're very close but a little low! Keep up :)\n")
        return lives-1
    elif guess<number+10 and guess>number:
        print("You're very close but higher than the number! Keep up :)\n")
        return lives-1
    elif guess<number-10:
        print("You're guessing it too low :(\n")
        return lives-1
    else:
        print("You're guessing it too high :(\n")
        return lives-1

def set_difficulty(choosen):
    ''' Sets the difficulty level '''
    if choosen=='easy':
        return EASY_LEVEL_LIVES
    elif choosen == 'hard':
        return HARD_LEVEL_LIVES
    else:
        print("\nEnter a valid response!😡")
        return set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())

def set_number():
    ''' Sets a random number to be choosen to play the game around with'''
    return random.randint(1,100)

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100...")
    number = set_number()
    lives = int(set_difficulty(input("\nChoose a difficulty. Type 'easy' or 'hard': ")))
    game_on = True
    while game_on:
        print(f"\nYou have {lives} lives remaining.🧬")
        guess = int(input("Make a guess: "))
        lives = checker(lives, guess, number)
        if guess == number:
            game_on = False
        elif lives == 0:
            game_on = False
            print("Uh oh!😵 You ran out of lives😇")
        elif lives == 1: 
            print("Come on! You have just one attempt remaining😰")

game()
while input("\nDo you want to play the game again? Type 'yes' to play again or 'no' to exit: ")=='yes':
    clean()
    game()
print("Thanks for playing this game🚀")