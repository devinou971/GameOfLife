def voisinageF(x, y):# permet de connaitre le nombre de voisins qu'à une cellule
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


def algoF(cell): # Le coeur du programme
	global old_grid
	old_grid = []
	for i in range(len(cell)): # On copie cell dans old_grid
		old_grid.append(cell[i])

	for i in range(len(old_grid)-1, -1, -1):
		nbvoisins = voisinage(old_grid[i][0], old_grid[i][1])
		if nbvoisins > 3:
			del cell[i]
		if nbvoisins < 2:
			del cell[i]
		x = old_grid[i][0]
		y = old_grid[i][1]
		if nbvoisins >= 1 and nbvoisins <= 7 :
			if not [x-1,y-1] in cell:
				voisins = voisinage(x-1, y-1)
				if voisins == 3 :
					cell.append([x-1,y-1])
			if not [x,y-1] in cell:
				voisins = voisinage(x, y-1)
				if voisins == 3 :
					cell.append([x,y-1])
			if not [x+1,y-1] in cell:
				voisins = voisinage(x+1, y-1)
				if voisins == 3 :
					cell.append([x+1,y-1])
			if not [x-1,y] in cell:
				voisins = voisinage(x-1, y)
				if voisins == 3 :
					cell.append([x-1,y])
			if not [x+1,y] in cell:
				voisins = voisinage(x+1, y)
				if voisins == 3 :
					cell.append([x+1,y])
			if not [x-1,y+1] in cell:
				voisins = voisinage(x-1, y+1)
				if voisins == 3 :
					cell.append([x-1,y+1])
			if not [x,y+1] in cell:
				voisins = voisinage(x, y+1)
				if voisins == 3 :
					cell.append([x,y+1])
			if not [x+1,y+1] in cell:
				voisins = voisinage(x+1, y+1)
				if voisins == 3:
					cell.append([x+1,y+1])