import copy
import random
import time

# VARIABLES

playerSymbols = ".XO"
abc = "abc"
ott = "123"
"""
X _ X 
_ _ _
X _ X
"""
corners = [(0,0),(0,2),(2,0),(2,2)]

"""
_ X _
X _ X
_ X _
"""
sides = [(0,1),(1,0),(1,2),(2,1)]

"""
_ _ _
_ X _
_ _ _
"""
center = (1,1)

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

"""
def minmax(grid, player):
    move = (-1, -1)
    opponent = 1 if player == 2 else 2
    if filled(grid) == 0:
        return (0, (1,1))
    if isWinner(grid, player):
        return (1, move)
    elif isWinner(grid, opponent):
        return (-1, move)
    
    score = -2

    for x in range(3):
        for y in range(3):
            if getValue(grid, x, y) == 0:
                gridWithNewMove = copy.deepcopy(grid)
                setValue(gridWithNewMove, x, y, player)
                newScore = -minmax(gridWithNewMove, opponent)[0]
                if newScore > score:
                    score = newScore
                    move = (x, y)
    
    if move == (-1,-1):
        return (0, move)
    
    return (score, move)
"""

"""
First turns of IA
"""
def firstTurns(grid, player):
    opponent = 1 if player == 2 else 2
    if filled(grid) == 1 and grid[1][1] == 0:
        return center
    elif filled(grid) == 0 or filled(grid) == 1:
        return random.choice(corners)
    
    if filled(grid) == 3 and (getValue(grid, 0, 0) == getValue(grid, 2, 2) == opponent or getValue(grid, 2, 0) == getValue(grid, 0, 2) == opponent):
        return random.choice(sides)
    return (-1, -1)


"""
Checks whether or not the player can win
"""
def playerCanWin(grid, player):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                grid[i][j] = player
                if isWinner(grid, player):
                    grid[i][j] = 0
                    return (j, i)
                grid[i][j] = 0
    return (-1, -1)

"""
Checks whether or not the player can fork (lol)
"""
def playerCanFork(grid, player, winCondition):
    tempGrid = copy.deepcopy(grid)
    for i in range(3):
        for j in range(3):
            if tempGrid[i][j] == 0:
                tempGrid[i][j] = player
                winCounter = 0
                for k in range(3):
                    for l in range(3):
                        if tempGrid[k][l] == 0:
                            tempGrid[k][l] = player
                            if isWinner(tempGrid, player):
                                winCounter += 1
                            if winCounter >= winCondition:
                                    return (j, i)
                            tempGrid[k][l] = 0
                tempGrid[i][j] = 0
    return (-1, -1)

"""
Function that returns what the bot would play according to the current grid
"""
def ai(grid, turn):
    opponent = 1 if turn == 2 else 2
    
    # Process first turns
    result = firstTurns(grid, turn)
    if result != (-1, -1):
        print('firstTurn')
        return (result[0], result[1])

    # If the Ai can win
    result = playerCanWin(grid, turn)
    if result != (-1, -1):
        print('aiCanWin')
        return (result[0], result[1])

    # If the Player can win
    result = playerCanWin(grid, opponent)
    if result != (-1, -1):
        print('playerCanWin')
        return (result[0], result[1])
    
    # If the Player can fork
    result = playerCanFork(grid, opponent, 2)
    if result != (-1, -1):
        print('playerCanFork')
        return (result[0], result[1])

    # If the Ai can fork
    result = playerCanFork(grid, turn, 2)
    if result != (-1, -1):
        print('aiCanFork')  
        return (result[0], result[1])

    # If the Ai can line up symbols to win
    result = playerCanFork(grid, turn, 1)
    if result != (-1, -1):
        print('aiLineUp')  
        return (result[0], result[1])
    
    print('random')

    freeSpace = []
    for x in range(3):
        for y in range(3):
            if getValue(grid, x, y) == 0:
                freeSpace.append((x, y))

    return random.choice(freeSpace)