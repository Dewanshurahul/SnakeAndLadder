import random

print("----Let's Gooo----")
# The Player will Start from position 0
position = 0
playerName = input("Player Please Enter Your Name: ")
# Until the Player Wins the Game it will be Continued
while position < 100:
    # In case the player position moves below 0
    # then the player restarts from 0
    if position < 0:
        position = 0
    # A random Number is Generated and according to this the Player will move Forward or Back Ward
    die_value = (((random.random() * 100) // 10) % 6) + 1
    #Random Number is generated to check whether Player will Play or not.
    play_Condition = ((random.random() * 100) // 10) % 3
    print(play_Condition)
    if play_Condition == 0:  # Condition is True for NO Play (The Player will be remain at the Same Point)
        pass
    elif play_Condition == 1:  # Condition is True for Ladder
        position += die_value
    elif play_Condition == 2:  #Condition is True for Snake
        position -= die_value