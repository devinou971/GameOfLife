#coding:utf-8
"""

Python 3.X

Damien DASSEUX
Arnaud DIONISIUS

Game Of Life

"""

def reload(): # cette fonction permettra de rafraichir le canvas
    can.delete(ALL)

    # On crée le grillage
    for x in range(resolution[0]+1):
    	can.create_line(pas*x,0,pas*x,height)
    for y in range(resolution[1]+1):
    	can.create_line(0,pas*y,width,pas*y)

    # On dessine toutes le cellules qui sont dans tout les différents stades
    for i in range(len(stade_1)):

        x0 = (stade_1[i][0] + pos[0]) * pas # le pos[0] en est le décalage de la grille que l'on doit prendre en compte
        y0 = (stade_1[i][1] + pos[1]) * pas
        x1 = x0 + pas
        y1 = y0 + pas

        can.create_rectangle(x0 , y0 , x1 , y1 , fill=couleur[1]) # On dessine un rectangle noire

    for i in range(len(stade_2)):

        x0 = (stade_2[i][0] + pos[0]) * pas
        y0 = (stade_2[i][1] + pos[1]) * pas
        x1 = x0 + pas
        y1 = y0 + pas
 
        can.create_rectangle(x0 , y0 , x1 , y1 , fill=couleur[2])

    for i in range(len(stade_3)):

        x0 = (stade_3[i][0] + pos[0]) * pas
        y0 = (stade_3[i][1] + pos[1]) * pas
        x1 = x0 + pas
        y1 = y0 + pas

        can.create_rectangle(x0 , y0 , x1 , y1 , fill=couleur[3])

    for i in range(len(stade_4)):

        x0 = (stade_4[i][0] + pos[0]) * pas
        y0 = (stade_4[i][1] + pos[1]) * pas
        x1 = x0 + pas
        y1 = y0 + pas

        can.create_rectangle(x0 , y0 , x1 , y1 , fill=couleur[4])

    for i in range(len(stade_5)):

        x0 = (stade_5[i][0] + pos[0]) * pas
        y0 = (stade_5[i][1] + pos[1]) * pas
        x1 = x0 + pas
        y1 = y0 + pas

        can.create_rectangle(x0 , y0 , x1 , y1 , fill=couleur[5])

def click_case(event): # cette fonction intervient quand l'on appuie dans le canvas et permet de remplir les tableaux de vie
	global stade_1, gen, gen_IntVar, choix, stade_2, stade_3, stade_4, stade_5, pos
	x , y = event.x, event.y # on prend la position de la souris
	i = 0 # la position des cases
	j = 0 # la position des cases
	while pas * i <= x:
		i = i + 1
	while pas * j <= y:
		j = j + 1

	pos_case_clicke = [i-1-pos[0], j-1-pos[1]] # cette variable contient le numéro de colone et de ligne de la case clické
	
	# on regarde si cette cellule n'est pas présente dans n'importe quel tableau de vie
	if pos_case_clicke in stade_1:
		stade_1.remove(pos_case_clicke) # si c'est le cas, on supprime la cellule
	elif pos_case_clicke in stade_2:
		stade_2.remove(pos_case_clicke)
	elif pos_case_clicke in stade_3:
		stade_3.remove(pos_case_clicke)
	elif pos_case_clicke in stade_4:
		stade_4.remove(pos_case_clicke)
	elif pos_case_clicke in stade_5:
		stade_5.remove(pos_case_clicke)

	elif choix == "stade 1": # si la cellule n'est présente nul part on l'ajoute la ou elle doit être
		stade_1.append(pos_case_clicke)
	elif choix == "stade 2":
		stade_2.append(pos_case_clicke)
	elif choix == "stade 3":
		stade_3.append(pos_case_clicke)
	elif choix == "stade 4":
		stade_4.append(pos_case_clicke)
	elif choix == "stade 5":
		stade_5.append(pos_case_clicke)

	gen = 0 # on remet la variable des génération à 0
	gen_IntVar.set(0)
	reload() # on rafrachit le canvas

