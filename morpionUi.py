from morpionLogic import game
from tkinter import * 
from tkinter.ttk import *

window = Tk()

class gamePage:
    playerSymbols = [
        PhotoImage(file="img/_.png"), 
        PhotoImage(file="img/x.png"), 
        PhotoImage(file="img/o.png")
    ]

    def __init__(self):
        self.turn = 1

        self.frame = Frame(window)
        self.frame.pack()

        self.info = Button(self.frame, text="i")
        self.info.grid(row=0, column=0)

        self.exit = Button(self.frame, text="Exit")
        self.exit.grid(row=0, column=2)

        self.buttons = [
            [
                Button(self.frame, image=self.playerSymbols[0]) for x in range(3)
            ] for y in range(3)
        ]

        for x in range(3):
            for y in range(3):
                b = self.buttons[y][x]
                id = str(x)+str(y)
                def lol():
                    print(id)
                b.config(command=lol)
                b.grid(row = x+1, column = y)
    
    def setGrid(self, grid):
        for x in range(3):
            for y in range(3):
                self.buttons[x][y].config(image=self.playerSymbols[grid[y][x]])

gamePage().setGrid([
        [1,0,0],
        [0,2,2],
        [0,0,1]
    ])

# frame.place(in_=window, anchor="c", relx=.5, rely=.5)

window.mainloop()