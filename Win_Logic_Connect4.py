"""This module represents the win methods and win logic of our ConnectFour module
We modified the methods to be used for testing. 
No big changes were made so the methods should return the same results as if a game was running."""

def isHorizontalWin(board,player):
    """This is the same method from the Board class of the ConnectFour module. 
    It was modified for testing, we removed the self part and had the method
    take in board and player as parameters."""
    if(board[1] == player and board[2] == player and board[3] == player and board[4] == player):
        return True
    elif(board[2] == player and board[3] == player and board[4] == player and board[5] == player):
        return True
    elif(board[6] == player and board[7] == player and board[8] == player and board[9] == player):
        return True
    elif(board[7] == player and board[8] == player and board[9] == player and board[10] == player):
        return True
    elif(board[11] == player and board[12] == player and board[13] == player and board[14] == player):
        return True
    elif(board[12] == player and board[13] == player and board[14] == player and board[15] == player):
        return True
    elif(board[16] == player and board[17] == player and board[18] == player and board[19] == player):
        return True
    elif(board[17] == player and board[18] == player and board[19] == player and board[20] == player):
        return True
    elif(board[21] == player and board[22] == player and board[23] == player and board[24] == player):
        return True
    elif(board[22] == player and board[23] == player and board[24] == player and board[25] == player):
        return True
    else:
        return False
        
def isVerticalWin(board,player):
    """This is the same method from the Board class of the ConnectFour module. 
    It was modified for testing, we removed the self part and had the method
    take in board and player as parameters."""
    if(board[1] == player and board[6] == player and board[11] == player and board[16] == player):
        return True
    elif(board[6] == player and board[11] == player and board[16] == player and board[21] == player):
        return True
    elif(board[2] == player and board[7] == player and board[12] == player and board[17] == player):
        return True
    elif(board[7] == player and board[12] == player and board[17] == player and board[22] == player):
        return True
    elif(board[3] == player and board[8] == player and board[13] == player and board[18] == player):
        return True
    elif(board[8] == player and board[13] == player and board[18] == player and board[23] == player):
            return True
    elif(board[4] == player and board[9] == player and board[14] == player and board[19] == player):
        return True
    elif(board[9] == player and board[14] == player and board[19] == player and board[24] == player):
        return True
    elif(board[5] == player and board[10] == player and board[15] == player and board[20] == player):
        return True
    elif(board[10] == player and board[15] == player and board[20] == player and board[25] == player):
        return True
    else:
        return False
    
def isDiagonalWin(board,player):
    """This is the same method from the Board class of the ConnectFour module. 
    It was modified for testing, we removed the self part and had the method
    take in board and player as parameters."""
    if(board[6] == player and board[12] == player and board[18] == player and board[24] == player):
        return True
    elif(board[2] == player and board[8] == player and board[14] == player and board[20] == player):
        return True
    elif(board[1] == player and board[7] == player and board[13] == player and board[19] == player):
        return True
    elif(board[7] == player and board[13] == player and board[19] == player and board[25] == player):
        return True
    else:
        return False

def isWinner(board,player):
    """This is the same method from the Board class of the ConnectFour module. 
    It was modified for testing, we removed the self part and had the method
    take in board and player as parameters."""
    if (isHorizontalWin(board,player)):
        return True
    elif (isVerticalWin(board,player)):
        return True
    elif (isDiagonalWin(board,player)):
        return True
    else:
        return False
