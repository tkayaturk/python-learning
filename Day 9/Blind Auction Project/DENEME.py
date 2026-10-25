# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winners = []
#     for bidder in bidding_record:
#         bidding_amount = bidding_record[bidder]
#         if bidding_amount > highest_bid:
#             highest_bid = bidding_amount
#
#     for bidder in bidding_record:
#         if bidding_record[bidder] == highest_bid:
#             winners.append(bidder)
#
#     for bidder in bidding_record:
#         print(f"{bidder} bid {bidding_record[bidder]}$")
#     if len(winners) >1:
#          print("There is a tie")
#     else:
#         print(f"the winner is {winners[0]} with {highest_bid}$")
#
#
# binds = {}
# game_stop = True
# while game_stop:
#     name = input("What is your name?:  \n ")
#     value = int(input("Whats your bid :  \n $ "))
#     binds[name] = value
#
#     continue_bind = input("Would you like to continue? type 'yes' or 'no':  \n ")
#     if continue_bind == "yes":
#         print("\n"* 20)
#     elif continue_bind == "no":
#         game_stop = False
#         find_highest_bidder(binds)
#



def find_highest_bidder(bidding_record):
    winners = []
    highest_bid = max(bidding_record.values())

    for bidder in bidding_record:
        if bidding_record[bidder] == highest_bid:
            winners.append(bidder)

    for bidder in bidding_record:
        print(f"{bidder} bid {bidding_record[bidder]}$")
    if len(winners) >1:
         print("There is a tie")
    else:
        print(f"the winner is {winners[0]} with {highest_bid}$")


binds = {}
game_stop = True
while game_stop:
    name = input("What is your name?:  \n ")
    value = int(input("Whats your bid :  \n $ "))
    binds[name] = value

    continue_bind = input("Would you like to continue? type 'yes' or 'no':  \n ")
    if continue_bind == "yes":
        print("\n"* 20)
    elif continue_bind == "no":
        game_stop = False
        find_highest_bidder(binds)

