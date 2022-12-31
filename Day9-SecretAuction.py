import os


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids = dict()
print("Welcome to the secret auction program.")
program = True
while program:
  name = input("What is your name?: ")
  bid = int(input("What's your bid? : $"))
  more_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  bids[name] = bid
  if(more_bidder=="yes"):
    os.system("cls")
  else:
    os.system("cls")
    program = False

winner_name = max(bids,key=bids.get)
print(f"The winner is {winner_name} with a bid of ${bids[winner_name]}")

