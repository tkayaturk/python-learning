def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


game_over = False
score = 15
computer_score = 13

while not game_over:
    ask = input("type 'y' or 'n': ")
    if ask == "y":
        score += 3
        print(score)
        if score > 21:
            print("busted")
            game_over = True
    else:
        game_over = True

while computer_score < 17:
    computer_score += 2
    print(computer_score)
