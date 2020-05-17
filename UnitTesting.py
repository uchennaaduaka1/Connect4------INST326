import unittest
import Win_Logic_Connect4

class ConnectFourTestCases(unittest.TestCase):
    """"This class uses an instance of the unittest module for testing.
        It contains thorough output expectations as well as tests for
        the win logic of the Connect Four module.
    
        Args:
            None
            
        Returns:
            None
            
        Side Effects:
            -Will print out 'Ran x tests in 0.000s if the tests fails the assertEqual, assertTrue or assertFalse method
            -AssertionError: if the tests fails the assertEqual, assertTrue or assertFalse method."""
    
    #Testing and output expectation for the the helper methods
    """This method tests if the print header will print 
    "Welcome to Connect Four". As we expect it to do such,
    we have set the unit test to be true, so that we check
    the expected result against the what would happen if we called the method."""

    
    """refreshScreen() method:
    since this method can only by running the game, 
    we will provide thorough documentation of what to expect to output.
    This method will be called every time a player makes a move. The users can 
    expect the method to output a new game board with updated moods. 
    It also print the header as well each time a the board is updated with a move.
    Lastly, if a user chooses to restart the game then a new blank game board should be printed."""
    
    
    #Testing and output expectation for the Board class methods
    """displayBoard() method:
    this method should expect to print a 5x5 board that represents our Connect Four game board.
    This method utilizes string formatting from 25 empty spaces of an empty list."""
    
    """updateSpace() method;
    This method takes in the number that corresponds with a space on the board, it also takes 
    in the player that chooses a number. This method is expects to put either an 'R' or an 'Y'
    on the space that corresponds with the users' choice."""
    
    #For the win methods, we will create a list of length 26 to represent the game board for each test. 
    #We will fill the board list pieces that will be passed through with the red and yellow pieces.
    #Denoted by either 'R' or 'Y'.
    
    def test_isHorizontalWin_Pass(self):
        """Testing the isHorizontalWin method.
        We put four Red pieces in the last row of the board list. We expect
        the method to return True and use the assertEquals method
        to verify our expectations."""
        board1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','Y','Y','Y','R','R','R','R']
        result1 = True
        self.assertEqual(result1,Win_Logic_Connect4.isHorizontalWin(board1,'R'))
    
    def test_isHorizontalWin_Fail(self):
        """Testing the isHorizontalWin method.
        We put random Yellow and Red pieces in the board. We expect
        the method to return False and use the assertTrue method
        to verify our expectations."""
        board2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','Y','R','Y','Y','R','Y','R']
        result2 = False
        self.assertTrue(result2 == Win_Logic_Connect4.isHorizontalWin(board2,'R'))
        
    def test_isVericalWin_Passed(self):
        """Testing the isVerticalWin method.
        We put four Yellow pieces in the first column of the board list as well as . We expect
        the method to return True and use the assertEquals method
        to verify our expectations."""
        board3 = [' ',' ',' ',' ',' ',' ','Y',' ',' ',' ',' ','Y',' ',' ',' ',' ','Y',' ',' ',' ',' ','Y','R','R','R',' ']
        result3 = True
        self.assertEqual(result3,Win_Logic_Connect4.isVerticalWin(board3,'Y'))
        
    def test_isVericalWin_Fail(self):
        """Testing the isVerticalWin method.
        We put random Yellow and Red pieces in the board. We expect
        the method to return False and use the assertTrue method
        to verify our expectations."""
        board4 = [' ',' ',' ',' ',' ',' ','R',' ',' ',' ',' ','Y',' ',' ',' ',' ','R',' ',' ',' ',' ','Y','R','R','Y','Y']
        result4 = False
        self.assertTrue(result4 == Win_Logic_Connect4.isVerticalWin(board4,'Y'))
    
    def test_isDiagonalWin_Passed(self):
        """Testing the isDiagonalWin method.
        We put four Red pieces to show the method detects a ascending diagonal win. 
        We expect the method to return True and use the assertEquals method
        to verify our expectations."""
        board5 = [' ',' ',' ',' ',' ',' ',' ','R',' ',' ',' ',' ',' ','R',' ',' ',' ',' ',' ','R',' ',' ','Y','Y','Y','R']
        result5 = True
        self.assertEqual(result5,Win_Logic_Connect4.isDiagonalWin(board5,'R'))
    
    def test_isDiagonalWin_Fail(self):
        """Testing the isDiagonalWin method.
        We put random Yellow and Red pieces in the board. We expect
        the method to return False and use the assertTrue method
        to verify our expectations."""
        board6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','Y',' ',' ','R','Y','R','Y','Y','Y','R']
        result6 = False
        self.assertTrue(result6 == Win_Logic_Connect4.isDiagonalWin(board6,'Y'))  
        
    def test_isWinner_Passed(self):
        """Testing the isWinner method.
        We put four Red pieces in the board to simulate a diagonal win.
        We expect the method to return True since the win will be a diagional one.
        We use the assertEqual method to verify our expectations.""" 
        board7 = [' ',' ',' ',' ',' ',' ',' ','R',' ',' ',' ',' ',' ','R',' ',' ',' ',' ',' ','R',' ',' ','Y','Y','Y','R']
        result7 = True
        self.assertEqual(result7,Win_Logic_Connect4.isWinner(board7,'R'))
    
    def test_isWinner_Fail(self):
        """Testing the isWinner method.
        We put random pieces of Red and Yellow. 
        We expect the method to return False, since there is no win detected.
        We use the assertTrue method to verify our exepctations."""
        board8 = [' ',' ',' ',' ',' ',' ','R',' ',' ',' ',' ','Y',' ',' ',' ',' ','R',' ',' ',' ',' ','Y','R','R','Y','Y']
        result8 = False
        self.assertTrue(result8 == Win_Logic_Connect4.isWinner(board8,'R'))
    
    """isTieGame():
    This method cycles through the game board with the use of a for loop.
    It will check if a space is not empty or " ".It will also sum up the 
    amount of no free spaces. Users can expect that if the amount of no free spaces
    equals 25, then the method will return True to represent a tie game. And
    False otherwise to represent it is not a full game."""
    
    """resetGame():
    Once a winner or tie game is determined, the resetGame() method will be invoked.
    The users should expect this method to set the game board back to a clean slate. 
    This method will only be invoked if the user answers yes to restarting the game."""
    
    #Testing and output expectation for the Play Game class methods
    
    """The Play Game class creates an attribute called isGameOn.
    Users can always expect the Play Game class to execute the game
    since isGameOn is giving a default value of True. The game will not run
    if the users set the isGameOn attribute to False."""
    
    """startGame():
    This method executes the game so long as the isGameOn attribute is just 
    its default value of True. The game will not execute if the attribute is given
    the value of False.
    
    The startGame method always assumes that the Red player will go first. This method
    then takes in inputs. The users can expect to type a number between 1-25 to represent
    empty spaces on the game board. This method will call the updateSpace method to execute the
    users input.
    
    The method will also use the refreshScreen method to display a screen with whatever space the
    user chooses. After each turn the method will invoke the isHorizontalWin, isVericalWin,
    isDiagonalWin, isTieGame and isWinner method to check if a win is possible. 
    
    If a win or a tied game has happened the method will 
    then ask the user if they would would like to play again:
    
        If the user answers 'Yes' or 'yes' then users can expect 
        the method to call on the restartGame() method for a new game.
        
        If the user answers 'No' or 'no' then system will exit with 
        the use of the sys module and the game will be over."""
    
if __name__ == "__main__":
    """This statement allows the terminal and 
    command line to execute each test when called."""
    unittest.main()