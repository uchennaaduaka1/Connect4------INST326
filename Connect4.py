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
    
    def dropDisc(self,column):
        if self.finishedGame:
            return False
        if column<0 and column >= self.size['c']:
            return False
        if len(self.grid[column]) >= self.size['r']:
            return False
        self.grid[column].append(self.players[self.player1])
        game_on = self.checkResults()
        if game_on == False:
            self.player1 = not self.player1
            return True
        else:
            self.finishedGame = game_on
            return True
        
class GUI:
    cellSize = 50
    gridColor = "White"
    player1Color = "Yellow"
    player2Color = "Red"
    backgroundColor = "Blue"
    gameIsOn = False
    
    def __init__(self, masterKey):
        self.masterKey = masterKey
        masterKey.title("Connect Four by Malonnie and Uchenna")
        
        self.canvas = Canvas(masterKey, width=300, height=60, background=self.backgroundColor)
        self.canvas.grid(row=1)
        
        self.statusVal = StringVar(self.masterKey,value="")
        self.statusLab = Label(self.masterKey,textvariable=self.statusVal,anchor=W)
        self.statusLab.grid(row=2)
        
        gameButton = Button(masterKey,text="Start Game Over",command=self.newGame)
        gameButton.grid(row=3)
        
        def newGame(self):
            self.p1 = "Yellow"
            self.p2 = "Red"
            
            columns = 7
            rows = 6
            
            self.gaming = ConnectFour(columns=columns,rows=rows)
            
            self.canvas.delete(ALL)
            
            self.canvas.config(width=(self.cellSize)*self.game.size['c'],
                              height=(self.cellSize)*self.game.size['r'])
            self.masterKey.update()
            
            self.drawGrid()
            self.makeMoves()
            
            self.changePlayer()
            self.gameIsOn = True
            
        def makeMoves(self):
            for c in range(self.game.size['c']):
                for r in range(self.game.size['r']):
                    if r>= len(self.game.grid[c]):
                        continue
                    x_0 = c*self.cellSize
                    y_0 = r*self.cellSize
                    x_1 = (c+1)*self.cellSize
                    y_1 = (r+1)*self.cellSize
                    
                    if self.game.grid[c][r] == self.game.players[True]:
                        fill = self.player1Color
                    else:
                        fill = self.player2Color
                    
                    self.canvas.create_ovals(x_0+2,self.canvas.winfo_height() - (y_0+2),
                                             x_1 -2,self.canvas.winfoheight() - (y_1-2),
                                            fill=fill, outline=self.gridColor)
        
        def drawGrid(self):
            fill=self.gridColor
            for r in range(self.game.size['r']):
                for c in range(self.game.size['c']):
                    x_2 = c*self.cellSize
                    y_2 = r*self.cellSize
                    x_3 = (c+1)*self.cellSize
                    y_3 = (r+1)*self.cellSize
                    self.canvas.create_ovals(x_2+2,
                                             self.canvas.winfo_height() - (y_2+2),
                                             x_3-2,self.canvas.winfo_height() - (y_3-2),
                                             fill=fill,outline=self.gridColor)
            x_0 = 0
            x_1 = self.canvas.winfo_width()
            for r in range(1, self.game.size['r']):
                y= r*self.cellSize
                self.canvas.create_line(x_0,y,x_1,y,fill=self.gridColor)
            y_0 = 0
            y_1 = self.canvas.winfo_height()
            for c in range(1,self.game.size['c']):
                x=c*self.cellSize
                self.canvas.create_line(x,y_0,x,y_1,fill=self.gridColor)
        
        def clickOnCanvas(self,click):
            if not self.gameIsOn:
                return
            if self.game.finished:
                return
            
            c = click.x // self.cellSize
            
            if(0 <= c < self.game.size['c']):
                self.drop(c)
                self.makeMoves()
                self.changePlayer()
            
            if self.game.finished:
                if self.game.finished == "Draw":
                    txt = "DRAW!"
                else:
                    if self.game.player1:
                        winner = self.p1
                    else:
                        winner = self.player2
                txt = winner + "won!"
                
                self.statusVal(txt)
            
        def drop(self,column):
            return self.game.drop(column)
        
        def changePlayer(self):
            p = self.p1 if self.game.player1 else self.p2
            self.statusVal.set('Current player: ' + p)
            
window = Tk()
app = GUI(window)
window.mainloop()