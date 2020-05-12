import os
import sys
class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        
    def displayBoard(self):
        print(" {} | {} | {} ".format(self.board[1],self.board[2],self.board[3]))
        print("------------")
        print(" {} | {} | {} ".format(self.board[4],self.board[5],self.board[6]))
        print("------------")
        print(" {} | {} | {} ".format(self.board[7],self.board[8],self.board[9]))
        print("\n")
    
    def updateSpace(self,spaceNum,player):
        if self.board[spaceNum] == " ":
            self.board[spaceNum] = player
        
    
    def isHorizontalWin(self,player):
        if (self.board[1] == player and self.board[2] == player and self.board[3] == player):
            return True
        elif (self.board[4] == player and self.board[5] == player and self.board[6] == player):
            return True
        elif (self.board[7] == player and self.board[8] == player and self.board[9] == player):
            return True
        else:
            return False
    
    def isVerticalWin(self,player):
        if (self.board[1] == player and self.board[4] == player and self.board[7] == player):
            return True
        elif (self.board[2] == player and self.board[5] == player and self.board[8] == player):
            return True
        elif (self.board[3] == player and self.board[6] == player and self.board[9] == player):
            return True
        else:
            return False
    
    def isDiagonalWin(self,player):
        #Descending diagonal
        if(self.board[1] == player and self.board[5] == player and self.board[9] == player):
            return True
        #Ascending diagonal
        elif(self.board[7] == player and self.board[5] == player and self.board[3] == player):
            return True
        else:
            return False
    
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
        if free_spaces == 9:
            return True
        else:
            return False
                
    
    def resetGame(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def computerMove(self,player):
        
        #If the center space is open, it will first choose that
        if self.board[5] == " ":
            self.updateSpace(5,player)
        
        #Computer can win
        
        #Computer blocks
        
        #Choose random position
        for i in range(1,10):
            if self.board[i] == " ":
                self.updateSpace(i,player)
                break
            else:
                continue
        
board = Board()

def print_header():
    print("Welcome to Tic Tac Toe\n")

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
    
            x_choice = int(input("Player X, please choose a space (1-9): "))
            board.updateSpace(x_choice, "X")
            refreshScreen()
        
            if board.isWinner("X"):
                print("X has won!")
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
   
            
            board.computerMove("O")
            
            refreshScreen()
        
            if board.isWinner("O"):
                print("O has won!")
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
