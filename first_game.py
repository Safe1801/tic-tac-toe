choices=[]

for pos in range(0,9):
    choices.append(str(pos+1))

is_Current_One=True # Default player will be X    

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


    # Users choice minus one, The reason behind it here is the "choices" -> variable that has the data type of list
    # Lists starts with index 0. And this list reflects the gameboards position. And choice variable that
    # stores the Users input has a range from 1 -9. As a consequence we therefore subtract the choice input variable with 1
    # to accommodate this list variable called "choices"
    
    if is_Current_One:
        choices[choice-1]='X' 
    else:
        choices[choice-1]='0'

    is_Current_One= not is_Current_One
    

    
    

    