def jouer(): # cette fonction permet de faire jouer e jeu automatiquement
        global play, gen_IntVar, gen, stade_1, stade_2, stade_3, stade_4, stade_5
        play = True
        while play:
                algorithme(stade_1, stade_2, stade_3, stade_4, stade_5)
                reload()
                gen = gen + 1
                gen_IntVar.set(gen)
                #can.update_idletasks() # on update toutes les précédentes fonctions
                can.update() # on update la fenetre
def spaceBar(*arg):
        global play, gen_IntVar, gen, stade_1, stade_2, stade_3, stade_4, stade_5
        if play:
                stopper()
        else :
        		jouer()

def next(*arg):
    algorithme(stade_1, stade_2, stade_3, stade_4, stade_5)
    reload()

def stopper(): # ici on arrete le jeu en cours
	global play
	play = False

def reset(*arg): # permet de tout arreter et de tout reinitialiser
    global play, stade_1, gen, gen_IntVar, stade_2, stade_3, stade_4, stade_5, pos
    pos = [0, 0]
    play = False
    stade_1 = []
    stade_2 = []
    stade_3 = []
    stade_4 = []
    stade_5 = []
    gen = 0
    gen_IntVar.set(0)
    reload()

def zoomM(*arg): # cette fonction permet de dézoomer
	global pas, resolution
	if pas != 1 and pas !=1: # on vérifie que pas et pas n'est pas éguale à 1 car, si c'est le cas, on aura un erreur : division par 0
		pas = pas - 1 # on décrémente la largeur des carrés
	resolution = [int(width / pas), int(height / pas)] # on regle la résolution
	reload() # on rafraichit la canvas

def zoomP(*arg): # cette fonction permet de zoomer
        global pas, resolution
        pas = pas + 1 # on incrémente la largeur des carrés
        resolution = [int(width / pas), int(height / pas)] # on regle la résolution
        reload() # on rafraichit le canvas

def goUp(*arg): # cette fonction permet de monter dans la grille
	global pos
	pos[1] = pos[1] + 1
	reload()

def goDown(*arg): # cette fonction permet de descendre dans la grille
	global pos
	pos[1] = pos[1] - 1
	reload()

def goLeft(*arg): # cette fonction permet d'aller à gauche dans la grille
	global pos
	pos[0] = pos[0] + 1
	reload()

def goRight(*arg): # cette fonction permet d'aller à la droite dans la grille
	global pos
	pos[0] = pos[0] - 1
	reload()

def Ouvrir(*arg):
	global play, stade_1, stade_2, stade_3, stade_4, stade_5
	play = False
	path = askopenfilename(initialdir = "save/", filetypes=[('json files', '.json'), ('all files', '')])
	doc = 0
	ok = True
	try:
		doc = open(path, "r")
	except TypeError :
		print("Aucun fichier sélectionné")
		ok = False
	except FileNotFoundError:
		print("Aucun fichier sélectionné")
		ok = False
	if ok :
		save = json.load(doc)
		if save["commentaire"] == "save":
			stade_1 = save["stade_1"]
			stade_2 = save["stade_2"]
			stade_3 = save["stade_3"]
			stade_4 = save["stade_4"]
			stade_5 = save["stade_5"]
		else:
			showerror("Ouverture", "Ceci n'est pas un fichier de sauvegarde")
		reload()

def Sauver(*arg):
	global play, stade_1, stade_2, stade_3, stade_4, stade_5
	play = False
	path = asksaveasfilename(initialdir = "save/", filetypes=[('json files', '.json')])
	if not path == "":
		if not path[-5:] == ".json":
			path = path + ".json"
		doc = open(path, "w")
		doc.write(json.dumps({"commentaire" : "save", "stade_1" : stade_1, "stade_2" : stade_2, "stade_3" : stade_3, "stade_4" : stade_4, "stade_5" : stade_5}, ensure_ascii=False))
		doc.close()

