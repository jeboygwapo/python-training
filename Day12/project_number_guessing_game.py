import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

def get_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5

def show_attempts():
    print(f"You have {attempts} remaining to guess the number.")

def go_guess(answer, attempts):
    guess = input(int("Make a guess: "))
    if guess == answer:
        print(f"You got it! The answer was {answer}")
        return 0
    elif guess > answer:
        print("Too low.\nGuess again.\n")
        return attempts-1
    else:
        print("Too high.\nGuess again.\n")
        return attempts-1


def main():
    welcome_message()
    attempts = get_difficulty()
    answer = random.randint(1,100)
    while attempts != 0:
        show_attempts(attempts)
        attempts = go_guess(answer, attempts)

    print("Too high.\nGuess again.\n")
    show_attempts()

    print("You've run out of guesses, you lose.")
    print(f"You got it! The answer was {answer}")

if __name__ == "__main__":
    main()
