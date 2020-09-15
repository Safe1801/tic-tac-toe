choices=[]


is_Current_One = True # Default player is player X

for pos in range(0,9):
    choices.append(str(pos+1))
    
while True: 

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

    except:
        print("Please enter only valid fields from board (0-8)")
        continue

    if is_Current_One:
        choices[choice-1]='X'
    else:
        choices[choice-1]='O'

    is_Current_One = not is_Current_One

        
