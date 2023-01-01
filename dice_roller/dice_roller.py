# Dice Roller
from tkinter import *
import tkinter as tk

app = Tk()
app.title("Dice Roller")
photo = PhotoImage(
    file="/Users/andrew./Documents/python_projects/Python Projects 2022/dice_roller/dice.png")
app.iconphoto(False, photo)

# Dice unicode characters dictionary
dice = {
    0: '🎲',
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: '⚃',
    5: '⚄',
    6: '⚅'
}

# First dice character to show when the app starts
label = Label(app, text=dice[0], font=('Times', 100))
label.grid(row=0, column=0, padx=40)


# Choose number from 1 - 6 randomly and display it
def roll():
    from random import randint
    dice_choice = randint(1, 6)

    dice_label = Label(
        app, text=dice[dice_choice], font=('Times', 100), width=2)
    dice_label.grid(row=0, column=0, padx=40)


# Roll button
roll_button = Button(app, text='Roll', command=roll)
roll_button.grid()

app.mainloop()
