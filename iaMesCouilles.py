abc = "ABC"
ott = "123"

def isWinner(self, player):
        for i in range(3):
            col = 0
            row = 0
            diag = 0
            reverseDiag = 0
            for y in range(3):
                if self.getValue(self.grid, y, i) == player:
                    col += 1
                if self.getValue(self.grid, i, y) == player:
                    row += 1
                if self.getValue(self.grid, y, y) == player:
                    diag += 1
                if self.getValue(self.grid, y, 2-y) == player:
                    reverseDiag += 1
                
                if row == 3 or col == 3 or diag == 3 or reverseDiag == 3:
                    return True
        return False


'''----------------------------------------------------------------------------------------------------------------------------'''


def convertToCoords(x,y):
    return abc[x]+ott[y]

def impossibleBot(grid, player):
    while isWinner(grid, player) == False:
        for i in range(3):
            for j in range(3):
                if grid[i][j] != 0:
                    played += 1
        if player == 1:
            
        
            grid = grid
        else:
        
        
            grid = grid
