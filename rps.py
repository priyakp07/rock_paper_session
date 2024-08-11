# ROCK PAPER SCISSOR GAME BY USING PYTHON

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice = Rock, Paper, Scissor:\n")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice},\nComputer choice = {comp_choice}\n")

if user_choice == comp_choice:
    print("Match tie\n\n")

elif user_choice == 'Rock':
    if comp_choice == 'Paper':
        print("Computer Won this match")

    else:
        print("You Won this match")


elif user_choice == 'Paper':
    if comp_choice == 'Scissor':
        print("Computer Won this match")

    else:
        print("You Won this match") 


elif user_choice == 'Scissor':
    if comp_choice == 'Paper':
        print("You Won this match")

    else:
        print("Computer Won this match")