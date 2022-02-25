# BlackJack Game
import random
# Random for choosing the card with random.choice
from art import logo

def deal_card():
    """ Returns a card by dealer"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(stack):
    """ Calculates the score and returns it"""
    score = sum(stack)
    if score == 21 and len(stack) == 2:
        return 21
    if 11 in stack and score>21: 
        stack.remove(11)
        stack.append(1)
    return score

def compare(user_score, ai_score):
    # Compares both players' score and prints the output
    if user_score>21 and ai_score>21:
        print("You both went over, it's a draw🤝🏽")
    elif user_score == ai_score:
        print("It's a draw👍🏽")
    elif ai_score == 0:
        print("BlackJack! Ai wins😵")
    elif user_score == 0:
        print("BlackJack! You win💫")
    elif user_score>21:
        print("You went over 21, you lose😭")
    elif ai_score>21:
        print("Ai went over 21, you win🚀")
    elif user_score>ai_score:
        print("You win😁")
    else:
        print("You lose🫂")

def play_game():
    """ Starts BlackJack game """
    print(logo)
    user =[]
    ai = []
    game_on = True

    # Deals two cards to both players
    for _ in range(2):
        user.append(deal_card())
        ai.append(deal_card())

    # Game starts
    while game_on:
        user_score = calculate_score(user)
        ai_score = calculate_score(ai)
        print(f"Your cards: {user}\nCurrent score: {user_score}")
        print(f"Ai's first card: {ai[0]}")

        # Checking if you're already lucky
        if user_score == 0 or ai_score == 0 or user_score>21:
            game_on= False
        # If you move to this one, guess you're not so lucky this game, but don't lose hope!
        else:
            if input("\nType 'y' to get another card or 'n' to pass: ") == 'y':
                user.append(deal_card())
            else:
                game_on = False
    # letting ai deal a card if score not over 17 or it got 21
    while ai_score !=0 and ai_score<17:
        ai.append(deal_card())
        ai_score = calculate_score(ai)

    print(f"\n   Your final hand: {user}   Your final score: {user_score}")
    print(f"   Ai's final hand: {ai}    Ai final score: {ai_score}")
    compare(user_score, ai_score)

i=0
while input("Do you want to play BlackJack? Type 'y' or 'n': ")=='y':
    play_game()
    i += 1
    print()
if i==0:
    print("Then why did you execute the program?🤔")
else:
    print("Thanks for playing this game :) \nExiting...")