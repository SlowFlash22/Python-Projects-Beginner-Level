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
import random
r=[paper, scissors, rock]
choice=int(input("Enter your choice: 0 for paper, 1 for scissors, 2 for rock"))
if choice>=3 or choice<0:
  print("You lose due to invalid choice")
else:
  print("Your choice:")
  print(r[choice])
  Ai=random.randint(0,2)
  print("Computer chose:")
  print(r[Ai])
  if choice==0 and Ai==2:
    print("You win")
  elif Ai==0 and choice==2:
    print("You lose.")
  elif choice<Ai:
    print("You lose.")
  elif choice>Ai:
    print("You win")
  else:
    print("It's a draw")