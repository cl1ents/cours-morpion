from morpionLogic import game
from Ai import minmax
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
import os.path as path

import threading
import time

window = tk.Tk()
window.title("Morpion")
width = 260 # Width 
height = 325 # Height

screen_width = window.winfo_screenwidth()  # Width of the screen
screen_height = window.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.minsize(width, height)
window.maxsize(width, height)

infoImage = tk.PhotoImage(file=path.dirname(__file__)+"/img/info.png")

titleFont = font.Font(size = 15, family="Segoe Ui", weight="bold")
bigButtonFont = font.Font(size = 14, family="Segoe Ui")

class MainMenu:
    def __init__(self, gamePage):
        self.frame = tk.Frame(window)
        self.gamePage = gamePage
        gamePage.mainMenu = self

        text = ttk.Label(self.frame, 
            text="\nBienvenue au Morpion!\n☆*: .｡. o(≧▽≦)o .｡.:*☆", 
            anchor="center", 
            font=titleFont, 
            justify=tk.CENTER)

        buttonPVP = tk.Button(self.frame, text="CONTRE UN JOUEUR", command=self.start, font=bigButtonFont)
        buttonAi = tk.Button(self.frame, text="CONTRE UNE IA", command=self.aiStart, font=bigButtonFont)

        text.pack(pady=20)
        buttonPVP.pack(pady=20)
        buttonAi.pack(pady=20)
    
    def start(self):
        self.frame.pack_forget()
        self.gamePage.ai = False
        self.gamePage.newGame()
        self.gamePage.frame.pack()

    def aiStart(self):
        self.frame.pack_forget()
        self.gamePage.ai = True
        self.gamePage.newGame()
        self.gamePage.frame.pack()

class GamePage:
    playerSymbols = [
        tk.PhotoImage(file=path.dirname(__file__)+"/img/_.png"), 
        tk.PhotoImage(file=path.dirname(__file__)+"/img/x.png"), 
        tk.PhotoImage(file=path.dirname(__file__)+"/img/o.png")
    ]

    def __init__(self):
        self.turn = 2
        self.lastTurn = 2
        self.currentGame = None
        self.playing = False
        self.canPlay = False

        self.frame = tk.Frame(window)

        retryFrame = tk.Frame(self.frame)
        retryFrame.pack(side = tk.BOTTOM, pady=4)

        self.retry = ttk.Button(retryFrame, text="REESSAYER?", command=self.newGame)

        self.text = ttk.Label(self.frame, text="\nBienvenue!", anchor="center")
        self.text.pack(side = tk.BOTTOM)

        separator = ttk.Separator(self.frame, orient='horizontal')
        separator.pack(fill='x', side = tk.BOTTOM, pady=8)

        self.gridContainer = tk.Frame(self.frame)
        self.gridContainer.pack(side = tk.BOTTOM)

        self.info = ttk.Button(self.frame, image=infoImage, command=self.showInfo)
        self.info.pack(side = tk.LEFT)

        self.exit = ttk.Button(self.frame, text="Quitter", command=self.back)
        self.exit.pack( side = tk.RIGHT )

        self.buttons = [
            [
                tk.Button(self.gridContainer, image=self.playerSymbols[0]) for x in range(3)
            ] for y in range(3)
        ]

        for i in range(3):
            for y in range(3): # FEUR
                b = self.buttons[y][i]
                b.bind("<Button-1>", self.onClickWrapper(y, i))
                b.grid(row = i+1, column = y)
    
    def back(self):
        self.frame.pack_forget()
        self.mainMenu.frame.pack()

    def showInfo(self):
        messagebox.showinfo("Règles", """Le but du jeu est simple:

Il suffit d'aligner, avant son adversaire, 3 symboles identiques horizontalement, verticalement ou en diagonale sur une grille de 3x3.
Le joueur ayant aligné 3 symboles gagne la partie.
Le joueur 1 a le symbole X et le joueur 2 a le symbole O
Pour jouer, le joueur clique la case où il veut jouer.""")

    def play(self, x, y):
        if self.currentGame.getValue(x, y) != 0 or not self.playing or not self.canPlay:
            return
        self.currentGame.setValue(x, y, self.turn)

        self.turn = (self.turn%2)+1
        self.update()
    
    def botPlay(self):
        time.sleep(.05)
        score, move = minmax(self.currentGame.grid, 2)
        self.canPlay = True
        self.play(move[0], move[1])

    def onClickWrapper(self, x, y):
        return lambda Button: self.play(x, y)
    
    def update(self):
        if self.currentGame:
            for x in range(3):
                for y in range(3):
                    self.buttons[x][y].config(image=self.playerSymbols[self.currentGame.getValue(x, y)])
            
            self.text.configure(text= "Joueur 1 a gagné!" if self.currentGame.isWinner(1) else "Joueur 2 a gagné!" if self.currentGame.isWinner(2) else "ÉGALITÉ!" if self.currentGame.isDraw() else f"C'est le tour du joueur {self.turn}." )

            self.playing = not (self.currentGame.isWinner(1) or self.currentGame.isWinner(2) or self.currentGame.isDraw())
            if self.playing:
                self.retry.pack_forget()
            else:
                self.retry.pack()
            
            if self.ai and self.turn == 2 and self.playing:
                self.canPlay = False
                self.text.configure(text="L'ordinateur reflechis...")
                thread = threading.Thread(target=self.botPlay)
                thread.daemon = True
                thread.start()
            else:
                self.canPlay = True
            
    def newGame(self):
        self.currentGame = game()
        self.turn = (not (self.lastTurn-1)) + 1
        self.lastTurn = self.turn
        self.update()


MainMenu(GamePage()).frame.pack()

# frame.place(in_=window, anchor="c", relx=.5, rely=.5)

window.mainloop()
