from tkinter import *
from tkinter import font

class ConnectFour:
    def __init__(self,columns=7,rows=6,player1='X',player='O'):
        self.size = {'c': columns, 'r': rows}
        self.grid = []
        self.player1 = True
        self.player2 = False
        self.players = {True: player1, False: player2}
        self.finishedGame = False
        self.grid = [[] for i in range(self.size['c'])]
        
    def checkResults(self):
        numOfDiscs = 0
        for i, column in enumerate(self.grid):
            numOfDiscs = len(self.grid[i])
            for j, row in enumerate(column):
                if i+4 <= self.size['c']:
                    horizontal = True
                else:
                    horizontal = False
                
                vertical = (j+4 <= len(self.grid[i]))
                
                if vertical:
                    if len(set(self.grid[i][j:j+4])) == 1:
                        return "Winner"
                
                if horizontal:
                    if len(self.grid[i]) > j and len(self.grid[i+1]) > j and len(self.grid[i+2]) > j and len(self.grid[i+3]) > j:
                        set_diagonal = set()
                        for k in range(4):
                            set_diagonal.add(self.grid[i+k][j])
                            
                            if len(set_diagonal) == 1:
                                return "Winner"
                    
                    if horizontal:
                        setDiagonal = set()
                        for k in range(4):
                            if len(self.grid[i+k]) > j+k:
                                setDiagonal.add(self.grid[i+k][j+k])
                            else:
                                setDiagonal.add("Not Occupied")
                            
                            if len(setDiagonal) == 1:
                                return "Winner"
                        
                        if horizontal and j-4+1 >=0:
                            setDiagonal = set()
                            for k in range(4):
                                if len(self.grid[i+k]) > j-k:
                                    setDiagonal.add(self.grid[i+k][j-k])
                                else:
                                    setDiagonal.add("Not Ocuppied")
                        
                            if len(setDiagonal) == 1:
                                return "Winner"
                    
                    if numOfDiscs == self.size['c']*self.size['r']:
                        return "There is a Draw"
                    return False
    
    