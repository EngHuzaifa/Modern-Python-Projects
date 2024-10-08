import random
from typing import List

def print_board(board: List[str]) -> None:

    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board: List[str], player: str) -> bool:
    
    win_conditions: List[List[int]] = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def get_available_moves(board: List[str]) -> List[int]:
    
    return [i for i, spot in enumerate(board) if spot == ' ']

def make_move(board: List[str], position: int, player: str) -> None:
    
    board[position] = player

def player_turn(board: List[str]) -> None:
    
    while True:
        try:
            move: int = int(input("Choose your move (1-9): ")) - 1
            if move in get_available_moves(board):
                make_move(board, move, 'X')
                break
            else:
                print("That spot is already taken or invalid. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def computer_turn(board: List[str]) -> None:
   
    move: int = random.choice(get_available_moves(board))
    make_move(board, move, 'O')
    print(f"Computer chose position {move + 1}")

def tic_tac_toe() -> None:
    """Main function to run the Tic-Tac-Toe game."""
    board: List[str] = [' '] * 9
    current_player: str = 'X'  # Player starts first

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        if current_player == 'X':
            player_turn(board)
            if check_winner(board, 'X'):
                print_board(board)
                print("🎉 Congratulations! You win!")
                return
            current_player = 'O'
        else:
            computer_turn(board)
            if check_winner(board, 'O'):
                print_board(board)
                print("💻 Computer wins! Better luck next time.")
                return
            current_player = 'X'
        print_board(board)

    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
