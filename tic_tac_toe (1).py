import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

def check_win(board):
    win_conds = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for cond in win_conds:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] and board[cond[0]] != " ":
            return board[cond[0]]
    if " " not in board:
        return "Draw"
    return None

def main():
    board = [" "] * 9
    current_player = "X"
    while True:
        print_board(board)
        try:
            choice = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
            if board[choice] == " ":
                board[choice] = current_player
                result = check_win(board)
                if result:
                    print_board(board)
                    if result == "Draw":
                        print("It's a draw!")
                    else:
                        print(f"Player {result} wins!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                input("Position taken! Press Enter to try again.")
        except (ValueError, IndexError):
            input("Invalid input! Enter 1-9. Press Enter to try again.")

if __name__ == "__main__":
    main()
