#game_board=['_']* 9
choices=[]
for pos in range(0,9):
    choices.append(str(pos+1))
    
while True:

    print("\n")
    print(choices[0]+ '|'+ choices[1]+ '|'+ choices[2])
    print("----------")
    print(choices[3]+ '|'+ choices[4]+ '|'+ choices[5])
    print("----------") 
    print(choices[6]+ '|'+ choices[7]+ '|'+ choices[8])

    try:
        choice=int(input("> ").strip())
    except:
        print("Please enter only valid fields from board (0-8)")
        continue



    

    
    

    
