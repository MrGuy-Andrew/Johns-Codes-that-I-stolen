import random

# Options of item you'll find in a school playground
play = ["Rock", "Paper", "Scissors"]

# This function ask the user's input(rock, paper, scissors)
def your_rps():
    player = input("CHOOSE YOUR ITEM: ")
    computer = play[random.randint(0, 2)]
    if player == "":
        print("PLEASE TYPE SOMETHING")
    elif player == computer:
        print(f"TIE! The computer also chose {computer}")
    elif player == "Rock":
        if computer == "Paper":
            print(f"YOU LOSE! The computer chose {computer}")
        else:
            print(f"YOU WIN! The computer chose {computer}")
    elif player == "Paper":
        if computer == "Scissors":
            print(f"YOU LOSE! The computer chose {computer}")
        else:
            print(f"YOU WIN! The computer chose {computer}")
    elif player == "Scissors":
        if computer == "Rock":
            print(f"YOU LOSE! The computer chose {computer}")
        else:
            print(f"YOU WIN! The computer chose {computer}")
    else:
        print("INVALID CHOICE. PLEASE CHOOSE ROCK, PAPER OR SCISSORS.")

your_rps()