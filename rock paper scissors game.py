import random

def play_game():
    print("Let's play Rock-Paper-Scissors!")
    print("Enter your move: (rock, paper, or scissors)")
    user_move = input().lower()
    computer_move = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose {user_move}")
    print(f"The computer chose {computer_move}\n")

    if user_move == computer_move:
        print("It's a tie!")
    elif (user_move == 'rock' and computer_move == 'scissors') or \
         (user_move == 'paper' and computer_move == 'rock') or \
         (user_move == 'scissors' and computer_move == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

play_game()
