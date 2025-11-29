import random
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def get_player_choice(player_name):
    """Get valid player choice (rock/paper/scissors)"""
    choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input(Fore.GREEN + f"{player_name}, enter your choice (rock/paper/scissors): ").lower()
        if choice in choices:
            return choice
        print(Fore.RED + "Invalid choice! Please enter rock, paper, or scissors.")

def get_ai_choice():
    """Generate random AI choice"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, ai_choice):
    """Determine the winner based on game rules"""
    # Game rules: rock > scissors, scissors > paper, paper > rock
    if player_choice == ai_choice:
        return "tie"
    elif (player_choice == 'rock' and ai_choice == 'scissors') or \
         (player_choice == 'scissors' and ai_choice == 'paper') or \
         (player_choice == 'paper' and ai_choice == 'rock'):
        return "player"
    else:
        return "ai"

def display_round_result(player_name, player_choice, ai_choice, winner):
    """Display colored round result"""
    print(Fore.CYAN + "\n--- Round Result ---")
    print(Fore.GREEN + f"{player_name}'s choice: {player_choice.upper()}")
    print(Fore.BLUE + f"AI's choice: {ai_choice.upper()}")
    print(Fore.CYAN + "---------------------")
    
    if winner == "tie":
        print(Fore.YELLOW + "It's a tie!")
    elif winner == "player":
        print(Fore.GREEN + f"Congratulations, {player_name}! You win this round!")
    else:
        print(Fore.RED + "AI wins this round!")
    print()

def rock_paper_scissors():
    """Main game loop"""
    print(Fore.YELLOW + "Welcome to Rock Paper Scissors!")
    player_name = input(Fore.GREEN + "Please enter your name: ")
    print(Fore.CYAN + f"\nHello {player_name}! Let's play against AI!")
    print(Fore.YELLOW + "Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock\n")

    while True:
        # Get choices
        player_choice = get_player_choice(player_name)
        print(Fore.BLUE + "AI is making its choice...")
        ai_choice = get_ai_choice()

        # Determine winner
        winner = determine_winner(player_choice, ai_choice)

        # Display result
        display_round_result(player_name, player_choice, ai_choice, winner)

        # Play again prompt
        play_again = input(Fore.GREEN + f"{player_name}, do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print(Fore.CYAN + f"Thank you for playing, {player_name}! Goodbye!")
            break

if __name__ == "__main__":
    rock_paper_scissors()