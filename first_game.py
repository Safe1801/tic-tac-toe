game_board=['_']* 9
while True:
    pos=input("Enter any position you want from(0-8): \n") #Take input from the user as a position from 0 to 8 and store it in the pos variable
    pos=int(pos)
    game_board[pos]='X'
    print(game_board[0]+ '|'+ game_board[1]+ '|'+ game_board[2])
    print(game_board[3]+ '|'+ game_board[4]+ '|'+ game_board[5])
    print(game_board[6]+ '|'+ game_board[7]+ '|'+ game_board[8])
