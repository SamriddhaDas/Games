

"""
Rock, paper, Scissor Game
---------------------------
How to play:
# The player competes against the computer
# Both choose either Rock, Paper or Scissor.
# Rules:
    Rock beats scissor
    Scissor beats paper
    Paper beats rock
# Enter your choice when prompted
# The game keeps score of your win, loss and tie
# You can play as many round as want
# Enter 'exit' anytime to quit

Enjoy the game!
"""
import random
#Function: display menu
def display_menu():
    print("\n--- Rock, Paper, Scissor ---")
    print("Type 'rock', 'paper' or 'scissor' to play")
    print("Rules: \n\tRock beats scissor \n\tScissor beats paper \n\tPaper beats rock")
    print("Type 'exit' to quit the game")
    print("----------------------------------------")

# Function: get computer's choice
def computer_choice():
    return random.choice(["rock", "paper", "scissor"])

# Function: determine winner
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissor") \
         or (player == "paper" and computer == "rock") \
         or (player == "scissor" and computer == "paper"):
        return "win"
    else:
        return "loss"

# Function: play one round
def play_round():
    player = input("\nYour choice: ").strip().lower()
    
    if player == "exit":
        return None  # exit condition
    elif player not in ["rock", "paper", "scissor"]:
        print("Invalid input! Please choose 'rock', 'paper', or 'scissor'.")
        return "invalid"
    
    computer = computer_choice()
    print(f"Computer chose: {computer}")
    
    result = determine_winner(player, computer)
    if result == "win":
        print(" You win this round!")
    elif result == "loss":
        print("You lose this round.")
    else:
        print("It's a tie.")
    
    return result

# Main game loop
def main():
    wins, losses, ties = 0, 0, 0
    display_menu()
    
    while True:
        result = play_round()
        
        if result is None:  # player chose to exit
            print("\nThanks for playing!")
            print(f"Final Score: {wins} Wins | {losses} Losses | {ties} Ties")
            break
        elif result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        elif result == "tie":
            ties += 1
        
        # Display current score after each round
        print(f"Score: {wins} Wins | {losses} Losses | {ties} Ties")

# Run the game
if __name__ == "__main__":
    main()

