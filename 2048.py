"""
Name : 2048.py

Author : Emel Keres

Date : 17.03.2024

Purpose : Projet jeu 2048

Version : Final

"""

# import
import random
from tkinter import *
from tkinter import messagebox

# variable
reset_count = 0
timer_value = 0
timer_running = True
timer_id = None
win = False

def update_timer():
    # cette fonction ajoute des secondes (1s, 2s...)
    global timer_value, timer_running, timer_id
    if timer_running:
        timer_value += 1
        lbl_timer.config(text=f"Temps: {timer_value} s")
        timer_id = root.after(1000, update_timer)

def gagner():
    # cette fonction qui permet au joueur de gagner si 2048 s'affiche dans une case au hasard et de continuer la partie (4096, 8192)
    if win is True :
        return False
    for line in range(len(number)):
        for col in range(len(number[line])):
            if number [line][col] == 2048:
                return True
    return False

def is_game_full():
    # cette fonction fait que si toutes les cases sont remplis, le jeu s'arrête
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
                count += 1

    for col in range(len(number[0])):
        for line in range(len(number)-1):
            if number[line][col] == number[line+1][col]:
                count += 1

    return count

def pack_4(a, b, c, d):
    # déplace et fusionne les valeurs d'une ligne ou colonne
    ligne = [a, b, c, d]
    moves = 0

    # tasser les valeurs vers la gauche
    ligne = [x for x in ligne if x !=0] # sa supprime les 0
    while len(ligne) < 4:
        ligne.append(0) # afficher des 0 apres avoir fait un déplacement (par ex. a gauche), les 0 vont s'afficher (par ex. a droite)
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
    # cette fonction réinitialise le plateau et incrémente le compteur de resets
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

    restart_timer()

def restart_timer():
    # cette fonction sert a quand on appuie sur le bouton "Nouveau", le timer ce remet a 0
    global timer_value, timer_running, timer_id
    timer_value = 0
    timer_running = True
    lbl_timer.config(text=f"Temps: {timer_value} s")

    if timer_id is not None:  # vérifie s'il y a un timer en cours
        root.after_cancel(timer_id)  # annule l'ancien timer

    update_timer()

def ajouter_nouveau_nombre():
    # cette fonction ajoute un '2' qui a 80% de chance de tomber au hasard, il s'ajoute dans une case vide et un '4' qui a 20% de chance de tomber au hasard
    cases_vides = [(i, j) for i in range(4) for j in range(4) if number[i][j] == 0]
    choix = random.choices([2, 4], weights=[80, 20])[0]
    i1, j1 = random.choice(cases_vides)
    cases_vides.remove((i1, j1))
    number[i1][j1] = choix

    display_game()

def display_game():
    # cette fonction met a jour les nombres afficher sur le plateau
    for i in range(4):
        for j in range(4):
            valeur = number[i][j]
            texte = str(valeur) if valeur > 0 else ""
            cases[i][j].config(text=texte, bg=color.get(valeur, "#FFFFFF"))

def changer_couleur_fond():
    # cette fonction sert a afficher des couleurs aléatoirements avec des couleurs prédéfinis
    couleurs = ["#FFD700", "#FF4500", "#32CD32", "#8A2BE2", "#FF69B4", "#00CED1", "#FF6347"]
    couleur_aleatoire = random.choice(couleurs)

    # modifie la couleur de fond de la fenêtre
    root.configure(bg=couleur_aleatoire)

    # modifie la couleur de fond des frames
    frame_logo.configure(bg=couleur_aleatoire)
    frame_nouveau_quitter.configure(bg=couleur_aleatoire)

    # modifie la couleur de fond des labels
    lbl_logo.configure(bg=couleur_aleatoire)
    lbl_nouveau_quitter.configure(bg=couleur_aleatoire)
    lbl_text.configure(bg=couleur_aleatoire)
    lbl_timer.configure(bg=couleur_aleatoire)

def mouvement_gauche():
    global win
    # déplacement vers la gauche avec la flèche directionnel, fusion des cases vers la gauche
    moves = 0
    for i in range(4):
        number[i][0], number[i][1], number[i][2], number[i][3], move = pack_4(
            number[i][0], number[i][1], number[i][2], number[i][3]
        )
        moves += move
    if moves > 0:
        ajouter_nouveau_nombre()
        changer_couleur_fond()
        if gagner():
            win = True
            messagebox.showinfo("Information", "Vous avez atteint 2048")
        if is_game_full() and count_mergeable() == 0:
            global timer_running
            timer_running = False  # stoppe le timer
            messagebox.showinfo("Information", "Vous avez perdu, appuyez sur le bouton Nouveau")

def mouvement_droite():
    global win
    # déplacement vers la droite avec la flèche directionnel, fusion des cases vers la droite
    moves = 0
    for i in range(4):
        number[i][3], number[i][2], number[i][1], number[i][0], move = pack_4(
            number[i][3], number[i][2], number[i][1], number[i][0]
        )
        moves += move
    if moves > 0:
        ajouter_nouveau_nombre()
        changer_couleur_fond()
        if gagner():
            win = True
            messagebox.showinfo("Information", "Vous avez atteint 2048")
        if is_game_full() and count_mergeable() == 0:
            global timer_running
            timer_running = False  # stoppe le timer
            messagebox.showinfo("Information", "Vous avez perdu, appuyez sur le bouton Nouveau")

