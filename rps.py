import random

u_input = input("Would you like to play(y/n): ")
while u_input == "y":
    u_input = input("Rock, Paper, Scissors?: ")
    computer = ["Rock", "Paper", "Scissors"]
    
    computer_rps = random.choice(computer)
    print(computer_rps)
    
    if u_input == "Rock":
        if computer_rps == "Rock":
            print(f"Computer chose {computer_rps}: It's a draw")
        elif computer_rps == "Paper":
            print(f"Computer chose {computer_rps}: Computer wins")
        elif computer_rps == "Scissors":
            print(f"Computer chose {computer_rps}: User wins")
        u_input = input("Would you like to play(y/n): ")
    elif u_input == "Paper":
        if computer_rps == "Rock":
            print(f"Computer chose {computer_rps}: User wins")
        elif computer_rps == "Paper":
            print(f"Computer chose {computer_rps}: It's a draw")
        elif computer_rps == "Scissors":
            print(f"Computer chose {computer_rps}: Computer wins")
        u_input = input("Would you like to play(y/n): ")
    elif u_input == "Scissors":
        if computer_rps == "Rock":
            print(f"Computer chose {computer_rps}: Computer wins")
        elif computer_rps == "Paper":
            print(f"Computer chose {computer_rps}: User wins")
        elif computer_rps == "Scissors":
            print(f"Computer chose {computer_rps}: It's a draw")
        u_input = input("Would you like to play(y/n): ")
    else:
        u_input = input("Wrong input: Try Again?(y/n): ")