def changerAlgo(preference, play):
	play = False
	path = askopenfilename(initialdir = "algo/", filetypes=[('Python files', '.py'), ('all files', '')])
	if path != "":
		name = path.split("/")[len(path.split("/"))-1]
		fichierpreference = open("preference/preference.json", "w") 
		fichierpreference.write(json.dumps({"couleur" : list(preference["couleur"]), "algo_de_base" : str(name), "pas" : int(preference["pas"]), "width" : int(preference["width"]), "height" : int(preference["height"]), "theme" : str(preference["theme"])}, ensure_ascii=False))
		fichierpreference.close()
		showinfo("Algorithme", "Le changement d'algorithme sera pris en compte lors du prochain démarage du programme")

def changerTheme(preference, play):
	play = False
	path = askopenfilename(initialdir = "preference/theme/", filetypes=[('json files', '.json'), ('all files', '')])
	if path != "":
		name = path.split("/")[len(path.split("/"))-1]
		fichierpreference = open("preference/preference.json", "w") 
		fichierpreference.write(json.dumps({"couleur" : list(preference["couleur"]), "algo_de_base" : str(preference["algo_de_base"]), "pas" : int(preference["pas"]), "width" : int(preference["width"]), "height" : int(preference["height"]), "theme" : str(name)}, ensure_ascii=False))
		fichierpreference.close()

		fichierpreference = open("preference/preference.json", "r")  # On ouvre le fichier de préference
		preference = json.load(fichierpreference) # on transforme son contenu en dictionnaire
		fichierpreference.close() # fermeture du fichier

		fichiertheme = open("preference/theme/"+preference["theme"], "r") # Ouverture du fichier de theme
		theme = json.load(fichiertheme) # transforamtion du contenu en dictionnaire
		fichiertheme.close() # fermeture du fichier

		showinfo("Theme", "Le changement de theme sera pris en compte lors du prochain démarage du programme")

def aide():
	helps = Tk()
	helps.configure(bg = theme["bg"])
	helps.title("Aide")
	Label(helps,text = "Raccourcis : \n\nO ->\n\nS ->\n\nR ->\n\nP ->\n\nM ->\n\nBarre espace ->\n\nCroix directionnel ->", bg=theme["bg"], fg = theme["fg"]).grid(row=0, column=0)
	Label(helps,text = "\n\n\tOuvrir un fichier save\n\n\tSauvegarder la grille actuelle\n\n\tRéinitialise la grille actuelle\n\n\tZoom Plus\n\n\tZoom Moins\n\n\tPause / Play\n\n\tFait bouger la grille", bg=theme["bg"], fg = theme["fg"]).grid(row=0, column=1)
	helps.mainloop()
        
def credit():
	cre = Tk()
	cre.title("Crédits")
	Label(cre,text="\n \t Jeu créé par Damien DASSEUX & Arnaud DIONISIUS \t \n", bg=theme["bg"], fg = theme["fg"]).grid(row=0, column=0)
	cre.mainloop()

