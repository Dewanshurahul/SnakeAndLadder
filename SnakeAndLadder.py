import random

print("----Let's Gooo----")
# The Player will Start from position 0
position = 0
playerName = input("Player Please Enter Your Name: ")
# Used to Count the Number of times the Dice is thrown
dice_thow = 0
# Until the Player Wins the Game it will be Continued
while position < 100:
    # A random Number is Generated and according to this the Player will move Forward or Backward
    die_value = (((random.random() * 100) // 10) % 6) + 1
    # Count Every Dice Throw
    dice_thow += 1
    #Random Number is generated to check whether Player will Play or not.
    play_Condition = ((random.random() * 100) // 10) % 3
    if play_Condition == 0:  # Condition is True for NO Play (The Player will be remain at the Same Point)
        continue
    # Condition is True for Ladder and ensure exact Winning Condition
    elif play_Condition == 1 and position + die_value <= 100:
        position += die_value
    # Condition is True for Snake
    elif play_Condition == 2:
        position -= die_value
    # In case the player position moves below 0
    # then the player restarts from 0
    if position < 0:
        position = 0
    print("Dice Count: "+str(dice_thow))
    print("Position: "+str(position))