'''Practicing python commands'''


# def multiply(value):
#     return value * 3
#
# number = 4
# result = multiply(number)
#
# print(result)

# def calculate_score(cards):
#     return sum(cards)
#
# my_cards = [10, 7]
#
# user_score = calculate_score(my_cards)
#
# print(user_score)

# def calculate_score(cards):
#     return sum(cards)
#
#
# user_cards = [10, 5, 3]
#
# user_score = calculate_score(user_cards)
#
# print(user_score)

# def calculate_score(cards):
#     if sum(cards) >= 21 and len(cards) == 2:
#         return 0
#
#
#
#
# user_cards = [11, 10]
#
# user_score = calculate_score(user_cards)
#
# print(user_score)

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#
#     return  sum(cards)
#
# user_cards = [14, 7]
#
# user_score = calculate_score(user_cards)
#
# print(user_score)


# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#
#     if sum(cards) > 21 and 11 in cards:
#         cards.remove(11)
#         cards.append(1)
#
#     return sum(cards)
#
#
# user_cards = [10, 9, 5]
#
# user_score = calculate_score(user_cards)
#
# print(user_score)

# is_game_over = False
# score = 15
#
# while not is_game_over:
#     print(f"Score: {score}")
#
#     choice = input("Kart çekmek için y, durmak için n: ")
#
#     if choice == "y":
#         score += 3



#
#         if score > 21:
#             print("Bust!")
#             is_game_over = True
#
#     else:
#         is_game_over = True
#
# print("Game finished")





computer_score = 0

while computer_score !=0 and computer_score <17:
    computer_score += 2

print(computer_score)