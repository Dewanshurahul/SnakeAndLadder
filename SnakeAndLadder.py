import random

print("----Let's Gooo----")
# The Players will Start from position 0
firstposition = 0
secondposition = 0
firstPlayerName = input("First Player Please Enter Your Name: ")
secondPlayerName = input("Second Player Please Enter Your Name: ")
# Used to Count the Number of times the Dice is thrown
dice_thow = 0
# Until the Player Wins the Game it will be Continued
while firstposition < 100 and secondposition < 100:
    print("------- First Player Chance -------")
    # A random Number is Generated and according to this the Player will move Forward or Backward
    die1_value = (((random.random() * 100) // 10) % 6) + 1
    # Count Every Dice Throw
    dice_thow += 1
    #Random Number is generated to check whether Player will Play or not.
    play_Condition = ((random.random() * 100) // 10) % 3
    if play_Condition == 0:  # Condition is True for NO Play (The Player will be remain at the Same Point)
        pass
    # Condition is True for Ladder and ensure exact Winning Condition
    elif play_Condition == 1 and firstposition + die1_value <= 100:
        firstposition += die1_value
    # Condition is True for Snake
    elif play_Condition == 2:
        firstposition -= die1_value
    # In case the player position moves below 0
    # then the player restarts from 0
    if firstposition < 0:
        firstposition = 0
    print("Dice Count: "+str(dice_thow))
    print("First Player's Position: "+str(firstposition))
    if firstposition == 100:
        print(firstPlayerName+" Wins")
        break

    print("------- Player 2 Chance -------")

    # A random Number is Generated and according to this the Player will move Forward or Backward
    die2_value = (((random.random() * 100) // 10) % 6) + 1
    # Count Every Dice Throw
    dice_thow += 1
    # Random Number is generated to check whether Player will Play or not.
    play_Condition = ((random.random() * 100) // 10) % 3
    if play_Condition == 0:  # Condition is True for NO Play (The Player will be remain at the Same Point)
        pass
    # Condition is True for Ladder and ensure exact Winning Condition
    elif play_Condition == 1 and secondposition + die2_value <= 100:
        secondposition += die2_value
    # Condition is True for Snake
    elif play_Condition == 2:
        secondposition -= die2_value
    # In case the player position moves below 0
    # then the player restarts from 0
    if secondposition < 0:
        secondposition = 0
    print("Dice Count: " + str(dice_thow))
    print("Second Player's Position: " + str(secondposition))
    if secondposition == 100:
        print(secondPlayerName+" Wins")
        break