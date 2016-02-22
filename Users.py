import MineSweeper;
def inbounds(part0, part1, board):
    if((part0<0) or (part0>=len(board)) or (part1<0) or (part1>=len(board))):
        return False;
    else: return True;
    
def verify(array,board):
    if(inbounds(array[0],array[1], board) == False): #Check inbounds
        return False;
    elif(array[2]!="o" and array[2]!="?" and array[2]!="b"): #Check input o/?/b
        return False;
    elif(board[array[0]][array[1]] !="x" and board[array[0]][array[1]]!="B"):
        return False;
    else:
        return True;


        