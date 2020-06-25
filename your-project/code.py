#Tic Tac Toe Game
import random
print("\n")
print("Welcome to the Tic Tac Toe Game!\n")
print("First, There will be a random draw to decide who goes first: User or Computer")

player_selection=[1,2]
random_num=random.choice(player_selection)
if random_num == 1:
    print("User is Player 1. User goes first!\n")
else:
    print("User is Player 2. Computer goes first!\n")

board_list=["-","-","-",
       "-","-","-",
       "-","-","-"]

print(" | " + "1" + " | " + "2" + " | " + "3" + " | ")
print(" | " + "4" + " | " + "5" + " | " + "6" + " | ")
print(" | " + "7" + " | " + "8" + " | " + "9" + " | \n")
print("Above you can see the positions you may choose to select your move. Good Luck!\n")

def board():
    print(" | " + board_list[0] + " | " + board_list[1] + " | " + board_list[2] + " | ")
    print(" | " + board_list[3] + " | " + board_list[4] + " | " + board_list[5] + " | ")
    print(" | " + board_list[6] + " | " + board_list[7] + " | " + board_list[8] + " | ")

#selection={1:board_list[0],2:board_list[1],3:board_list[2],4:board_list[3],5:board_list[4],6:board_list[5],7:board_list[6],8:board_list[7],9:board_list[8]}

def game():
    #First thing is to show the board where the game will be played
    board()




game()
