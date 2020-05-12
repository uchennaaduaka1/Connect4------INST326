import os
import sys
class Board:
    def __init__(self):
        self.board = [" "]*26
        
    def displayBoard(self):
        print(" {} | {} | {} | {} | {}".format(self.board[1],self.board[2],self.board[3],self.board[4],self.board[5]))
        print("-------------------")
        print(" {} | {} | {} | {} | {}".format(self.board[6],self.board[7],self.board[8],self.board[9],self.board[10]))
        print("-------------------")
        print(" {} | {} | {} | {} | {}".format(self.board[11],self.board[12],self.board[13],self.board[14],self.board[15]))
        print("-------------------")
        print(" {} | {} | {} | {} | {}".format(self.board[16],self.board[17],self.board[18],self.board[19],self.board[20]))
        print("-------------------")
        print(" {} | {} | {} | {} | {}".format(self.board[21],self.board[22],self.board[23],self.board[24],self.board[25]))
        print("\n")
    
    def updateSpace(self,spaceNum,player):
        if self.board[spaceNum] == " ":
            self.board[spaceNum] = player
        
    
    def isHorizontalWin(self,player):
        if(self.board[1] == player and self.board[2] == player and self.board[3] == player and self.board[4] == player):
            return True
        elif(self.board[2] == player and self.board[3] == player and self.board[4] == player and self.board[5] == player):
            return True
        elif(self.board[6] == player and self.board[7] == player and self.board[8] == player and self.board[9] == player):
            return True
        elif(self.board[7] == player and self.board[8] == player and self.board[9] == player and self.board[10] == player):
            return True
        elif(self.board[11] == player and self.board[12] == player and self.board[13] == player and self.board[14] == player):
            return True
        elif(self.board[12] == player and self.board[13] == player and self.board[14] == player and self.board[15] == player):
            return True
        elif(self.board[16] == player and self.board[17] == player and self.board[18] == player and self.board[19] == player):
            return True
        elif(self.board[17] == player and self.board[18] == player and self.board[19] == player and self.board[20] == player):
            return True
        elif(self.board[21] == player and self.board[22] == player and self.board[23] == player and self.board[24] == player):
            return True
        elif(self.board[22] == player and self.board[23] == player and self.board[24] == player and self.board[25] == player):
            return True
        else:
            return False
    
    def isVerticalWin(self,player):
        if(self.board[1] == player and self.board[6] == player and self.board[11] == player and self.board[16] == player):
            return True
        elif(self.board[6] == player and self.board[11] == player and self.board[16] == player and self.board[21] == player):
            return True
        elif(self.board[2] == player and self.board[7] == player and self.board[12] == player and self.board[17] == player):
            return True
        elif(self.board[7] == player and self.board[12] == player and self.board[17] == player and self.board[22] == player):
            return True
        elif(self.board[3] == player and self.board[8] == player and self.board[13] == player and self.board[18] == player):
            return True
        elif(self.board[8] == player and self.board[13] == player and self.board[18] == player and self.board[23] == player):
            return True
        elif(self.board[4] == player and self.board[9] == player and self.board[14] == player and self.board[19] == player):
            return True
        elif(self.board[9] == player and self.board[14] == player and self.board[19] == player and self.board[24] == player):
            return True
        elif(self.board[5] == player and self.board[10] == player and self.board[15] == player and self.board[20] == player):
            return True
        elif(self.board[10] == player and self.board[15] == player and self.board[20] == player and self.board[25] == player):
            return True
        else:
            return False
    
    def isDiagonalWin(self,player):
        if(self.board[6] == player and self.board[12] == player and self.board[18] == player and self.board[24] == player):
            return True
        elif(self.board[2] == player and self.board[8] == player and self.board[14] == player and self.board[20] == player):
            return True
        elif(self.board[1] == player and self.board[7] == player and self.board[13] == player and self.board[19] == player):
            return True
        elif(self.board[7] == player and self.board[13] == player and self.board[19] == player and self.board[25] == player):
            return True
    
    def isWinner(self,player):
        if (self.isHorizontalWin(player)):
            return True
        elif (self.isVerticalWin(player)):
            return True
        elif (self.isDiagonalWin(player)):
            return True
        else:
            return False
    
    def isTieGame(self):
        free_spaces = 0
        for space in self.board:
            if space != " ":
                free_spaces += 1
        if free_spaces == 25:
            return True
        else:
            return False
                
    
    def resetGame(self):
        self.board = [" "]*36
    
        
board = Board()

def print_header():
    print("Welcome to Connect Four\n")

def refreshScreen():
    os.system("clear")
    
    print_header()
    board.displayBoard()

class PlayGame:
    def __init__(self,isGameOn=True):
        self.isGameOn = isGameOn
        
    def startGame(self):
        while self.isGameOn:
            refreshScreen()
    
            red_player = int(input("Red player, please choose a space number: "))
            board.updateSpace(red_player, "R")
            refreshScreen()
        
            if board.isWinner("R"):
                print("Red has won!")
                restart = input("Would you like to play again (Yes/No): ")
                if restart == 'Yes':
                    board.resetGame()
                    continue
                else:
                    break
            
            if board.isTieGame():
                print("\nTie Game!")
                restart = input("Would you like to play again (Yes/No): ")
                if restart == 'Yes':
                    board.resetGame()
                    continue
                else:
                    break
    
            
            yellow_player = int(input("Yellow player, please choose a space number: "))
            board.updateSpace(yellow_player, "Y")
            refreshScreen()
            
            
            refreshScreen()
        
            if board.isWinner("Y"):
                print("Yellow player has won!")
                restart = input("Would you like to play again (Yes/No): ")
                if restart == 'Yes':
                    board.resetGame()
                    continue
                else:
                    break
        
            if board.isTieGame():
                print("\nTie Game!")
                restart = input("Would you like to play again (Yes/No): ")
                if restart == 'Yes':
                    board.resetGame()
                    continue
                else:
                    break
        

if __name__ == "__main__":
    game = PlayGame()
    game.startGame()