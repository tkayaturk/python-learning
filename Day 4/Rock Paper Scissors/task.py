import random
choose_what_you_do = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
if choose_what_you_do == "0" or choose_what_you_do == "1" or choose_what_you_do == "2":
    if choose_what_you_do == "0":
        print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')
    elif choose_what_you_do == "1":
        print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')
    elif choose_what_you_do == "2":
        print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
    print("Computer Choice")
    random_hand_moves = random.randint(0,2)
    if random_hand_moves == 0:
        print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')
    elif random_hand_moves == 1:
        print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')
    else:
        print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
    #first move rock
    if choose_what_you_do == "0":
       if random_hand_moves == 0:
           print("It's a draw!")
       elif  random_hand_moves == 1:
           print("You lose!")
       else:
           print("You win!")

    elif choose_what_you_do == "1":
       if random_hand_moves == 0:
           print("You win!")
       elif random_hand_moves == 1:
           print("It's a draw!")
       else:
           print("You lose!")
    elif choose_what_you_do == "2":
       if random_hand_moves == 0:
           print("You lose!")
       elif  random_hand_moves == 1:
           print("You win!")
       else:
           print("Its a draw!")

else:
    print("Bro really you want to play this game?")











