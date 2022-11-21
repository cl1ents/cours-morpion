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

from copy import deepcopy
from os import system, name as osname
from random import choice, randint

"""
Checks if string can be converted to an int
"""
def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

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
    output = ''
    output += "    A B C\n    _ _ _\n"
    for i in range(len(grid)):
        output += ott[i]+" | "
        row = grid[i]
        for e in row:
            output += playerSymbols[e]+" "
        output += "\n"
    
    print(output)

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
Converts numbers (0, 1) to text coordinates (A2) 
"""
def convertToTextCoords(x, y):
    return abc[x]+ott[y]
    

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
First turns of IA
"""
def firstTurns(grid, player):
    opponent = 1 if player == 2 else 2
    roundNumber = filled(grid)

    if roundNumber == 1 and getValue(grid, 1, 1) == 0:
        return center
    elif roundNumber == 0 or roundNumber == 1:
        return choice(corners)
    elif roundNumber == 3 and (getValue(grid, 0, 0) == getValue(grid, 2, 2) == opponent or getValue(grid, 2, 0) == getValue(grid, 0, 2) == opponent):
        return choice(sides)
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
def playerCanFork(grid, player):
    winCounter = 0
    tempGrid = deepcopy(grid)
    for i in range(3):
        for j in range(3):
            if tempGrid[i][j] == 0:
                tempGrid[i][j] = player
                for k in range(3):
                    for l in range(3):
                        if tempGrid[k][l] == 0:
                            tempGrid[k][l] = player
                            if isWinner(tempGrid, player):
                                winCounter += 1
                            if winCounter >= 2:
                                return (j, i)
                            tempGrid[k][l] = 0
                tempGrid[i][j] = 0
    return (-1, -1)

"""
Function that returns what the bot would play according to the current grid
"""
def aiInput(grid, turn):
    opponent = 1 if turn == 2 else 2
    
    # Process first turns
    result = firstTurns(grid, turn)
    if result != (-1, -1):
        return convertToTextCoords(result[0], result[1])

    # If the Ai can win
    result = playerCanWin(grid, turn)
    if result != (-1, -1):
        return convertToTextCoords(result[0], result[1])

    # If the Player can win
    result = playerCanWin(grid, opponent)
    if result != (-1, -1):
        return convertToTextCoords(result[0], result[1])
    
    # If the Player can fork
    result = playerCanFork(grid, opponent)
    if result != (-1, -1):
        return convertToTextCoords(result[0], result[1])

    # If the Ai can fork
    result = playerCanFork(grid, turn)
    if result != (-1, -1):
        return convertToTextCoords(result[0], result[1])
    
    freeSpace = []
    for x in range(3):
        for y in range(3):
            if getValue(grid, x, y) == 0:
                freeSpace.append(convertToTextCoords(x, y))

    return choice(freeSpace)


"""
Custom input to intercept whatever the player types.
(Handles exit)
"""
def customInput(txt, autoPlay = False, grid = [], player = 0):
    if autoPlay:
        return aiInput(grid, player)
    else:
        while True:
            enteredInput = input(txt)
            if enteredInput.lower() == "exit":
                if input("Est tu sûr? (oui/non) > ").lower() == "oui":
                    exit()
            else:
                return enteredInput

"""
Round handler:
Handles (HUMAN READABLE) player input
"""
def round(grid, player, ai):
    coordinates = (-1, -1)
    while coordinates == (-1, -1):
        clear()
        printGrid(grid)
        print("\nC'est le tour du joueur "+str(player)+"! ("+playerSymbols[player]+")")
        playerInput = customInput("Entrer des coordonnées (e.g: A2) > ", ai == player, grid, player)
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
input("(Appuyez sur entrer pour continuer.)")

grid = createGrid()
turn = 2
playing = True
ai = 0 # Ai's turn, if not 1 or 2, then Ai doesn't play

clear()
print("""
Est-ce que vous voulez jouer contre l'ordinateur?
Si oui, choisissez 1 si vous voulez que l'ordinateur commence, 2 si vous voulez commencer
Sinon, appuyez simplement sur entrer :]
""")
aiStr = input('> ')

if checkInt(aiStr):
    ai = int(aiStr)


while playing:
    turn = (turn%2)+1
    round(grid, turn, ai)
    
    if isWinner(grid, turn):
        clear()
        printGrid(grid)
        print("\nJOUEUR "+str(turn)+" A GAGNÉ!\n")
        input('(Appuyez sur entrer pour continuer.)')
        playing = False
    elif isDraw(grid):
        clear()
        printGrid(grid)
        print("\nÉGALITÉ!\n")
        input('(Appuyez sur entrer pour continuer.)')
        playing = False
    
    if not playing:
        playerResponse = ''
        while playerResponse != "oui" and playerResponse != "non":
            clear()
            playerResponse = customInput("Voulez vous rejouer? (oui/non) > ").lower()
        
        if playerResponse == "oui":
            playing = True
            grid = createGrid()
            turn = 2

            aiStr = ''
            print("""Est-ce que vous voulez jouer contre l'ordinateur?
Si oui, choisissez 1 si vous voulez que l'ordinateur commence, 2 si vous voulez commencer
Sinon, appuyez simplement sur entrer :]
""")
            aiStr = input('> ')

            if checkInt(aiStr):
                ai = int(aiStr)