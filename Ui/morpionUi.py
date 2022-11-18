from morpionLogic import game
from tkinter import * 
from tkinter.ttk import *
import os.path as path

window = Tk()
window.title("Morpion")
window.geometry("260x325")
window.minsize(260, 325)
window.maxsize(260, 325)

infoImage = PhotoImage(file=path.dirname(__file__)+"/img/info.png")

class GamePage:
    playerSymbols = [
        PhotoImage(file=path.dirname(__file__)+"/img/_.png"), 
        PhotoImage(file=path.dirname(__file__)+"/img/x.png"), 
        PhotoImage(file=path.dirname(__file__)+"/img/o.png")
    ]

    def __init__(self):
        self.turn = 1
        self.currentGame = None
        self.playing = False

        self.frame = Frame(window)

        retryFrame = Frame(self.frame)
        retryFrame.pack(side = BOTTOM, pady=4)

        self.retry = Button(retryFrame, text="REESSAYER?", command=self.newGame)

        self.text = Label(self.frame, text="\nBienvenue!", anchor="center")
        self.text.pack(side = BOTTOM)

        separator = Separator(self.frame, orient='horizontal')
        separator.pack(fill='x', side = BOTTOM, pady=8)

        self.gridContainer = Frame(self.frame)
        self.gridContainer.pack(side = BOTTOM)

        self.info = Button(self.frame, image=infoImage)
        self.info.pack(side = LEFT)

        self.exit = Button(self.frame, text="Quitter")
        self.exit.pack( side = RIGHT )

        self.buttons = [
            [
                Button(self.gridContainer, image=self.playerSymbols[0]) for x in range(3)
            ] for y in range(3)
        ]

        for i in range(3):
            for y in range(3): # FEUR
                b = self.buttons[y][i]
                b.bind("<Button-1>", self.onClickWrapper(y, i))
                b.grid(row = i+1, column = y)
    
    def play(self, x, y):
        if self.currentGame.getValue(x, y) != 0 or not self.playing:
            return
        self.currentGame.setValue(x, y, self.turn)

        self.turn = (self.turn%2)+1
        self.update()

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
            

    def newGame(self):
        self.currentGame = game()
        self.turn = 1
        self.update()

gamePage = GamePage()
gamePage.newGame()
gamePage.frame.pack()

# frame.place(in_=window, anchor="c", relx=.5, rely=.5)

window.mainloop()