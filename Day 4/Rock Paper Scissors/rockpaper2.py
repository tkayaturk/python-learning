import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_images = [rock, paper, scissors]
user_choice = int(input('Welcome to the rock, paper and scissors game! \n Please Select your move '
      'For  Rock Type "0" For Paper Type "1" and For Scissors Type "2" \n '))
if user_choice >=0 and user_choice <= 2:
   print(hand_images[user_choice])


   computer_choice = random.randint(0,2)

   print("Computer choice :")
   print(hand_images[computer_choice])

   if user_choice == computer_choice:
      print("It's a tie!")
   elif user_choice == 0 and computer_choice == 2:
       print("You win!")
   elif user_choice == 2 and computer_choice == 0:
       print("You lose!")
   elif user_choice > computer_choice:
       print("You Win")
   elif user_choice < computer_choice:
       print("You Lose")









else:
   print("Thats not a valid option")



