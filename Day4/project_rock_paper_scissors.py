# Rock Paper Scissor Game using Randomization
import random

choices = ["Rock", "Paper", "Scissors"]
user_choice = int(input("What do you choose? "
               "Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice in [0,1,2]:
    computer_choice = random.randint(0,2)
    print(f"User Picked: {choices[user_choice]}")
    print(f"Computer Picked: {choices[computer_choice]}")
    if user_choice != computer_choice: 
        if user_choice == 0:
            if computer_choice == 2:
                print("You win")
            else:
                print("You lose")
        elif user_choice == 1:
            if computer_choice == 0:
                print("You win")
            else:
                print("You lose")
        else:
            if computer_choice == 1:
                print("You win")
            else:
                print("You lose")
    else:
        print("Draw")
else:
    print("Invalid choice")

