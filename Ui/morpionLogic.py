def testCoordinate(grid, x, y):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y]) 

def createGrid(): # [y][x]
    return [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

class game:
    def getValue(self, x, y):
        return 0 if not testCoordinate(self.grid, x, y) else self.grid[y][x]

    def setValue(self, x, y, value):
        if not testCoordinate(self.grid, x, y):
            return False
        self.grid[y][x] = value
        return True
    
    def isWinner(self, player):
        for i in range(3):
            col = 0
            row = 0
            diag = 0
            reverseDiag = 0
            for y in range(3):
                if self.getValue(y, i) == player:
                    col += 1
                if self.getValue(i, y) == player:
                    row += 1
                if self.getValue(y, y) == player:
                    diag += 1
                if self.getValue(y, 2-y) == player:
                    reverseDiag += 1
                
                if row == 3 or col == 3 or diag == 3 or reverseDiag == 3:
                    return True
        return False

    def isDraw(self):
        filled = 0
        for row in self.grid:
            for e in row:
                filled += (e != 0)
        return filled == 9

    def __init__(self):
        self.grid = createGrid()
