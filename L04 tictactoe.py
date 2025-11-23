import random
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def display_board(board):
    print()
    print(' ' + format_symbol(board[0]) + ' | ' + format_symbol(board[1]) + ' | ' + format_symbol(board[2]))
    print(Fore.CYAN + '-----------')
    print(' ' + format_symbol(board[3]) + ' | ' + format_symbol(board[4]) + ' | ' + format_symbol(board[5]))
    print(Fore.CYAN + '-----------')
    print(' ' + format_symbol(board[6]) + ' | ' + format_symbol(board[7]) + ' | ' + format_symbol(board[8]))
    print()

def format_symbol(symbol):
    if symbol == 'X':
        return Fore.RED + symbol + Fore.RESET
    elif symbol == 'O':
        return Fore.BLUE + symbol + Fore.RESET
    else:
        return Fore.YELLOW + symbol + Fore.RESET

def player_choice():
    symbol = ''
    while symbol not in ['X','O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? ").upper()

    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move(board, symbol, player_name):
    move = -1
    while move not in range(1,10) or not board[move - 1].isdigit():
        try:
            move = int(input(Fore.GREEN + f"{player_name}, enter your move (1-9): "))
            if move not in range(1,10) or not board[move - 1].isdigit():
                print(Fore.RED + "Invalid move. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a number between 1 and 9.")
    board[move - 1] = symbol

def ai_move(board, ai_symbol, player_symbol):
    # Check if AI can win in the next move
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
            
    # Check if player could win on their next move, and block them
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
            
    # Choose a random move
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # Vertical
        (0, 4, 8), (2, 4, 6)                # Diagonal
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

def check_full(board):
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    print(Fore.YELLOW + "Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.GREEN + "Please enter your name: ")
    
    while True:
        board = ['1','2','3','4','5','6','7','8','9']
        player_symbol,ai_symbol  = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol, player_name)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"Congratulations, {player_name}! You have won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print(Fore.YELLOW + "It's a tie!")
                        break
                    else:
                        turn = 'AI'
            else:
                print(Fore.BLUE + "AI is making its move...")
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI has won the game!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print(Fore.YELLOW + "It's a tie!")
                        break
                    else:
                        turn = 'Player'
        play_again = input(Fore.GREEN + f"{player_name}, do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(Fore.CYAN + "Thank you for playing{player_name}!")
            break

if __name__ == "__main__":
    tic_tac_toe()