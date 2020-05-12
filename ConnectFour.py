import os
import sys
class Board:
    """"This class will create the game board. It initializes a list called board with 37 empty spaces representing an empty game board.
    
        Args:
            None
            
        Returns:
            Returns a game board as well an updated screen with player moves. A refreshed board if the players choose to restart the game
            
        Side Effects:
            This class carries no side effects."""
    def __init__(self):
        """This function initializes the game board as a list with 37 empty spaces.
        
            Args:
                None
                
            Returns:
                Does not return anything
                
            Side Effects:
                Does not carry any side effects."""
        self.board = [" "]*26
        
    def displayBoard(self):
        """This function prints out the game board.

            Args:
                No arguments
                
            Returns:
                Does not return anything.
                
            Side Effects:
                Prints out the board corresponding with spaces 1-25 of the board list."""
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
        """This function updates the space chosen by the player
        
            Args:
                spaceNum = the number the player chooses to put its piece in.
                player = the player who chooses the space ('R' or 'Y')
            
            Returns:
                Does not return anything.
            
            Side Effects:
                Updates the selected space with given space number and the player.
        
            """
        if self.board[spaceNum] == " ":
            self.board[spaceNum] = player
        
    
    def isHorizontalWin(self,player):
        """This function checks for the horizontal win and returns true if the space and the space to its right is four in a row.
        
            Args:
                player = the Red or Yellow player which will check if the space is equal to 'R' or 'Y'
                
            Returns:
                Returns true if the first four space in any of the five rows has the same player
                Returns true if the second through fifth space in any of the five rows has the same player
                Returns false if otherwise
            
            Side Effects:
                Carries no side effects."""
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
        """This function checks for the vertical win and returns true if the space and the space above is four in a row.
        
            Args:
                player = the Red or Yellow player which will check if the space is equal to 'R' or 'Y'
                
            Returns:
                Returns true if the first four spaces in any of the five columnss has the same player
                Returns true if the second through fifth spaces in any of the five columns has the same player
                Returns false if otherwise
            
            Side Effects:
                Carries no side effects."""
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
        """This function checks for the diagonal win and returns true if four spaces that are offset to its left or right by one is the same space
        
            Args:
                player = the Red or Yellow player which will check if the space is equal to 'R' or 'Y'
                
            Returns:
                Returns true if the a space and its pieces offset one down/one left or one up/one right has the same player
                Returns false if otherwise
            
            Side Effects:
                Carries no side effects."""
        if(self.board[6] == player and self.board[12] == player and self.board[18] == player and self.board[24] == player):
            return True
        elif(self.board[2] == player and self.board[8] == player and self.board[14] == player and self.board[20] == player):
            return True
        elif(self.board[1] == player and self.board[7] == player and self.board[13] == player and self.board[19] == player):
            return True
        elif(self.board[7] == player and self.board[13] == player and self.board[19] == player and self.board[25] == player):
            return True
    
    def isWinner(self,player):
        """This function determines if a player has one given whether it is a horizontal, diagonal, or vertical win
        
            Args:
                player = the Red or Yellow player which will check if the space is equal to 'R' or 'Y'
                
            Returns:
                Returns true if at least it is a horizontal, vertical, or diagonal win
                Returns false otherwise
            
            Side Effects:
                This function carries no side effects."""
        if (self.isHorizontalWin(player)):
            return True
        elif (self.isVerticalWin(player)):
            return True
        elif (self.isDiagonalWin(player)):
            return True
        else:
            return False
    
    def isTieGame(self):
        """This function determines if the game is a tie based on if there are no free spaces.
        
            Args:
                No arguments
            
            Returns:
                Returns true if free spaces is equal to 25
                Returns false otherwise
                
            Side Effects:
                This function carries no side effects."""
        free_spaces = 0
        for space in self.board:
            if space != " ":
                free_spaces += 1
        if free_spaces == 25:
            return True
        else:
            return False
                
    
    def resetGame(self):
        """This function resets the board if the player chooses to restart the game
        
            Args:
                No arguments
            
            Returns:
                Does not return anything
            
            Side Effects:
                Re-initializes the board attribute to a list of 26 empty spaces."""
        self.board = [" "]*26
    

#Creating an instance of the Board class to use in the PlayGame class        
board = Board()

def print_header():
    """A helper function to print out a message at the start

        Args:
            No arguments
        
        Returns:
            Does not return anything
        
        Side Effects:
            Prints a message."""
    print("Welcome to Connect Four\n")

def refreshScreen():
    """This function refreshes the screen after each turn to display the updates

        Args:
            None
            
        Returns:
            Does not return anything
        
        Side Effects:
            Clears the terminal with the os module
            Prints the message from the print_header() function
            displays the board from the board class."""
    
    os.system("clear")
    print_header()
    board.displayBoard()

class PlayGame:
    """This class executes the Board class as well as allows for input to run the entire game
    
        Args:
            isGameOn: Determines if the gameIsOn, defaults value is True
            
        Returns:
            This class does not return anything
            
        Side Effects:
            Takes in input from the terminal and/or command line
            Updates board with player moves
            Displays the winner of the game
            Asks users if they want to play again:
                        -If yes, will call the resetGame function
                        -If no, will exit system with .exit() from the sys module."""
    def __init__(self,isGameOn=True):
        """Initializes the isGameOn attribute to isGameOn

            Args:
                None
            
            Returns:
                None
                
            Side Effects:
                Does not carry any side effects."""
    
        self.isGameOn = isGameOn
        
    def startGame(self):
        """This is the main game loop that executes the game and class/method calls
        
            Args:
                None
                
            Return:
                Does not return anything
                
            Side Effects:
                Takes in input from the terminal and/or command line
            Updates board with player moves
            Displays the winner of the game
            Asks users if they want to play again:
                        -If yes, will call the resetGame function
                        -If no, will exit system with .exit() from the sys module."""
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
    """This statement executes the PlayGame call as the entire game when the file is called upon innthe terminal/command line
    
    Args:
        None
    
    Returns:
        None
    
    Side Effects:
        Executes PlayGame class."""
    game = PlayGame()
    game.startGame()
