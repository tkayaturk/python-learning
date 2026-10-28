# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if sum(cards) > 21 and 11 in cards:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)
#
# my_cards = [11, 7, 5]
# result = calculate_score(my_cards)
# print(result)

# game_over = False
# score = 15
# while not game_over:
#     score += 3
#     print(score)
#     if score > 21:
#         print("Game Over")
#         game_over = True
#
# game_over = False
# score = 15
#
# while not game_over:
#     choice = input("Kart çek? y/n: ")
#     if choice == "y":
#         score += 3
#         if score > 21:
#             print("Busted")
#             game_over= True
#         print(score)
#     else:
#         game_over= True
#     # y ise score'a 3 ekle
#     # n ise oyunu bitir

#
# computer_score = 13
#
# while computer_score = 17:
#     computer_score += 2
#     print(computer_score)
#
# def play_game():
#     game_over = False
#     score = 15
#     computer_score = 13
#
#     while not game_over:
#         ask = input(" type 'y' or 'n'")
#         if ask == "y":
#             score += 3
#             print(score)
#             if score > 21:
#                 print("busted")
#                 game_over = True
#         else:
#             game_over = True
#     while computer_score < 17:
#         computer_score += 2
#         print(computer_score)
#
# play_game()



# def withdraw(balance, amount):
#    if amount > balance:
#        return "yetersiz bakiye"
#
#
#    return balance - amount - 10
#
#
#
# sonuc = withdraw(1000,200)
# print(sonuc)

#
# def buy_ticket(money,price):
#     if price > money:
#         return "not enough money"
#     return money - price
#
# sonuc = buy_ticket(100,65)
# print(sonuc)