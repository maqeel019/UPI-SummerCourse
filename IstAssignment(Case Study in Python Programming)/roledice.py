import random

def roll_dice():
    """Roll two six-sided dice and return the sum of the spots"""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def play_game():
    """Play the game of craps"""
    print("Welcome to Craps!")
    print("Rolling the dice...")

    # Roll the dice for the first time
    point = None
    while True:
        sum_of_dice = roll_dice()
        print(f"You rolled a {sum_of_dice}")

        if sum_of_dice in [7, 11]:
            print("You win!")
            break
        elif sum_of_dice in [2, 3, 12]:
            print("You lose. Craps!")
            break
        else:
            point = sum_of_dice
            print(f"Your point is {point}")
            break

    # Roll the dice until you make your point or roll a 7
    while point is not None:
        sum_of_dice = roll_dice()
        print(f"You rolled a {sum_of_dice}")
        if sum_of_dice == 7:
            print("You lose. You rolled a 7 before making your point.")
            break
        elif sum_of_dice == point:
            print("You win! You made your point.")
            break

play_game()