import art

print(art.logo)
user_list= {}

bidding = True
while bidding:
    key_of_the_user= input("What is your name? \n ")
    value_of_the_user= input("What is your bid? \n $")

    user_list[key_of_the_user] = int(value_of_the_user)

    ask_other_peoples= input("Are there any other bidders? "
                         "Type 'yes or 'no'\n ").lower()
    if ask_other_peoples == "no":
        bidding = False
    elif ask_other_peoples == "yes":
        print("\n" * 20)

highest_bid = 0
for bidder in user_list:
    if user_list[bidder] > highest_bid:
        highest_bid = user_list[bidder]
        winner = bidder
print(f"The winner is {winner} with highest bid {highest_bid}$.")





# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


