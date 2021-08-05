import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

r = [rock, paper, scissors]

print("Let's play Rock, Paper, Scissors")
choice = input("Choice please:\n").lower()
Ai = random.choice(r)

#printing the art for choice taken
if choice == "rock":
    print(rock)
    print("Computer chose:")
    print(Ai)
elif choice == "paper":
    print(paper)
    print("Computer chose:")
    print(Ai)
elif choice == "scissors":
    print(scissors)
    print("Computer chose:")
    print(Ai)
else:
    print("You lose, invalid number")

# Comparison to determine who won!
if choice == "rock" and Ai == paper:
    print("You lose.")
elif choice == "rock" and Ai == rock:
    print("Draw.")
elif choice == "rock" and Ai == scissors:
    print("You win.")
elif choice == "paper" and Ai == paper:
    print("Draw.")
elif choice == "paper" and Ai == rock:
    print("You win.")
elif choice == "paper" and Ai == scissors:
    print("You lose.")
elif choice == "scissors" and Ai == rock:
    print("You lose.")
elif choice == "scissors" and Ai == paper:
    print("You win.")
elif choice == "scissors" and Ai == scissors:
    print("Draw.")