def JeuFamille(): # Arnaud
        def afficher(can, posCellsCan):
                can.delete(ALL)

                # On crée le grillage
                for x in range(resolution[0]):
                        can.create_line(pas*x,0,pas*x,height)
                for y in range(resolution[1]):
                        can.create_line(0,pas*y,width,pas*y)

        # On dessine toutes le cellules qui sont dans tout les différents stades
                for i in range(len(posCellsCan)):

                        x0 = (posCellsCan[i][0]) * pas
                        y0 = (posCellsCan[i][1]) * pas
                        x1 = x0 + pas
                        y1 = y0 + pas

                        can.create_rectangle(x0 , y0 , x1 , y1 , fill=couleur[1]) # On dessine un rectangle noire

        def click_caseF(cells, can, lp, event):
                x , y = event.x, event.y # on prend la position de la souris

                i = 0 # la position des cases
                j = 0 # la position des cases
                while pas * i <= x:
                        i = i + 1
                while pas * j <= y:
                        j = j + 1

                pos_case_clicke = [i-1, j-1] # cette variable contient le numéro de colone et de ligne de la case clické

        # on regarde si cette cellule n'est pas présente dans le tableau de vie
                if pos_case_clicke in cells:
                        cells.remove(pos_case_clicke) # si c'est le cas, on supprime la cellule

                else : 
                        if len(cells)>=Nocells:
                                showinfo("Nombre de cellules","Vous avez utilisé toutes vos cellules !")
                        else:
                                cells.append(pos_case_clicke)

                if len(cells)>Nocells: lp["text"]="nombre de cellules restantes: 0"
                else: lp["text"]="nombre de cellules restantes:" + str(Nocells-len(cells))
                
                afficher(can, cells)

        def Tim(posCellsCan1, posCellsCan2, can1, can2, t1):
                t1 = t1 + 1
                algoF0(posCellsCan1, can1)
                algoF0(posCellsCan2, can2)
                t = Timer(0.2, lambda t1 = t1, posCellsCan1 = posCellsCan1, posCellsCan2 = posCellsCan2, can1 = can1, can2 = can2: Tim(posCellsCan1, posCellsCan2, can1, can2, t1))
                t.start()
                if t1 == 50 : 
                        t.cancel()              
        def  Ok(player, playerOk, posCellsCan1, posCellsCan2, can1, can2):
                playerOk.append(player)
                if 1 in playerOk and 2 in playerOk:
                        #for i in range(51):
                                #t = Timer(0.8, lambda player = player, playerOk = playerOk, posCellsCan1 = posCellsCan1, posCellsCan2 = posCellsCan2, can1 = can1, can2 = can2: Ok(player, playerOk, posCellsCan1, posCellsCan2, can1, can2))
                                #t.start()
                        #       algoF0(posCellsCan1, can1)
                        #       algoF0(posCellsCan2, can2)
                        Tim(posCellsCan1, posCellsCan2, can1, can2, 0)
                        if len(posCellsCan1) > len(posCellsCan2):
                                showinfo("Gagnant", "Le premier joueur a gagné")
                        elif len(posCellsCan1) < len(posCellsCan2):
                                showinfo("Gagnant", "Le deuxième joueur a gagné")
                        else:
                                showinfo("Gagnant", "Egalité")

                        posCellsCan1 = []
                        posCellsCan2 = []
                        playerOk = []
                        Nocells = 15

        def algoF0(cells, can):
                algoF(cells)
                afficher(can, cells)

        Jeu = Tk()
        Jeu.configure(bg=theme["bg"])
        Jeu.title("Jeu famille")

        posCellsCan1 = []
        posCellsCan2 = []
        playerOk = []
        Nocells = 15
        
        lp1 = Label(Jeu,text="nombre de cellules restantes:"+str(Nocells))
        lp1.configure(bg=theme["bg"], fg = theme["fg"])
        lp1.grid(row=2, column=0)
        
        lp2 = Label(Jeu,text="nombre de cellules restantes:"+str(Nocells))
        lp2.configure(bg=theme["bg"], fg = theme["fg"])
        lp2.grid(row=2, column=2)

        can1 = Canvas(Jeu, width = width  / 2 , height=height  / 2, bg=theme["Canvasbg"])
        can1.grid(row=0, column=0)
        can1.bind("<Button-1>", lambda event, cells = posCellsCan1, can = can1, lp = lp1: click_caseF(cells, can, lp, event))# lambda est une fonction permettant de mettre plusieurs argments contrairement à une methode classique

        espace = Label(Jeu, text="\t")
        espace.configure(bg=theme["bg"], fg = theme["fg"])
        espace.grid(row=0, column=1)

        can2 = Canvas(Jeu, width = width  / 2 , height=height  / 2, bg=theme["Canvasbg"])
        can2.grid(row=0, column=2)
        can2.bind("<Button-1>", lambda event, cells = posCellsCan2, can = can2, lp = lp2: click_caseF(cells, can, lp, event))

        bp1 = Button(Jeu, text="Ok", command= lambda playerOk = playerOk, posCellsCan1 = posCellsCan1, posCellsCan2 = posCellsCan2, can1 = can1, can2 = can2: Ok(1, playerOk, posCellsCan1, posCellsCan2, can1, can2)) # Boutton player 1 | labmda : crée une fonction anonyme qui appelle une autre fonction
        bp2 = Button(Jeu, text="Ok", command= lambda playerOk = playerOk, posCellsCan1 = posCellsCan1, posCellsCan2 = posCellsCan2, can1 = can1, can2 = can2: Ok(2, playerOk, posCellsCan1, posCellsCan2, can1, can2)) # Boutton player 2 

        bp1.configure(bg=theme["Buttonbg"], activebackground=theme["Buttonactivebackground"],  fg = theme["fg"] )
        bp2.configure(bg=theme["Buttonbg"], activebackground=theme["Buttonactivebackground"],  fg = theme["fg"] )

        bp1.grid(row=1, column=0)
        bp2.grid(row=1, column=2)
        
        for x in range(resolution[0]):
                can1.create_line(pas*x,0,pas*x,height  /  2)
                can2.create_line(pas*x,0,pas*x,height  /  2)
        for y in range(resolution[1]):
                can1.create_line(0,pas*y,width  /  2,pas*y)
                can2.create_line(0,pas*y,width  /  2,pas*y)

        Jeu.mainloop()

