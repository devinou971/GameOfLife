def voisinage(x, y):# permet de connaitre le nombre de voisins qu'à une cellule
	global old_grid# On appelle old_grid
	voisins = 0

	#On vérifie 1 à 1 les 8 cases 
	if [x-1,y-1] in old_grid: 
		voisins = voisins + 1
	if [x-1,y] in old_grid:
		voisins = voisins +1
	if [x-1,y+1] in old_grid:
		voisins = voisins +1
	if [x,y+1] in old_grid:
		voisins = voisins +1
	if [x,y-1] in old_grid:
		voisins = voisins +1
	if [x+1,y-1] in old_grid:
		voisins = voisins +1
	if [x+1,y+1] in old_grid:
		voisins = voisins +1
	if [x+1,y] in old_grid:
		voisins = voisins +1
	return voisins


def algorithme(stade_1, stade_2, stade_3, stade_4, stade_5): # Le coeur du programme
	global old_grid
	old_grid = []
	for i in range(len(stade_1)): # On copie stade_1 dans old_grid
		old_grid.append(stade_1[i])
		
	for i in range(len(old_grid)-1, -1, -1): # on décremente pour ne pas sauter de cases
                x = old_grid[i][0]
                y = old_grid[i][1]
                nbvoisins = voisinage(x, y)
                if nbvoisins > 3:
                        del stade_1[i]
                if nbvoisins < 2:
                        del stade_1[i]
                        
                if nbvoisins >= 1 and nbvoisins <= 7 : # reproduction
                        if not [x-1,y-1] in stade_1:
                                voisins = voisinage(x-1, y-1)
                                if voisins == 3 :
                                        stade_1.append([x-1,y-1])
                        if not [x,y-1] in stade_1:
                                voisins = voisinage(x, y-1)
                                if voisins == 3 :
                                        stade_1.append([x,y-1])
                        if not [x+1,y-1] in stade_1:
                                voisins = voisinage(x+1, y-1)
                                if voisins == 3 :
                                        stade_1.append([x+1,y-1])
                        if not [x-1,y] in stade_1:
                                voisins = voisinage(x-1, y)
                                if voisins == 3 :
                                        stade_1.append([x-1,y])
                        if not [x+1,y] in stade_1:
                                voisins = voisinage(x+1, y)
                                if voisins == 3 :
                                        stade_1.append([x+1,y])
                        if not [x-1,y+1] in stade_1:
                                voisins = voisinage(x-1, y+1)
                                if voisins == 3 :
                                        stade_1.append([x-1,y+1])
                        if not [x,y+1] in stade_1:
                                voisins = voisinage(x, y+1)
                                if voisins == 3 :
                                        stade_1.append([x,y+1])
                        if not [x+1,y+1] in stade_1:
                                voisins = voisinage(x+1, y+1)
                                if voisins == 3:
                                        stade_1.append([x+1,y+1])