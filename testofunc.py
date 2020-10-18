def printBoard(board):
    print('   |   |')
    print('' + board[7] +'   | ' + board[8] + '  |' + board[9])
    print('   |   |')
    print('----------')
    print('   |   |')
    print('  ' + board[4] + ' | ' + board[5] + '  | ' + board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print('  ' + board[1] + ' | ' + board[2] + '  | ' + board[3])
    print('   |   |')

board=['']*10
printBoard(board)

def isWinner(board,current_player):
    return ((board[7] == current_player and board[8] == current_player
             and board[9] == current_player)
            or (board[4] == current_player and board[5] == current_player
                and board[6] == current_player)
            or (board[1] == current_player and board[2] == current_player
                and board[3] == current_player)
            or (board[7] == current_player and board[4] == current_player
                and board[1] == current_player)
            or (board[8] == current_player and board[5] == current_player
                and board[2] == current_player)
            or (board[9] == current_player and board[6] == current_player
                and board[3] == current_player)
            or (board[7] == current_player and board[5] == current_player
                and board[3] == current_player)
            or (board[9] == current_player and board[5] == current_player
                and board[1] == current_player))

def makeMove(board, current_player, move):
    board[move]=current_player



def boardCopy(board):
    cloneBoard=[]
    for pos in board:
        cloneBoard.append(pos)
    return cloneBoard   

    