def selection(event):
	global choix
	choix = lst.get(lst.curselection())

import json # besoins pour les préférences
from threading import Timer

try :
    from tkinter import *
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    from tkinter.messagebox import showerror, showinfo
except ImportError:
    print("""Tkinter n'est pas intallé sur votre machine ou vous avez lancé ce programme avec Python2.X\n
    	      auquel cas je vous demanderais de lancer le programme avec Python3.X.""")
    variableInutile = input("\n\nAppuyer sur entrer pour quitter")# en fait cela sert à attendre que l'utilisateur appui sur "entrer" pour arrerter le programme
    exit()

fen = Tk() # Initialisation de la fenetre
fen.title("Game of Life") # On lui donne un titre
try:
    fen.iconbitmap("icon.ico")
except:
    print("il n'est pas possible d'afficher l'image")
fen.resizable(width=False, height=False)

choix = "stade 1" # Cette partie permet de défini le choix du stade d'écriture

pos = [0,0] # cette variable permet de controler le déplacement dans le game of life

fichierpreference = open("preference/preference.json", "r")  # On ouvre le fichier de préference
preference = json.load(fichierpreference) # on transforme son contenu en dictionnaire
fichierpreference.close() # fermeture du fichier

fichiertheme = open("preference/theme/"+preference["theme"], "r") # Ouverture du fichier de theme
theme = json.load(fichiertheme) # transforamtion du contenu en dictionnaire
fichiertheme.close() # fermeture du fichier

fichierJeuFamille = open("preference/JeuFamille/algoFamille.py", "r") # Overture algoF Arnaud
exec(fichierJeuFamille.read()) # execution du prgm
fichierJeuFamille.close()# fermeture du fichier

couleur = preference["couleur"] # on définit les couleur des cellules

algo = "algo/" + preference["algo_de_base"] # on défini la path relative de l'algorithme

exec(open(algo, "r").read()) # on l'execute

pas = preference["pas"] # On définit ici les variable dont on va avoir besoins plus tard
width = preference["width"]
height = preference["height"]
resolution = [int(width / pas), int(height / pas)]
play = False
gen = 0
gen_IntVar = IntVar()
gen_IntVar.set(0)

# On défini tout les stade de cellules possible
stade_1 = []
stade_2 = []
stade_3 = []
stade_4 = []
stade_5 = []

