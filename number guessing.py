import random

def guess_number():
    target_number = random.randint(1, 100)  # Generates a random number between 1 and 100
    attempts = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
            break
        elif user_guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

guess_number()
