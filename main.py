current_player = "x"
winner = None
game_still_going = True

board = ["_","_","_",
         "_","_","_",
         "_","_","_",]






def display_board():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])



def play_game():

    display_board()
    while game_still_going:
        handle_turn(current_player)
        
        check_if_game_is_over()

        flip_player()
    if winner == "x" or winner == "o":
        print("Player" ,winner , "won.")
    elif winner == None:
        print("Tie.")



def handle_turn(current_player):
    # global current_player
    print("Player",current_player +"'s Turn")

    position = input("Choose position for 1-9 : ")
    valid = False
    while not valid:
    
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose position for 1-9 : ")
        position = int(position) - 1
        if board[position] == "_":
            valid = True
        else:
            print("Your con't go there. Try again.")
    board[position]= current_player
    display_board()



def check_if_game_is_over():
    check_for_winner()
    Check_if_tie()




def check_for_winner():

    global winner

    rows = check_rows()
    columns = check_columns()
    diagonals = check_diagonals()

    if rows :
        winner = rows
    elif columns:
        winner = columns
    elif diagonals:
        winner = diagonals
    else:
        winner = None
    return




def check_rows():
     
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        pass
    

def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        pass
    

def check_diagonals():
    global game_still_going

    diagnal_1 = board[0] == board[4] == board[8] != "_"
    diagnal_2 = board[2] == board[4] == board[6] != "_"

    
    if diagnal_1 or diagnal_2:
        game_still_going = False
    if diagnal_1:
        return board[0]
    elif diagnal_2:
        return board[2]
    else:
        pass
    
    

def Check_if_tie():
    global board
    global game_still_going
    if "_" not in board :
        game_still_going = False
    return



def flip_player():
    global current_player
    if current_player == "x":
        current_player= "o"
    elif current_player == "o":
        current_player = "x" 
    return
play_game()

# PROJECT COMPLETED.
