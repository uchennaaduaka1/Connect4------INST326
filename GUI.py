class GUI:
    """This class represents the pure design of our 
    Connect4Game. Below lists the variables we have 
    created for cell size, colors and game status"""
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
