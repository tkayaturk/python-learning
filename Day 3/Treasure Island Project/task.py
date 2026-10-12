print(r'''
*******************************************************************************
    __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('Youre in the danger on the burning ship! Which way you want to jump\n    Type "left" or "right": ').lower()

if direction == "left":
    decision =input('You jumped the water! but you see one shark coming toward you! do you gonna swim '
                    'to ship part or just wait in your poisition\n  '
                    'Type "swim" or "wait"  ')

    if decision == "wait":
       door = input('Your pirate mates helped you until the island and you have 3 colorful door in front of the building'
                    'Which door you will choose?\n  '
                    ' Type "red" or "blue" "yellow" ')
       if door == "yellow":
            print("You just took help from clever banana monkeys! Youre WIN!")
       elif door == "red":
           print("You just entered burning spot and you died!")
       elif door == "blue":
           print("You were eaten by beasts in the forest!")
       else:
           print("you suffered from youre decision skills and fucked by beasts")



    else:
        print("Shark took smell of your blood and ate YOU!")



else:
    print("You just jumped the shark mouth!!")




