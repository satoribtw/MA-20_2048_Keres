"""
Name : 2048.py

Author : Emel Keres

Date : 10.02.2024

Purpose : Projet jeu 2048

Version : 0.2

"""

import random
from tkinter import *

reset_count = 0

def display_game():
    for line in range(len(cases)):
        for col in range(len(cases[line])):
            cases[line][col].config(
                text=2**number[line][col],
                bg=color[number[line][col]]
            )

def pack_4(a, b, c, d):
    # déplace et fusionne les valeurs d'une ligne ou colonne
    ligne = [a, b, c, d]
    moves = 0

    # tasser les valeurs vers la gaiche
    ligne = [x for x in ligne if x !=0] # sa supprime les 0
    while len(ligne) < 4:
        ligne.append(0) # afficher des 0 apres avoir fait un déplacement a gauche, les 0 vont s'afficher a droite
    if [a, b, c, d] != ligne:
        moves += 1

    # fusionner les valeurs identiques (par ex. 4+4=8)
    for i in range(3):
        if ligne [i] == ligne[i + 1] and ligne [i] != 0:
            ligne[i] *= 2
            ligne[i + 1] = 0
            moves += 1

    # retasser apres la fusion
    ligne = [x for x in ligne if x != 0]
    while len(ligne) < 4:
        ligne.append(0)
    return ligne[0], ligne[1], ligne[2], ligne[3], moves

def reset_plateau():
    # sa réinitialise le plateau et incrémente le compteur de resets
    global reset_count
    reset_count += 1

    # rénitialise toutes les cases à 0
    for i in range (4):
        for j in range(4):
            number[i][j] = 0

    # ajouteur deux nombre au départ (2 et 2)
    ajouter_nouveau_nombre()
    ajouter_nouveau_nombre()

    # met a jour l'affichage
    mise_a_jour_affichage()

def ajouter_nouveau_nombre():
    # ajoute un '2' dans une case vide, ou un '4' après 9 resets
    cases_vides = [(i, j) for i in range(4) for j in range(4) if number[i][j] == 0]
    if cases_vides:
        i, j = random.choice(cases_vides)
        number[i][j] = 1 if reset_count % 9 != 0 else 2  # 4 après 9 resets, sinon 2
        mise_a_jour_affichage()

def mise_a_jour_affichage():
    # met a jour des nombres afficher sur le plateau
    for i in range(4):
        for j in range(4):
            valeur = number[i][j]
            texte = str(valeur) if valeur > 0 else ""
            cases[i][j].config(text=texte, bg=color.get(valeur, "#FFFFFF"))

def mouvement_gauche():
    # déplacement vers la gauche avec la flèche directionnel, fusion des cases vers la gauche
    moves = 0
    for i in range(4):
        number[i][0], number[i][1], number[i][2], number[i][3], move = pack_4(
            number[i][0], number[i][1], number[i][2], number[i][3]
        )
        moves += move
    if moves > 0:
        ajouter_nouveau_nombre()

def mouvement_droite():
    # déplacement vers la droite avec la flèche directionnel, fusion des cases vers la droite
    moves = 0
    for i in range(4):
        number[i][3], number[i][2], number[i][1], number[i][0], move = pack_4(
            number[i][3], number[i][2], number[i][1], number[i][0]
        )
        moves += move
    if moves > 0:
        ajouter_nouveau_nombre()


def mouvement_haut():
    # déplacement vers le haut avec la flèche directionnel, fusion des cases vers le haut
    moves = 0
    for j in range(4):
        number[0][j], number[1][j], number[2][j], number[3][j], move = pack_4(
            number[0][j], number[1][j], number[2][j], number[3][j]
        )
        moves += move
    if moves > 0:
        ajouter_nouveau_nombre()


def mouvement_bas():
    # déplacement vers le haut avec la flèche directionnel, fusion des cases vers le bas
    moves = 0
    for j in range(4):
        number[3][j], number[2][j], number[1][j], number[0][j], move = pack_4(
            number[3][j], number[2][j], number[1][j], number[0][j]
        )
        moves += move
    if moves > 0:
        ajouter_nouveau_nombre()

root = Tk()
root.title("2048")
root.geometry("500x500")

# grille du jeu (valeurs en puissances de 2)
number = [[0 for _ in range(4)] for _ in range(4)]  # Plateau vide au départ

# interface graphique
cases = [[None for _ in range(4)] for _ in range(4)]
color = {
    0: "#FFFFFF", 2: "#CDA2BE", 4: "#B5739D", 8: "#C3ABD0", 16: "#A680B8",
    32: "#A9C4EB", 64: "#7EA6E0", 128: "#9AC7BF", 256: "#67AB9F", 512: "#B9E0A5",
    1024: "#97D077", 2048: "#FFD966"
}

for i in range(4):
    for j in range(4):
        cases[i][j] = Label(root, text="", width=7, height=3, relief='solid', font=("Arial", 15), bg=color[0], fg="black")
        cases[i][j].place(x=70 + 90 * j, y=150 + 85 * i)

# associer les touches aux mouvements (gacuhe, droite, haut, bas)
root.bind("<Left>", lambda event: mouvement_gauche())
root.bind("<Right>", lambda event: mouvement_droite())
root.bind("<Up>", lambda event: mouvement_haut())
root.bind("<Down>", lambda event: mouvement_bas())

# frame
frame_score_top = LabelFrame(root)
frame_score_top.pack(side=RIGHT)
frame_score = LabelFrame(frame_score_top)
frame_score.pack(side=LEFT)
frame_top = LabelFrame(frame_score_top)
frame_top.pack(side=RIGHT)
frame_logo = LabelFrame(root)
frame_logo.pack(padx=15, pady=10, fill=X)
frame_nouveau = LabelFrame(root)
frame_nouveau.pack()

# label
lbl_score_top = Label(frame_score_top)
lbl_score_top.pack()
lbl_logo = Label(frame_logo, text="2048", font=("Arial", 50))
lbl_logo.pack(side=LEFT)

# afficher les premiers chiffres
ajouter_nouveau_nombre()
ajouter_nouveau_nombre()

root.mainloop()