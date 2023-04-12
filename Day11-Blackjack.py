############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import os
import random as rd

# Art for this game
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

programa = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def obtenerMazo():
    score = 0
    mazo = list()

    for i in range(2):
        mazo.append(rd.choice(cards))
        score += mazo[i]
    return (mazo, score)


while programa:
    inicio = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if inicio.lower() == "y":
        os.system("cls")
        print(logo)
        playerMazo, playerScore = obtenerMazo()
        computerMazo, computerScore = obtenerMazo()

        print(f"    Your cards: {playerMazo}, current score: {playerScore}")
        print(f"    Computer's first card: {computerMazo[0]}")

        pedir = True

        while pedir:
            opcion = input("Type 'y' to get another card, type 'n' to pass: ")
            if opcion.lower() == "y":
                playerMazo.append(rd.choice(cards))
                playerScore = sum(playerMazo)

                if playerScore > 21:
                    pedir = False
                else:
                    print(f"    Your cards: {playerMazo}, current score: {playerScore}")
            else:
                pedir = False

        if playerScore <= 21:
            while playerScore > computerScore and computerScore < 22:
                computerMazo.append(rd.choice(cards))
                computerScore = sum(computerMazo)
            if computerScore <= 21:
                if playerScore > computerScore:
                    print(
                        f"    Your final hand: {playerMazo}, final score: {playerScore}"
                    )
                    print(
                        f"    Computer's final hand: {computerMazo}, final score: {computerScore}"
                    )
                    print("Opponent went over. You win 😎")
                elif computerScore == playerScore:
                    print(
                        f"    Your final hand: {playerMazo}, final score: {playerScore}"
                    )
                    print(
                        f"    Computer's final hand: {computerMazo}, final score: {computerScore}"
                    )
                    print("Nothing went over. Draw 🤯")
                else:
                    print(
                        f"    Your final hand: {playerMazo}, final score: {playerScore}"
                    )
                    print(
                        f"    Computer's final hand: {computerMazo}, final score: {computerScore}"
                    )
                    print("You went over. You lose 😭")
            else:
                print(f"    Your final hand: {playerMazo}, final score: {playerScore}")
                print(
                    f"    Computer's final hand: {computerMazo}, final score: {computerScore}"
                )
                print("Opponent went over. You win 😎")
        else:
            print(f"    Your final hand: {playerMazo}, final score: {playerScore}")
            print(
                f"    Computer's final hand: {computerMazo}, final score: {computerScore}"
            )
            print("You went over. You lose 😭")
    else:
        programa = False
