# Reeborg's World - Maze Challenge
# The robot follows the right-hand wall until it reaches the goal.
# Functions like move(), turn_left(), and at_goal() are provided by Reeborg's World.


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()