# On crée un canvas
can = Canvas(fen, width =width, height=height, bg=theme["Canvasbg"])

# On crée un grillage
"""
for x in range(resolution[0]+1):
	can.create_line(pas*x,0,pas*x,height*2)
for y in range(resolution[1]+1):
	can.create_line(0,pas*y,width*2,pas*y)
"""
reload()

affichageGeneration = Label(fen, textvariable=gen_IntVar) # on crée un label qui sert à montrer à quelle génération on en est
affichageGeneration.configure(bg=theme["bg"], fg = theme["fg"])
affichageGeneration.grid(row=2, column=2) # on l'affiche à un certain emplacement

boutonReset = Button(fen, text="Reset", command=reset) # on crée un bouton qui sert à reset le canvas
boutonReset.configure(bg=theme["Buttonbg"], activebackground=theme["Buttonactivebackground"], fg = theme["fg"] )
boutonReset.grid(row = 2, column= 1) # on l'affiche à un certain emplacement

boutonNext = Button(fen, text="Next", command=next) 
boutonNext.configure(bg=theme["Buttonbg"], activebackground=theme["Buttonactivebackground"], fg = theme["fg"] )
boutonNext.grid(row = 1, column = 1)

boutonJouer = Button(fen, text="Play", command=jouer)
boutonJouer.configure(bg=theme["Buttonbg"], activebackground=theme["Buttonactivebackground"], fg = theme["fg"] )
boutonJouer.grid(row = 1, column = 0)

boutonStop = Button(fen, text="Stop", command=stopper)
boutonStop.configure(bg=theme["Buttonbg"], activebackground=theme["Buttonactivebackground"], fg = theme["fg"] )
boutonStop.grid(row = 1, column = 2)

can.bind("<Button-1>", click_case)
can.grid(row=0, column=1)

lst = Listbox(fen)
lst.insert(0, "stade 1")
lst.insert(1, "stade 2")
lst.insert(2, "stade 3")
lst.insert(3, "stade 4")
lst.insert(4, "stade 5")
lst.configure(bg=theme["bg"], height=5, selectbackground=theme["Listeboxselectbackground"], fg=theme["fg"])
lst.bind("<ButtonRelease-1>", selection)
lst.grid(row=0, column=0)
lst.select_set(0)

menubar = Menu(fen)

filemenu = Menu(menubar)
filemenu.add_command(label="Ouvrir (O)", command= Ouvrir)
filemenu.add_command(label="Sauver (S)", command= Sauver)
filemenu.add_separator()
filemenu.add_command(label="Quitter", command=fen.quit)
menubar.add_cascade(label="Fichier", menu=filemenu)

menufamille = Menu(menubar)
menufamille.add_command(label="Ecran partagé", command=JeuFamille)
menubar.add_cascade(label="Jeu", menu = menufamille)

menuPreference = Menu(menubar)
menuPreference.add_command(label="Changer d'algorithme", command=lambda preference = preference, play = play:changerAlgo(preference, play))
menuPreference.add_command(label="Changer de theme", command=lambda preference = preference, play = play:changerTheme(preference, play))
menubar.add_cascade(label="Préférence", menu = menuPreference)

menuapropos = Menu(menubar)
menuapropos.add_command(label="aide", command=aide)
menuapropos.add_command(label="crédits", command=credit)
menubar.add_cascade(label="à propos", menu = menuapropos)

fen.config(menu=menubar)
fen.configure(bg =theme["bg"])
fen.bind("<Key-o>",  Ouvrir)
fen.bind("<Key-s>", Sauver)
fen.bind("<Key-r>", reset)
fen.bind("<Key-Down>", goDown)
fen.bind("<Key-Up>", goUp)
fen.bind("<Key-Left>", goLeft)
fen.bind("<Key-Right>", goRight)
fen.bind("<Key-p>", zoomP)
fen.bind("<Key-m>", zoomM)
fen.bind("<space>", spaceBar)
fen.mainloop()
