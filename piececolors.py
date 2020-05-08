class State:
    def __init__(self):
        self.player = 'yellow'
        self.gameSlots = [0]*8
        self.grid = [[None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None]]
        
    def resetBoard(self):
        self.gameSlots = [0]*8
        self.grid = [[None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None]]