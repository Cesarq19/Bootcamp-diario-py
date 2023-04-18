# Import needed libraries
import random as rd
import os
from art import *
from game_data import data

register = data.copy()

# Functions 
def initialize():
    index_one = rd.randint(0, len(register) - 1)
    first_person = register[index_one]
    register.pop(index_one)

    index_two = rd.randint(0, len(register) - 1)
    second_person = register[index_two]
    register.pop(index_two)

    return [first_person, second_person]

def actualize_list(options):
    index_random = rd.randint(0, len(register) - 1)
    actual = list()
    actual.append(options[1])
    actual.append(register[index_random])
    register.pop(index_random)
    return actual

def correct_election(option_one, option_two):
    if option_one > option_two:
        return "a"
    else:
        return "b" 
    
def lost_message(score):
    os.system("cls")
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

def game():
    player_score = 0
    game_status = True

    options = initialize()

    while game_status:
        op1_name, op1_description, op1_followers, op1_country = options[0]["name"], options[0]["description"], options[0]["follower_count"], options[0]["country"]
        op2_name, op2_description, op2_followers, op2_country = options[1]["name"], options[1]["description"], options[1]["follower_count"], options[1]["country"]

        os.system("cls")

        print(len(register))
        print(logo)

        if(player_score > 0):
            print(f"You're right! Current score: {player_score}.")
        
        print(f"Compare A: {op1_name}, a {op1_description}, from {op1_country}.")
        print(vs)
        print(f"Against B: {op2_name}, a {op2_description}, from {op2_country}.")

        # Line for tests
        print(op1_followers, op2_followers)

        election = input("Who has more followers? Type 'A' or 'B': ")

        more_followers = correct_election(op1_followers, op2_followers)

        if (election.lower() == more_followers):
            player_score += 1
            options = actualize_list(options)

        else:
            game_status = False

    lost_message(player_score)
    
# Main program
game()