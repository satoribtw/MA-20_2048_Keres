"""
Name : 2048.py

Author : Emel Keres

Date : 20.01.2024

Purpose : Projet jeu 2048

Version : 0.02

"""

from tkinter import *

root = Tk()
root.title("2048")
root.geometry("500x500")

puissances = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,0]
]

cases = [
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None],
    [None,None,None,None]
]

color = {
    1 : "#CDA2BE",
    2 : "#B5739D",
    3 : "#C3ABD0",
    4 : "#A680B8",
    5 : "#A9C4EB",
    6 : "#7EA6E0",
    7 : "#9AC7BF",
    8 : "#67AB9F",
    9 : "#B9E0A5",
    10 : "#97D077",
    11 : "#FFE599",
    12 : "#FFD966",
    13 : "#FFD966",
    14 : "#FFFFFF",
    15 : "#FFFFFF",
    0 : "#FFFFFF"
}

for line in range(len(puissances)):
    for col in range(len(puissances[line])):
        cases[line][col] = Label(root, text=2**puissances[line][col], width=7, height=3, relief='solid', font=("Arial",15), bg=color[puissances[line][col]], fg="white")
        cases[line][col].place(x=70 + 90 * col, y=150 + 85 * line)

# frame
frame_score_top_logo = LabelFrame(root)
frame_score_top_logo.pack()
frame_score_top = LabelFrame(frame_score_top_logo)
frame_score_top.pack(side=RIGHT)
frame_score = LabelFrame(frame_score_top)
frame_score.pack(side=LEFT)
frame_top = LabelFrame(frame_score_top)
frame_top.pack(side=RIGHT)
frame_logo = LabelFrame(root)
frame_logo.pack(side=LEFT, padx=15, pady=10)
frame_nouveau = LabelFrame(root)
frame_nouveau.pack()

# label
lbl_score_top = Label(frame_score_top)
lbl_score_top.pack()
lbl_logo = Label(frame_score_top_logo, text="2048", font=("Arial", 50))
lbl_logo.pack(side=LEFT)

root.mainloop()