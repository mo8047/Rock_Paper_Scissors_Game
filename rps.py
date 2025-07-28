import random

u_input = input("Would you like to play(y/n): ")
while u_input == "y":
    u_input = input("Rock, Paper, Scissors?: ")
    computer = ["Rock", "Paper", "Scissors"]
    

    Rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
    
    # Paper
    Paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
    
    # Scissors
    Scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
    
    ascii_art = {
        "Rock":Rock,
        "Paper":Paper,
        "Scissors":Scissors
    }
    
    computer_rps = random.choice(computer)
    print(computer_rps)
    
    if u_input == computer_rps:
        print("It's a draw")
    elif u_input == "Rock" and computer_rps == "Scissors":
        print("User Wins")
    elif u_input == "Paper" and computer_rps == "Rock":
        print("User Wins")
    elif u_input == "Scissors" and computer_rps == "Paper":
        print("User Wins")
    else:
        print("Computer Wins")
    
        
    computer_art = ascii_art[computer_rps]
    print(computer_art)
    u_input = input("Would you like to play(y/n): ")
