# Import needed libraries
import random as rd
from art import *
from game_data import data


# Functions 
def choices_select():
    return rd.choices(data,k=2)
# Main program
print(choices_select())