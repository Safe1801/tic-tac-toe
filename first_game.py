choices=[]

for pos in range(0,9):
    choices.append(str(pos+1))

is_Current_One=True # Default player will be X    

won=False
print(choices)
while not won:
    # main loop, infinite amount of times.
    



    print("\n")
    print('|' + choices[0]+ '|'+ choices[1]+ '|'+ choices[2])
    print("------")
    print('|' + choices[3]+ '|'+ choices[4]+ '|'+ choices[5])
    print("------") 
    print('|'+ choices[6]+  '|'+ choices[7]+ '|'+ choices[8])

    if is_Current_One:
        print("Player X")

    else:
        print("Player O")

    try:
        choice=int(input("> ").strip())

    except ValueError:
        print("Please enter only valid fields from board (0-8)")
        continue


    # Users choice minus one, The reason behind it here is the "choices" -> variable that has the data type of list
    # Lists starts with index 0. And this list reflects the gameboards position. And choice variable that
    # stores the Users input has a range from 1 -9. As a consequence we therefore subtract the choice input variable with 1
    # to accommodate this list variable called "choices"
    
    if is_Current_One:
        try:
            choices[choice - 1]='X' 
        except IndexError:
            print("Please enter only valid fields from board(0-8)")
    else:
        try:
            choices[choice - 1]='O'
        except IndexError:
            print("Please enter only valid fields from board(0-8)")

    # Toggle between Player 1 and Player 2 with the help of Boolean
    is_Current_One = not is_Current_One

    for pos_x in range(0,3):
        pos_y = pos_x * 3

        if (choices[pos_y] == choices[(pos_y + 1)]) and (choices[pos_y] == choices[(pos_y + 2)]):
            won=True # main loop will break

        # column condition

        if (choices[pos_x] == choices[(pos_x + 3)]) and (choices[pos_x] == choices[(pos_x +6)]):
            won=True #main loop will break
    if ((choices[0]==choices[4]) and (choices[0] == choices[(8)]) or (choices[2] == choices[4]) and (choices[2]==choices[6])):
        won=True # main loop will break
    
    
print("Player " + str(int(is_Current_One + 1 )) + " won, Congratulations!")    
    
"""
is_Current_One=True

>>> int(is_Current_One)

1

>>> str(int(is_Current_One))

'1'

"""
