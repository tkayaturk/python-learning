import random


print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100."
      " ")

secret_number = random.randint(1, 100)
print(secret_number)


def easy_or_hard_choice():
    ask = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    if ask == "hard":
        attemps = 5
    else:
        attemps = 10

    print(f"You have {attemps} attemps remaining to guess the number.")

    return attemps


attemps = easy_or_hard_choice()
game_over = False

while not game_over:
    user_guess = int(input("Make a guess : "))
    if user_guess != secret_number:
        attemps -= 1
        if attemps > 0:
            if user_guess > secret_number:
                print("Too high \n "
                      "Guess again.")
                print(f"you have {attemps} remain.")
            else:
                print("Too low \n "
                      "Guess Again.")
                print(f"you have {attemps} remain,")
        else:
            print("You lose")
            game_over = True
    else:
        print("You Got it!")
        game_over = True
