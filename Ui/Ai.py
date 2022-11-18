import copy
import random
import time

# VARIABLES

playerSymbols = ".XO"
abc = "abc"
ott = "123"

# FUNCTIONS

"""
Tests whether or not coordinates fit inside of a grid
"""
def testCoordinate(grid, x, y):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y]) 

"""
Gets value at the X and Y coordinates inside of a grid
"""
def getValue(grid, x, y):
    return 0 if not testCoordinate(grid, x, y) else grid[y][x]


"""
Sets value at the X and Y coordinates inside of a grid
"""
def setValue(grid, x, y, value):
    if not testCoordinate(grid, x, y):
        return False
    grid[y][x] = value
    return True

"""
Converts text coordinates (A2) to numbers (0, 1)
"""
def toCoordinates(coord):
    coordLower = coord.lower()
    if len(coordLower) == 2: 
        if coordLower[0] in abc and coordLower[1] in ott:
            return (abc.index(coordLower[0]), ott.index(coordLower[1]))
        elif coordLower[1] in abc and coordLower[0] in ott:
            return (abc.index(coordLower[1]), ott.index(coordLower[0]))
    
    return (-1, -1)

"""
Checks whether or not player won inside of the grid
"""
def isWinner(grid, player):
    for i in range(3):
        col = 0
        row = 0
        diag = 0
        reverseDiag = 0
        for y in range(3):
            if getValue(grid, y, i) == player:
                col += 1
            if getValue(grid, i, y) == player:
                row += 1
            if getValue(grid, y, y) == player:
                diag += 1
            if getValue(grid, y, 2-y) == player:
                reverseDiag += 1
            
            if row == 3 or col == 3 or diag == 3 or reverseDiag == 3:
                return True
    return False

"""
coordinates to str
"""
def coordinatesToStr(x, y):
    return abc[x]+ott[y]

"""
gets filled cases
"""
def filled(grid):
    filled = 0
    for row in grid:
        for e in row:
            filled += (e != 0)
    return filled

"""
Checks whether or not the grid is considered a draw
"""
def isDraw(grid):
    return filled(grid) == 9

def minmax(grid, player):
    move = (-1, -1)
    opponent = 1 if player == 2 else 2
    if filled(grid) == 0:
        return (0, (random.randint(0, 2), random.randint(0, 2)))
    elif isWinner(grid, player):
        return (1, move)
    elif isWinner(grid, opponent):
        return (-1, move)
    
    score = -2

    for x in range(3):
        for y in range(3):
            if getValue(grid, x, y) == 0:
                gridWithNewMove = copy.deepcopy(grid)
                setValue(gridWithNewMove, x, y, player)
                newScore, zzz = minmax(gridWithNewMove, opponent)
                newScore *= -1
                if newScore > score:
                    score = newScore
                    move = (x, y)
    
    if move == (-1,-1):
        return (0, move)
    
    return (score, move)