from random import randint
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
position = 0
player1_letter = ' '
player2_letter = ' '
marker = ' '
name = ''
# here we are assiging each player a letter to play with and displaying them
def display_board(*args):
    print('|',board[6],'|',board[7],'|',board[8],'|')
    print('----------')
    print('|',board[3],'|',board[4],'|',board[5],'|')
    print('----------')
    print('|',board[0],'|',board[1],'|',board[2],'|')   


# We are taking in the players letters and assging them
def player_input(position, turn):
    if turn:
        board[position-1]= 'O'
    else:
        board[position-1]= 'X'





def win_check(board,mark):
    if not mark:
        mark = "X"
    else:
        mark = "O"
    return ((board[7] == mark and board[8] == mark and board[8] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
    (board[6] == mark and board[3] == mark and board[0] == mark) or # down the middle
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
    (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
    (board[8] == mark and board[4] == mark and board[0] == mark)) # diagonal

def check_board():
    for i in board:
        if i != " ":
            continue
        else:
            return False
    return True


turn = randint(0,1)
if name == 'X':
    player2_letter = 'O'
else:
    player2_letter = 'X'
name = ""
while True:
    display_board(1,2,3,4,5,6,7,8,9)
    if not turn:
        name = "X"
    else:
        name = "O"
    player_letter = int(input("Please choose a position for player " + name + ": "))
    if board[player_letter-1] != " ":
        print("Choose another position")
        continue
    player_input(player_letter,turn)
    if win_check(board, turn):
        print(name, " wins")
        display_board()
        break
    elif check_board():
        print("Draw")
    if turn == False:
        turn = True
    else:
        turn = False
    display_board()






#Displaying the palying board