def mouvement_haut():
    global win
    # déplacement vers le haut avec la flèche directionnel, fusion des cases vers le haut
    moves = 0
    for j in range(4):
        number[0][j], number[1][j], number[2][j], number[3][j], move = pack_4(
            number[0][j], number[1][j], number[2][j], number[3][j]
        )
        moves += move
    if moves > 0:
        ajouter_nouveau_nombre()
        changer_couleur_fond()
        if gagner():
            win = True
            messagebox.showinfo("Information", "Vous avez atteint 2048")
        if is_game_full() and count_mergeable() == 0:
            global timer_running
            timer_running = False  # stoppe le timer
            messagebox.showinfo("Information", "Vous avez perdu, appuyez sur le bouton Nouveau")

def mouvement_bas():
    global win
    # déplacement vers le haut avec la flèche directionnel, fusion des cases vers le bas
    moves = 0
    for j in range(4):
        number[3][j], number[2][j], number[1][j], number[0][j], move = pack_4(
            number[3][j], number[2][j], number[1][j], number[0][j]
        )
        moves += move
    if moves > 0:
        ajouter_nouveau_nombre()
        changer_couleur_fond()
        if gagner():
            win = True
            messagebox.showinfo("Information", "Vous avez atteint 2048")
        if is_game_full() and count_mergeable() == 0:
            global timer_running
            timer_running = False  # stoppe le timer
            messagebox.showinfo("Information", "Vous avez perdu, appuyez sur le bouton Nouveau")

def quit():
    # cette fonction fait quitter la fenêtre avec le bouton "Quitter"
    global btn_quitter
    root.quit()

# la fenêtre
root = Tk()
root.title("2048")
root.geometry("620x620")
root.configure(bg='#CCCCFF')

# grille du jeu (valeurs en puissances de 2)
# plateau vide au départ
number = [[0 for _ in range(4)] for _ in range(4)]

# interface graphique
cases = [[None for _ in range(4)] for _ in range(4)]
color = {
    0: "#FFFFFF", 2: "#CDA2BE", 4: "#B5739D", 8: "#C3ABD0", 16: "#A680B8",
    32: "#A9C4EB", 64: "#7EA6E0", 128: "#9AC7BF", 256: "#67AB9F", 512: "#B9E0A5",
    1024: "#97D077", 2048: "#FFD966", 4096: "#FFD966", 8192: "#FFD966"
}

# associer les touches aux mouvements (gacuhe, droite, haut, bas)
root.bind("<Left>", lambda event: mouvement_gauche())
root.bind("<Right>", lambda event: mouvement_droite())
root.bind("<Up>", lambda event: mouvement_haut())
root.bind("<Down>", lambda event: mouvement_bas())

# frame
frame_logo = Frame(root, bg='#CCCCFF')
frame_logo.pack(padx=15, pady=10, fill=X)
frame_nouveau_quitter = Frame(root, bg='#CCCCFF')
frame_nouveau_quitter.pack(padx=15, fill=X)
lbl_timer = Label(root, text=f"Temps: {timer_value} s", font=("Arial", 13), bg='#CCCCFF')
lbl_timer.pack()
frame_cases = Frame(root, bg='#B3B3B3', width=415, height=430)
frame_cases.pack(padx=15, pady=25)

# la boucle permet de faire les cases (4 lignes et 4 colonnes) avec la couleur des chiffres, la taille des cases, l'arrière plan des cases
for i in range(4):
    for j in range(4):
        cases[i][j] = Label(frame_cases, text="", width=8, height=4, relief='solid', font=("Arial", 15), bg=color[0], fg="white")
        cases[i][j].place(x=10 + 100 * j, y=10 + 105 * i)

# label
lbl_logo = Label(frame_logo, text="2048", font=("Arial", 40), bg='#CCCCFF')
lbl_logo.pack(side=LEFT)
lbl_nouveau_quitter = Label(frame_nouveau_quitter, bg='#CCCCFF')
lbl_nouveau_quitter.pack(side=RIGHT)
lbl_text = Label(frame_nouveau_quitter, text="Glissez les chiffres et obtenez la tuile 2048 !", font=("Arial", 10), bg='#CCCCFF')
lbl_text.pack(side=LEFT)

# bouton
btn_quitter = Button(frame_nouveau_quitter,text="Quitter", font=("Arial", 10), bg='#B3B3B3', command=quit)
btn_quitter.pack(side=RIGHT)
btn_nouveau = Button(frame_nouveau_quitter,text="Nouveau", font=("Arial", 10), bg='#B3B3B3', command=reset_plateau)
btn_nouveau.pack(side=RIGHT, padx=10)

# afficher les deux premiers chiffres sur les cases
ajouter_nouveau_nombre()
ajouter_nouveau_nombre()

# affiche le timer
update_timer()

root.mainloop()