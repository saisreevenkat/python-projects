# Tic Tac Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to display the game board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()
        print("It's", current_player, "turn.")

        # Get player input
        while True:
            position = int(input('Enter a position (1-9): ')) - 1
            if position >= 0 and position < 9 and board[position] == ' ':
                break
            print('Invalid position. Try again.')

        # Update the board
        board[position] = current_player

        # Check for a win
        if check_win(current_player):
            display_board()
            print('Player', current_player, 'wins!')
            game_over = True
        elif is_board_full():
            display_board()
            print("It's a tie!")
            game_over = True

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
