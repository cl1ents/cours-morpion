# FUNCTIONS

from os import system, name as osname
"""
Clears console
"""
def clear():
    system('cls' if osname=='nt' else 'clear')

"""
Creates a 3 by 3 grid filled with 0s
"""
def createGrid(): # [y][x]
    return [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

"""
Prints the grid in a user-friendly way
e.g:
    A B C
    _ _ _
1 | X O O
2 | O X X
3 | X O -
"""
def printGrid(grid):
    print("    A B C")
    print("    _ _ _")
    for i in range(len(grid)):
        print("123"[i], end=" | ")
        row = grid[i]
        for e in row:
            print(".XO"[e], end = " ")
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
    coordLower = coord.lower()
    if len(coordLower) == 2: 
        if coordLower[0] in "abc" and coordLower[1] in "123":
            return ("abc".index(coordLower[0]), "123".index(coordLower[1]))
        elif coordLower[1] in "abc" and coordLower[0] in "123":
            return ("abc".index(coordLower[1]), "123".index(coordLower[0]))
    
    return (-1, -1)

"""
Custom input to intercept whatever the player types.
(Handles exit)
"""
def customInput(txt):
    while True:
        enteredInput = input(txt)
        if enteredInput.lower() == "exit":
            if input("Are you sure? (yes/no) > ").lower() == "yes":
                exit()
        else:
            return enteredInput

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

def round(grid, player):
    coordinates = (-1, -1)
    while coordinates == (-1, -1):
        clear()
        printGrid(grid)
        print("\nITS PLAYER "+str(player)+"'s TURN! ("+".XO"[player]+")")
        playerInput = customInput("Enter coordinates (e.g: A2) > ")
        coordinates = toCoordinates(playerInput)

        if getValue(grid, coordinates[0], coordinates[1]) != 0:
            coordinates = (-1, -1)
    
    setValue(grid, coordinates[0], coordinates[1], player)
    
clear()
print("""----
Welcome to MORPION!!
----
Le but du jeu est simple:
Il suffit d'aligner, avant son adversaire, 3 symboles identiques horizontalement, verticalement ou en diagonale sur une grille de 3x3.
Le joueur ayant aligné 3 symboles gagne la partie.
Le joueur 1 a le symbole X et le joueur 2 a le symbole O
Pour jouer, le joueur indique les coordonnées de la case dans laquelle il veut jouer, par exemple "C2"

""")
input('(Appuyez sur entrer pour continuer.)')

grid = createGrid()
turn = 2
playing = True

while playing:
    turn = (turn%2)+1
    round(grid, turn)
    
    if isWinner(grid, turn):
        clear()
        printGrid(grid)
        print("\nPLAYER "+str(turn)+" WINS!\n")
        input('(Appuyez sur entrer pour continuer.)')
        playing = False