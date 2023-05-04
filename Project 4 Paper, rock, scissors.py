import random

print('Welcome to the Paper, Scissors, Rock Game! Who is going to win?\n\n')

#variables using ASCII
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

#User's choice (input):
users_choice = input('What should it be? Rock, paper, scissors?\n').lower()
if users_choice == 'paper':
  print(paper)
elif users_choice == 'rock':
  print(rock)
else:
  print(scissors)

#Computer's choice (random):
options = ['rock', 'paper', 'scissors']
len = len(options)
computers_choice = random.randint(0, len-1)
if computers_choice == options[0]:
  print(rock)
elif computers_choice == options[1]:
  print(paper)
else:
  print(scissors)

print("Let's check the result!")

#The result:
if users_choice == 'paper':
  if computers_choice == options[0]:
    print('You won!')
  elif computers_choice == options[1]:
    print("It's a draw!")
  else: #computers_choice == options[2]:
    print('You lost!')
elif users_choice == 'scissors':
  if computers_choice == options[0]:
    print('You lost!')
  elif computers_choice == options[1]:
    print("You won!")
  else: #computers_choice == options[2]:
    print("It's a draw!")
elif users_choice == 'rock':
  if computers_choice == options[0]:
    print("It's a draw!")
  elif computers_choice == options[1]:
    print("You lost!")
  else: #computers_choice == options[2]:
    print("You won!")
else:
  print('Error')