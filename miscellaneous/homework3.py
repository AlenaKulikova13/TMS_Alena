
#3 stone_scissors_paper_bot_game

import random
your_options = input("Choose your weapon: stone, scissors, paper: ").lower()
bots_options = random.choice(['stone', 'scissors', 'paper'])
if bots_options == your_options:
    print(f"You both gave {your_options} - it's a Draw")
elif bots_options == 'paper':
    if your_options == 'stone':
        print("Your choice is stone, bot's is paper - bot won")
    else:
        print("Your choice is scissors, bot's is paper - you won")
elif bots_options == 'scissors':
    if your_options == 'paper':
        print("Your choice is paper, bot's is scissors - bot won")
    else:
        print("Your choice is stone, bot's is scissors - you won")
elif bots_options == 'stone':
    if your_options == 'paper':
        print("Your choice is scissors, bot's is stone - bot won")
    else:
        print("Your choice is paper, bot's is stone - you won")
