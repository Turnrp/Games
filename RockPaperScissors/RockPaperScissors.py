import tkinter as tk
from tkinter.constants import FALSE, N, S, SE, SW
from random import randint

OpponentChoice = randint(0, 2)
_Wins = ((1, 0), (2, 1), (0, 2))
TopText = "Welcome To Rock Paper Scissors!"
Score = 0
#Functions

def Rock():
    SetPlayerChoice(0)
def Paper():
    SetPlayerChoice(1)
def Scissors():
    SetPlayerChoice(2)

def SetPlayerChoice(button):
    global OpponentChoice
    global TopText
    global score
    global Score
    global title
    OpponentChoice = randint(0, 2)

    if(CheckWinner(button) == True):
        TopText = "Winner!"
        Score+=1
    elif(CheckWinner(button) == False):
        TopText = "Loser..."
        Score-=1
    else:
        TopText = "Tie"

    title.config(text=TopText)
    score.config(text=Score)

def CheckWinner(choice):
    global OpponentChoice
    print(OpponentChoice, choice)
    if(OpponentChoice != choice):
        for i in _Wins:
            if(OpponentChoice == i[0] and choice == i[1]):
                return False
            elif(OpponentChoice == i[1] and choice == i[0]):
                return True
    else:
        return 2
#Actual Stuff

window = tk.Tk()
window.title("")
p1 = tk.PhotoImage(file = 'Sprites/icon.png')
window.iconphoto(False, p1)
window.minsize(200, 150)
window.maxsize(200, 150)

#Rock=0 Paper=1 Scissors=2
title = tk.Label(text=TopText, anchor=N, master=window)
rock = tk.Button(text="Rock", anchor=SE, command=Rock, master=window)
paper = tk.Button(text="Paper", anchor=S, command=Paper, master=window)
scissors = tk.Button(text="Scissors", anchor=SW, command=Scissors, master=window)
score = tk.Label(text=Score, anchor=S)

title.pack()

rock.pack()
paper.pack()
scissors.pack()

score.pack()

window.mainloop()