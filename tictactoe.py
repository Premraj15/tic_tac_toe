import random
def display_board(board):
    print("     |     |    ")
    print("  "+board[7]+"  |  "+board[8]+"  |  "+board[9])
    print("     |     |    ")
    print("------------------")
    print("     |     |    ")
    print("  "+board[4]+"  |  "+board[5]+"  |  "+board[6])
    print("     |     |    ")
    print("------------------")
    print("     |     |    ")
    print("  "+board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("     |     |    ")

def user_input(board):
    position=0
    
    accept_value=range(1,10)

    while position not in accept_value or not space_check(board,position):
        position=int(input("Enter the position(1-9) : "))
        
    return position


def player_choose():
    marker=''
    while marker!='X'and marker!='O':
        marker=input('Player1, Enter choice(X-O) :  ')
    
    if(marker=='X'):
        return('X','O')
    else:
        return('O','X')

def place_choice(board,choice,mark):
    board[choice]=mark

def choose_first():
    flip=random.randint(0,1)

    if flip==0:
        return 'player1'
    else:
        return 'player2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def replay():
    choice=''
    while choice not in ['Y','N']:
        choice =input("Play again? Enter Y or N :")
    if choice=='Y':
        return True
    else:
        return False


def win_check(board,mark):
    print("\n"*100)
    return( (board[1]==board[2]==board[3]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[7]==board[8]==board[9]==mark) or
    (board[1]==board[4]==board[7]==mark) or
    (board[2]==board[5]==board[8]==mark) or
    (board[3]==board[6]==board[9]==mark) or
    (board[1]==board[5]==board[9]==mark) or
    (board[7]==board[5]==board[3]==mark))

# main function


while True:

    board=[' ']*10
    
    player1,player2=player_choose()

    turn=choose_first()

    print(turn+" will play first")

    game_on=True
    while game_on:
        if turn=='player1':
            display_board(board)

            position=user_input(board)
            place_choice(board,position,player1)


            if win_check(board,player1):
                display_board(board)
                print("player1 won the game")
                game_on=False

            if full_board_check(board):
                display_board(board)
                print("Game is tie")
                game_on=False
            
            turn='player2'
            
        else:
            display_board(board)

            position=user_input(board)
            place_choice(board,position,player2)


            if win_check(board,player2):
                display_board(board)
                print("player 2 won the game")
                game_on=False

            if full_board_check(board):
                display_board(board)
                print("Game is tie")
                game_on=False
            
            turn='player1'



    if not replay():
        break
    