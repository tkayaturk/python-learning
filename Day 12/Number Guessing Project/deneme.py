from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_diffucilty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Its Too High bro")
        return turns - 1
    elif user_guess < actual_answer:
        print("Its Too low")
        return turns - 1
    else:
        print("That was Correct!")

def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_diffucilty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()