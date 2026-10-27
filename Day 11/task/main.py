from art import logo
import random
want_to_play= input("Do u want to play AbQBlackjack? type 'y' for Yes  type 'n' for no : \n  ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def cards_information():
    print(f"Your current cards {your_cards}, Current Score {sum(your_cards)}")
    print(f"Computer final hand {opponent_cards} final score{sum(opponent_cards)} ")


def ask_user_for_draw_card():
    game_continue = True
    while game_continue:
        ask_user_choice = input("Type 'y' to get another card, type 'n' to pass:")
        if ask_user_choice == "y":
            for _ in range(1):
                your_cards.append(random.choice(cards))

                if sum(your_cards) > 21 and 11 in your_cards:
                    your_cards.remove(11)
                    your_cards.append(1)

                print(f"Your current cards {your_cards}, Current Score {sum(your_cards)}")

                if sum(your_cards) > 21:
                    game_continue = False
                    print("You Lose!")
                elif sum(your_cards) == 21:
                    game_continue = False
        else:
            computer_until_draw= True
            while computer_until_draw:
                if sum(opponent_cards) > 21 and 11 in opponent_cards:
                    opponent_cards.remove(11)
                    opponent_cards.append(1)

                elif sum(opponent_cards) <= 16:
                    opponent_cards.append(random.choice(cards))
                else:
                    computer_until_draw= False
            print(f"Your current cards {your_cards}, Current Score {sum(your_cards)}")
            print(f"Computer final hand {opponent_cards} final score{sum(opponent_cards)} ")

            if sum(opponent_cards) > 21:
                print("Dealer busted! You Win!")
            elif sum(opponent_cards) < sum(your_cards):
                print("You Win!")
            elif sum(opponent_cards) > sum(your_cards):
                print("You Lose!")
            else:
                print("It's tie!")

            game_continue = False


if want_to_play == "y":
    game_playing = True
    while  game_playing:
        print("\n" * 20)
        print(logo)
        your_cards=[]
        opponent_cards= []
        for _ in range(2):
           your_cards.append(random.choice(cards))
           if sum(your_cards) > 21 and 11 in your_cards:
               your_cards.remove(11)
               your_cards.append(1)

        for _ in range(2):
           opponent_cards.append(random.choice(cards))
           if sum(opponent_cards) > 21 and 11 in opponent_cards:
               opponent_cards.remove(11)
               opponent_cards.append(1)

        print(f"Your current cards {your_cards}, Current Score {sum(your_cards)}")
        print(f"Computer first card {opponent_cards[0]}")

        if sum(your_cards) == 21:
            if sum(opponent_cards) == sum(your_cards):
                cards_information()
                print("Its tie!")
            else:
                cards_information()
                print("You Win!")

        elif sum(opponent_cards) == 21:
            cards_information()
            print("You lose")
        else:
            ask_user_for_draw_card()

        play_again = input("Do you want to play again? Type 'y' or 'n': ")

        if play_again == "n":
            game_playing = False


