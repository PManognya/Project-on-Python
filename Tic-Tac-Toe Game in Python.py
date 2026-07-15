#Tic-Tac-Toe Game in Python
def display_board(board):
    print(f"{board[7]}|{board[8]}|{board[9]}")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print(f"{board[1]}|{board[2]}|{board[3]}")

def check_win(board, mark):
    win_combos = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
        (1, 5, 9), (3, 5, 7)              # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False

def is_board_full(board):
    return all(board[i] != " " for i in range(1, 10))

def play_game():
    board = {i: " " for i in range(1, 10)}
    current_player = "X"

    while True:
        display_board(board)
        print(f"\nPlayer {current_player}, it's your turn.")

        while True:
            try:
                position = int(input("Choose a position (1-9): "))
                if position not in board or board[position] != " ":
                    print("That position is taken or invalid. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a number between 1 and 9.")

        board[position] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"\n🎉 Player {current_player} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("\nIt's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

    print("\nGame over!")

if __name__ == "__main__":
    play_game()