player1 = 'Player'

def menu():
    global player1
    print("Welcome to Quasco's Tic-Tac-Toe(Single-player)")
    print("You('P' on the board) will play with computer('C' on the board)")
    player1= str(input("Enter Player name:"))



menu()


#Single player Tic Tac Toe game in python

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def ins_Letter(letter, pos):
    board[pos] = letter

def free_space(pos):
    return board[pos] == ' '

def dis_board(board):
    print("--------- ***** ---------")
    print("\n")
    print("Tic-Tac-Toe by Quasco")
    print("\n")
    print(board[1] + " | " + board[2] + " | " + board[3] + "     1 | 2 | 3")
    print(board[4] + " | " + board[5] + " | " + board[6] + "     4 | 5 | 6")
    print(board[7] + " | " + board[8] + " | " + board[9] + "     7 | 8 | 9")
    print("\n")
    
def Winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le)or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('Choose a position from 1-9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_space(move):
                    run = False
                    ins_Letter('P', move)
                else:
                    print("You can't go there. Go again.")
            else:
                print("Choose a position from 1-9:")
        except:
            print("Please type a number.")
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['C', 'P']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if Winner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = slc_random(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = slc_random(edgesOpen)
        
    return move

def slc_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    global player1
    print("Begin game!")
    dis_board(board)

    while not(board_full(board)):
        if not(Winner(board, 'C')):
            playerMove()
            dis_board(board)
        else:
            print("Sorry, Computer\'s won this time.")
            break

        if not(Winner(board, 'P')):
            move = compMove()
            if move == 0:
                print("Tie Game.")
            else:
                ins_Letter('C', move)
                print("Computer placed an \'Computer\' in position :", move)
                dis_board(board)
        else:
            print(player1, " won this time! Good Job!")
            break

        

board = [' ' for x in range(10)]
main()

while True:
    answer = input("Do you want to play again? (Y/N)")
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        menu()
        main()
    else:
        break




def t(board):
    while True:
            try:
                    x = int(input("Choose a position from 1-9: "))
                    if x in board:
                            return x
                    else:
                            print("\nSpace already taken. Try again")
            except ValueError:
                    print("\nThat's not a number. enter a space 1-9")
def GO(win,board):
    for x, o, b in win:
            if board[x] == board[o] == board[b]:
                    print("Player {0} wins!\n".format(board[x]))
                    print("Congratulations!\n")
                    return True
    if 9 == sum((pos == 'X' or pos == 'O') for pos in board):
            print("The game ends in a tie\n")
            return True
def tic_tac_toe():
    board = [None] + list(range(1, 10))
    win = [(1, 2, 3),(4, 5, 6),(7, 8, 9),(1, 4, 7),(2, 5, 8),(3, 6, 9),(1, 5, 9),(3, 5, 7),]
    for player in 'XO' * 9:
            drawboard(board)
            if GO(win,board):
                    break
            print("Player {0}".format(player))
            board[t(board)] = player
            print()
def main():
    while True:
            tic_tac_toe()
            #menu()
            if input("Play again (y/n)\n") == "y":
                menu()
            else:
                break
            
main()
