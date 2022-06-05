#Ifeoluwa Ogungbemi I4G000988ANZ
#Rock-paper-scissors

import random

#Create list for possible inputs and corresponding options
inputs = ['R', 'P', 'S']
options = ['Rock', 'Paper', 'Scissors']

print("Welcome to the Rock-paper-scissors game")

#Loop the program to allow for automatic restart in case of ties, and also to ensure re-input
while True:
    print("*******************************")
    print('Select your choice: \n 1. R for Rock \n 2. P for Paper \n 3. S for Scissors')
    user_input = input("Your choice: ")
    user_input = user_input.upper() #Changes the user input to uppper case in order to match with the list items
    if user_input not in inputs:
        print('Not a valid option. Try again!')
        continue

#Validate Computer choice and User Choice
    comp_choice = random.choice(options)
    if user_input == 'R':
        user_choice = options[0]
    elif user_input == 'P':
        user_choice = options[1]
    elif user_input == 'S':
        user_choice = options[2]

    print("Player("+user_choice+") : CPU("+comp_choice+")")
    print("*******************************")

#Check both players move to determine the winner
    if user_choice == comp_choice:
        print("It's a tie. Let's start again")
        continue
    elif (user_choice == 'Rock' and comp_choice == 'Paper') or (comp_choice == 'Rock' and user_choice == 'Paper'):
        winner = 'Paper'
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or (comp_choice == 'Rock' and user_choice == 'Scissors'):
        winner = 'Rock'
    else:
        winner = 'Scissors'

#COnfirms the winner and quit afterwards
    if winner == user_choice:
        print("User wins")
        quit()
    else:
        print("Computer wins")
        quit()
