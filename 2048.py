"""
Name : 2048.py

Author : Emel Keres

Date : 03.03.2024

Purpose : Projet jeu 2048

Version : 0.3

"""

# import
import random
from tkinter import *
from tkinter import messagebox

win = False

def gagner():
    # fonction qui permet au joueur de gagner si 2048 s'affiche dans une case au hasard et de continuer la partie (4096, 8192)
    if win == True:
        return False
    for line in range(len(number)):
        for col in range(len(number[line])):
            if number [line][col] == 2048:
                return True
    return False

def is_game_full():
    # fonction qui fait que si toutes les cases sont remplis, le jeu s'arrete
    for line in range(len(number)):
        for col in range(len(number[line])):
            if number [line][col] == 0:
                return False
    return True

def count_mergeable():
    # cette fonction fait le compte fusionnable
    count = 0
    for line in range (len(number)):
        for col in range (len(number[line])-1):
            if number [line][col] == number [line][col+1]:
                count +=1

    for col in range(len(number[0])):
        for line in range(len(number)-1):
            if number[line][col] == number[line+1][col]:
                count += 1

    return count

reset_count = 0

def pack_4(a, b, c, d):
    # déplace et fusionne les valeurs d'une ligne ou colonne
    ligne = [a, b, c, d]
    moves = 0

    # tasser les valeurs vers la gauche
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
    global reset_count, win
    win = False
    reset_count += 1

    # rénitialise toutes les cases à 0
    for i in range (4):
        for j in range(4):
            number[i][j] = 0

    # ajouteur deux nombre au départ (2 et 2)
    ajouter_nouveau_nombre()
    ajouter_nouveau_nombre()

    # met a jour l'affichage
    display_game()

def ajouter_nouveau_nombre():
    # ajoute un '2' qui a 80% de chance de tomber au hasard, il s'ajoute dans une case vide et un '4' qui a 20% de chance de tomber au hasard
    cases_vides = [(i, j) for i in range(4) for j in range(4) if number[i][j] == 0]
    choix = random.choices([2, 4], weights=[80, 20])[0]
    i1, j1 = random.choice(cases_vides)
    cases_vides.remove((i1, j1))
    number[i1][j1] = choix

    display_game()

def display_game():
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
        if gagner():
            win = True
            messagebox.showinfo("Information", "Vous avez atteint 2048")
        if is_game_full() and count_mergeable() == 0:
            messagebox.showinfo("Information", "Vous avez perdu")

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
        if gagner():
            win = True
            messagebox.showinfo("Information", "Vous avez atteint 2048")
        if is_game_full() and count_mergeable() == 0:
            messagebox.showinfo("Information", "Vous avez perdu")

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
        if gagner():
            win = True
            messagebox.showinfo("Information", "Vous avez atteint 2048")
        if is_game_full() and count_mergeable() == 0:
            messagebox.showinfo("Information", "Vous avez perdu")

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
        if gagner():
            win = True
            messagebox.showinfo("Information", "Vous avez atteint 2048")
        if is_game_full() and count_mergeable() == 0:
            messagebox.showinfo("Information", "Vous avez perdu")

# la fenêtre
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
    1024: "#97D077", 2048: "#FFD966", 4096: "#FFD966", 8192: "#FFD966"
}

for i in range(4):
    for j in range(4):
        cases[i][j] = Label(root, text="", width=7, height=3, relief='solid', font=("Arial", 15), bg=color[0], fg="white")
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

# bouton
btn_nouveau = Button(frame_nouveau,text="Nouveau", font=("Arial", 15), command=reset_plateau)
btn_nouveau.pack()

# afficher les premiers chiffres
ajouter_nouveau_nombre()
ajouter_nouveau_nombre()

root.mainloop()