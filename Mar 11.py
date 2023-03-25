import random

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

def main():

    global board
    print_board()
    for i in range(9):
        board[i]= " "
      

    while (True):
        player_turn()
        computer_turn()
        print_board()
        if check_winner("X"):
            print("Player Win!")
            break
        elif check_winner("O"):
            print("Computer Win!")
            break


def player_turn():
    while(True):
        x = int(input("Enter the location:"))
        if (x < 9) and (x >=0):
            x=int(x)
            if board[x]==" ":
                break
    
    board[x]= "X"



def computer_turn():
    while(True):
        x = random.choice(range(9))
        if board[x]==" ":
            break

    board[x]= "O"

def check_winner(mark):
    target= mark
    if (board[0] == target) and (board[1] == target) and (board[2] == target):
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

