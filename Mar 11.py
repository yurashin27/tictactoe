import random
import time

board = [i for i in range(9)]

def draw_check():
    num_of_O=0
    num_of_X=0
    for i in range(9):
        if board[i]=="O":
            num_of_O=num_of_O+1
        elif board[i]=="X":
            num_of_X=num_of_O+1
    if (num_of_O==4) and (num_of_X==4):
        print("Draw!")
        return True
    else:
        return False


def print_board():
    global board
    print("|"+str(board[0])+"|"+str(board[1])+"|"+str(board[2])+"|")
    print("|"+str(board[3])+"|"+str(board[4])+"|"+str(board[5])+"|")
    print("|"+str(board[6])+"|"+str(board[7])+"|"+str(board[8])+"|")
    print(" ")

def main():

    global board
    print_board()
    for i in range(9):
        board[i]= " "

    while (True):
        genius_computer_turn()
        print_board()
        if check_game_end():
            break
        # player_turn()
        random_computer_turn("X")
        print_board()
        if check_game_end():
            break
        time.sleep(0.5)

def check_game_end():
    if check_winner("X"):
        print("X Win!")
        return True
    if check_winner("O"):
        print("O Win!")
        return True
    if draw_check():
        return True



def player_turn():
    while(True):
        x = int(input("Enter the location:"))
        if (x < 9) and (x >=0):
            x=int(x)
            if board[x]==" ":
                break
    
    board[x]= "X"

def check_empty_space_when_my_two(input_list, mark):
    sum=0
    for i in input_list:
        if board[i] == mark:
            sum += 1
    if sum == 2:
        for j in input_list:
            if board[j] ==" ":
                return j 
    return None

def check_opponent_two():
    row1= [0,1,2]    
    row2= [3,4,5] 
    row3= [6,7,8]   
    col1= [0,3,6]   
    col2= [1,4,7]  
    col3= [2,5,8]      
    dia1= [0,4,8]     
    dia2= [2,4,6]
    
    check_list =[row1,row2,row3,col1, col2, col3, dia1, dia2]
    for i_list in check_list:
        res= check_empty_space_when_my_two(i_list, "X")
        if res != None:
            return res
    return None
    


def check_my_two():
    row1= [0,1,2]    
    row2= [3,4,5] 
    row3= [6,7,8]   
    col1= [0,3,6]   
    col2= [1,4,7]  
    col3= [2,5,8]      
    dia1= [0,4,8]     
    dia2= [2,4,6]
    
    check_list =[row1,row2,row3,col1, col2, col3, dia1, dia2]
    for i_list in check_list:
        res= check_empty_space_when_my_two(i_list, "O")
        if res != None:
            return res
    return None


def random_computer_turn(mark):
    while(True):
        x = random.choice(range(9))
        if board[x]==" ":
            break

    board[x]= mark

def check_near_corner(position, first_near, second_near):
    if board[position] == "O":
        if board[first_near] == " ":
            return first_near
        elif board[second_near] ==" ":
            return second_near
    return None


def find_near_corner():
    target= check_near_corner(0,2,6)
    if target is not None:
        return target
    target=check_near_corner(2,0,8)
    if target is not None:
        return target
    target=check_near_corner(6,0,8)
    if target is not None:
        return target
    target=check_near_corner(8,6,2)
    if target is not None:
        return target


def genius_computer_turn():
    if check_corner() == True:
        if board[4]==" ":
            board[4] = "O"
        else:
            target= check_my_two()
            if target !=None:
                board[target]="O"
            else:
                target= check_opponent_two()
                if target !=None:
                    board[target]="O"
                else:
                    target = find_near_corner()
                    if target !=None:
                        board[target]="O"
                    else:
                        print("next step")
    
    else:
        x= random.choice([0, 2, 6, 8])
        board[x]= "O"



def check_corner():
    if  (board[0] == "O") or (board[0]== "X") or \
        (board[2] == "O") or (board[0]== "X") or \
        (board[6] == "O") or (board[0]== "X") or \
        (board[8] == "O") or (board[0]== "X"):
        return True
    else:
        return False
        

def check_winner(mark):
    target= mark
    if   (board[0] == target) and (board[1] == target) and (board[2] == target):
        return True
    elif (board[3] == target) and (board[4] == target) and (board[5] == target):
        return True
    elif (board[6] == target) and (board[7] == target) and (board[8] == target):
        return True
    elif (board[0] == target) and (board[3] == target) and (board[6] == target):
        return True
    elif (board[1] == target) and (board[4] == target) and (board[7] == target):
        return True
    elif (board[2] == target) and (board[5] == target) and (board[8] == target):
        return True
    elif (board[0] == target) and (board[4] == target) and (board[8] == target):
        return True
    elif (board[2] == target) and (board[4] == target) and (board[6] == target):
        return True
    
if __name__ == "__main__":
    main()

