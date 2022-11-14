# FUNCTIONS

"""
Creates a 3 by 3 grid filled with 0s
"""
def createGrid(): # [y][x]
    return [
        [1,0,0],
        [0,2,0],
        [0,0,2]
    ]

"""
Prints the grid in a user-friendly way
e.g:
    1 2 3
    _ _ _
A | X O O
B | O X X
C | X O -
"""
def printGrid(grid):
    print("    1 2 3")
    print("    _ _ _")
    for i in range(len(grid)):
        print("ABC"[i], end=" | ")
        row = grid[i]
        for e in row:
            print("X" if e == 1 else "O" if e == 2 else ".", end = " ")
        print("")

def testCoordinate(grid, x, y):
    return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y]) 

def getValue(grid, x, y):
    return 0 if not testCoordinate(grid, x, y) else grid[y][x]

def setValue(grid, x, y, value):
    if not testCoordinate(grid, x, y):
        return False
    grid[y][x] = value
    return True

def toCoordinates(coord):
    if len(coord) == 2:
        if coord[0] in "ABC" and coord[1] in "123":
            return ("ABC".index(coord[0]), "123".index(coord[1]))
        elif coord[1] in "ABC" and coord[0] in "123":
            return ("ABC".index(coord[1]), "123".index(coord[0]))
    
    return (-1, -1)

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


grid = createGrid()
printGrid(grid)
print(isWinner(grid, 1))
print(toCoordinates('A3'))