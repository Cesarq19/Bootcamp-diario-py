# Include the imports
import random as rd

# Define variables and constants
logo = """
    
 _______           _______  _______  _______ _________ _        _______    _______  _______  _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \\__   __/( (    /|(  ____ \  (  ____ \(  ___  )(       )(  ____ \\
| (    \/| )   ( || (    \/| (    \/| (    \/   ) (   |  \  ( || (    \/  | (    \/| (   ) || () () || (    \/
| |      | |   | || (__    | (_____ | (_____    | |   |   \ | || |        | |      | (___) || || || || (__    
| | ____ | |   | ||  __)   (_____  )(_____  )   | |   | (\ \) || | ____   | | ____ |  ___  || |(_)| ||  __)   
| | \_  )| |   | || (            ) |      ) |   | |   | | \   || | \_  )  | | \_  )| (   ) || |   | || (      
| (___) || (___) || (____/\/\____) |/\____) |___) (___| )  \  || (___) |  | (___) || )   ( || )   ( || (____/\\
(_______)(_______)(_______/\_______)\_______)\_______/|/    )_)(_______)  (_______)|/     \||/     \|(_______/
                                                                                                              
"""
mensaje = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
"""
target_number = rd.randint(0,100)
attemps = 0

# Define functions
def too_high():
    print("Too high. \nGuess again")
def too_low():
    print("Too low. \nGuess again")
def game():
    lives = 0
    for i in range(attemps):
        lives = attemps - i
        print(f"You have {lives} remaining to guess the number.")
        guess = input("Make a guess: ")
        if(int(guess) > target_number):
            too_high()
        elif(int(guess) < target_number):
            too_low()
        else:
            print(f"You got it! The answer was {target_number}")
            break

    if (lives == 1):
        print("You've run out of guesses, you lose.")

# Logic 
print(logo)

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if (choice.lower() == "easy"):
    attemps = 10
else:
    attemps = 5

game()