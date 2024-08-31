import random

def play_number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have a number in mind between 1 and 50.")

    low, high = 1, 50
    guess = None
    number_of_guesses = 0

    while True:
        guess = input(f"Guess a number between {low} and {high}: ")

        # Check if the input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        # Convert guess to an integer
        guess = int(guess)
        number_of_guesses += 1

        # Simulating the feedback
        if guess < low or guess > high:
            print(f"Your guess is out of range! It should be between {low} and {high}. Try again.")
        else:
            # Randomly decide if the guess is too high or too low if not correct
            if random.choice(["low", "high"]) == "low":
                if guess == high:
                    print(f"Congratulations! You guessed the number in {number_of_guesses} tries.")
                    break
                else:
                    low = guess + 1
                    print("Too low! Try again.")
            else:
                if guess == low:
                    print(f"Congratulations! You guessed the number in {number_of_guesses} tries.")
                    break
                else:
                    high = guess - 1
                    print("Too high! Try again.")

if __name__ == "__main__":
    play_number_guessing_game()
