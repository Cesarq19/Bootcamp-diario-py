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
opciones = [rock,paper,scissors]

election = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
computer_choice = random.randint(0,2)

print(opciones[int(election)])

print("Computer choice: ")
print(opciones[computer_choice])

if int(election) == 0:
    if computer_choice == 1:
        print("You lose.")
    elif computer_choice == 2:
        print("You win.")
    else:
        print("You tie.")
if int(election) == 1:
    if computer_choice == 2:
        print("You lose.")
    elif computer_choice == 0:
        print("You win.")
    else:
        print("You tie.")
if int(election) == 2:
    if computer_choice == 0:
        print("You lose.")
    elif computer_choice == 1:
        print("You win.")
    else:
        print("You tie.")

