#TiC TC TOE 
# Author- Shivam


board = [" " for i in range (0,9)]

def print_board():
    row1= "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2= "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3= "|{}|{}|{}|".format(board[6], board[7], board[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == "X":
        number=1
    elif icon== "O":
        number=2

    print("Your turn player {}".format (number))
    choice= int(input("Enter an input from 1 to 9: "))
    if board[choice-1]== " ":
        board[choice-1]= icon
    else:
        print()
        print("The space is taken, please select another number---")
        choice= int(input("Enter an input from 1 to 9: "))
        if board[choice-1]== " ":
         board[choice-1]= icon
    
def is_victory(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon) or \
      (board[3]==icon and board[4]==icon and board[5]==icon) or \
      (board[6]==icon and board[7]==icon and board[8]==icon) or \
      (board[0]==icon and board[3]==icon and board[6]==icon) or \
      (board[1]==icon and board[4]==icon and board[7]==icon) or \
      (board[2]==icon and board[5]==icon and board[8]==icon) or \
      (board[0]==icon and board[4]==icon and board[8]==icon) or \
      (board[2]==icon and board[4]==icon and board[6]==icon):
        return True
    else:
        return False
    
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
    
    

while True:
 board = [' '] * 10
 gameisplaying=True
 while gameisplaying:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins")
        gameisplaying=False
        break
        
    player_move("O")    
    if is_victory("O"):
        print_board()
        print ("O WINS")
        gameisplaying=False
        break
 if not playAgain():
    gameisplaying=True
    break
    
