# number_guessing.py
# Practice: variables, loops, conditionals, functions and random.
#
# python number_guessing.py         -> the computer plays against itself
# python number_guessing.py --play  -> you guess the number

import random
import sys


def check_guess(guess, secret):
    """Return 'low', 'high' or 'correct'."""
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"


def computer_plays(secret, low=1, high=100):
    """Guess the number using binary search: always pick the middle."""
    attempts = 0
    while True:
        attempts += 1
        guess = (low + high) // 2
        result = check_guess(guess, secret)
        print(f"Computer guesses {guess}: {result}")
        if result == "correct":
            return attempts
        if result == "low":
            low = guess + 1
        else:
            high = guess - 1


def human_plays(secret):
    attempts = 0
    while True:
        text = input("Your guess (1-100): ")
        try:
            guess = int(text)
        except ValueError:
            print("Please enter a whole number")
            continue
        attempts += 1
        result = check_guess(guess, secret)
        if result == "correct":
            return attempts
        print("Too", result)


def main():
    secret = random.randint(1, 100)
    if "--play" in sys.argv:
        attempts = human_plays(secret)
    else:
        attempts = computer_plays(secret)
    print(f"Found {secret} in {attempts} attempts")


if __name__ == "__main__":
    main()

# Try it:
# 1. Limit the player to 7 attempts.
# 2. Keep track of the best score across several rounds.
