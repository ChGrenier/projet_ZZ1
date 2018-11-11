"""
contient l'initialisation de la figure à réaliser et les fonctions qui permettent de placer des cube dedant
"""


import definition_cube as d
import ordres as o
import gestion_figure as gf

#----dictionnaire des faces des cubes--------------------------------------------------------------------------------------------------------------------------------------------

fichier = open(o.nom_fichier_cubes, 'r')

"""
creation d'un dictionnaire contenant toutes les faces des cubes repertories dans le fichier ouvert sous la forme num: liste des faces
faces_cubes : 	dictionnaire des cubes et de leur faces
C : 		variable temporaire de recuperation des donnees sous forme de chaine de caracteres
"""

faces_cubes = {} 
for line in fichier:
	C=line.split(";")
	faces_cubes[int(C[0])] = [int(i) for i in C[1].split(",")]

fichier.close()

#----dictionnaire des objets cubes-----------------------------------------------------------------------------------------------------------------------------------------------

"""
creation dun dictionnaire contenant les objets cubes a partir du dictionnaire des faces
position_init : 	position initiale du cube, a l'exterieur de la figure
angle_init :		angle initiale du cube
L_voisins_init :	liste initiale des voisins du cube, initialisee a 0, de la forme [Y-1, Z+1, X+1, Z-1, X-1, Y+1]
objets_cubes :		dictionnaire des objets cubes avec leur carateristiques (.X, .Y, .Z, .orientation, .L_faces, .num, .L_voisins, .angle)
"""

objets_cubes = {}
for i in faces_cubes:
	objets_cubes[i] = d.Cube(o.position_init, faces_cubes[i], i, o.L_voisins_init, o.angle_init)


#----verification de la compatibilite de deux cubes------------------------------------------------------------------------------------------------------------------------------

def compatibilite(cube_1, cube_2, dico_cube):
	"""
	retourne True si un cube peu bien etre place a l'endroi designe et False sinon
	compare les faces en contacte (forme, complementarite) et verifie que les cubes sont sous le meme angle entre un cube et chacun de ses voisins
	cube_1 :	numero du premier cube a comparer, int
	cube_2 :	numero du deuxieme cube a comparer, int
	dico_cube :	dictionnaire d'objets cubes
	ok :		booleen verifiant si les cubes sont compatibles ou non 
	"""
	if dico_cube[cube_1].X < dico_cube[cube_2].X :
		ok = (dico_cube[cube_1].L_faces[2] + dico_cube[cube_2].L_faces[4] == 0 and dico_cube[cube_1].angle == dico_cube[cube_2].angle)

	elif dico_cube[cube_1].X > dico_cube[cube_2].X :
		ok = (dico_cube[cube_1].L_faces[4] + dico_cube[cube_2].L_faces[2] == 0 and dico_cube[cube_1].angle == dico_cube[cube_2].angle)

	elif dico_cube[cube_1].Y < dico_cube[cube_2].Y :
		ok = (dico_cube[cube_1].L_faces[5] + dico_cube[cube_2].L_faces[0] == 0 and dico_cube[cube_1].angle == dico_cube[cube_2].angle)

	elif dico_cube[cube_1].Y > dico_cube[cube_2].Y :
		ok = (dico_cube[cube_1].L_faces[0] + dico_cube[cube_2].L_faces[5] == 0 and dico_cube[cube_1].angle == dico_cube[cube_2].angle)

	elif dico_cube[cube_1].Z < dico_cube[cube_2].Z :
		ok = (dico_cube[cube_1].L_faces[1] + dico_cube[cube_2].L_faces[3] == 0 and dico_cube[cube_1].angle == dico_cube[cube_2].angle)

	elif dico_cube[cube_1].Z > dico_cube[cube_2].Z :
		ok = (dico_cube[cube_1].L_faces[3] + dico_cube[cube_2].L_faces[1] == 0 and dico_cube[cube_1].angle == dico_cube[cube_2].angle)
	
	return ok

#----mise a jour de la liste des voisins-----------------------------------------------------------------------------------------------------------------------------------------

def MAJ_L_voisins(dico_cube, cube, figure):
	"""
	met a jour la liste des voisin du cube numero cube dans le dictionnaire dico_cube
	dico_cube :	dictionnaire d'objets
	cube :		numero du cube, int
	figure : 	figure a realiser
	"""
	#si la coordonnee que l'on verifi est dans la figure et que le contenu de la figure en cette coordonnee est differant de 0 alors :
		#ajouter le numero du cube qui s'y trouve a la liste des voisins du cube par rapport auquel on travail
	

	if dico_cube[cube].X + 1 < len(figure) and figure[dico_cube[cube].X + 1][dico_cube[cube].Y][dico_cube[cube].Z].num == 0 :
		dico_cube[cube].L_voisins[2] = figure[dico_cube[cube].X + 1][dico_cube[cube].Y][dico_cube[cube].Z].num

	if dico_cube[cube].Y + 1 < len(figure[0]) and figure[dico_cube[cube].X][dico_cube[cube].Y + 1][dico_cube[cube].Z].num == 0 :
		dico_cube[cube].L_voisins[5] = figure[dico_cube[cube].X][dico_cube[cube].Y + 1][dico_cube[cube].Z].num

	if dico_cube[cube].Z + 1 < len(figure[0][0]) and figure[dico_cube[cube].X][dico_cube[cube].Y][dico_cube[cube].Z + 1].num == 0 :
		dico_cube[cube].L_voisins[1] = figure[dico_cube[cube].X][dico_cube[cube].Y][dico_cube[cube].Z + 1].num

	if dico_cube[cube].X - 1 > 0 and figure[dico_cube[cube].X - 1][dico_cube[cube].Y][dico_cube[cube].Z].num == 0 :
		dico_cube[cube].L_voisins[4] = figure[dico_cube[cube].X - 1][dico_cube[cube].Y][dico_cube[cube].Z].num

	if dico_cube[cube].Y - 1 > 0 and figure[dico_cube[cube].X][dico_cube[cube].Y - 1][dico_cube[cube].Z].num == 0 :
		dico_cube[cube].L_voisins[0] = figure[dico_cube[cube].X][dico_cube[cube].Y - 1][dico_cube[cube].Z].num

	if dico_cube[cube].Z - 1 > 0 and figure[dico_cube[cube].X][dico_cube[cube].Y][dico_cube[cube].Z - 1].num == 0 :
		dico_cube[cube].L_voisins[3] = figure[dico_cube[cube].X][dico_cube[cube].Y][dico_cube[cube].Z - 1].num



	#ajouter une liste de voisins mis a jour pour savoir qui d'autre metre a jour dans le voisinage ?

#----demande de placement--------------------------------------------------------------------------------------------------------------------------------------------------------

def placement_possible(position, cube, figure, dico_cube):
	"""
	retourn True si le placement est possible et False sinon
	position :	coordonnees ou l'on veut placer le cube, triplet
	cube :		numero du cube a placer, int
	figure :	figure a obtenir, matrice 3D
	dico_cube :	dictionnaire d'objets cubes
	ok :		booleen verifiant si le placement est possible ou non
	"""
	MAJ_L_voisins(dico_cube, cube, figure)
	ok = True
	i = 0
	while ok and i< len(dico_cube[cube].L_voisins) :
		if dico_cube[cube].L_voisins[i] != 0 and ok :
			ok = compatibilite(dico_cube[cube], dico_cube[i], dico_cube)
		i+=1
	return ok



#----placement d'un cube dans la figure------------------------------------------------------------------------------------------------------------------------------------------

def placer_cube(position, cube, figure, dico_cube):
	"""
	place un cube dans la matrice de la forme et met a jour la liste des voisins de ce cube et de ceux autour
	position :	coordonnees ou l'on veut placer le cube dans la figure, triplet
	cube :		numero du cube a placer, int
	figure :	figure a obtenir, matrice 3D
	dico_cube :	dicionnaire d'objets cubes
	"""
	place=False
	if placement_possible(position, cube, figure, dico_cube) and not gf.present(cube, figure):
		if position[0] <len(figure) and position[1] <len(figure[0]) and position[2] <len(figure[0][0]) and position[0] >=0 and position[1] >=0 and position[2] >=0 :
			figure[position[0]][position[1]][position[2]] = dico_cube[cube]

			dico_cube[cube].X = position[0]
			dico_cube[cube].Y = position[1]
			dico_cube[cube].Z = position[2]
			place=True

			MAJ_L_voisins(dico_cube, cube, figure)

			#metre a jour les liste de voisins des voisins
			for i in dico_cube[cube].L_voisins :
				if i != 0 :
					MAJ_L_voisins(dico_cube, i, figure) #pas tres optimal...
	return place

#----retirer un cube de la figure------------------------------------------------------------------------------------------------------------------------------------------------

def retirer_cube_C(cube, figure, dico_cube):
	"""
	retire un cube de la matrice de la forme a partir du numero du cube et met a jour la liste des voisins de ce cube et de ceux autour
	cube :		numero du cube a placer, int
	figure :	figure a obtenir, matrice 3D
	dico_cube :	dicionnaire d'objets cubes
	"""
	figure[dico_cube[cube].X][dico_cube[cube].X][dico_cube[cube].X] = dico_cube[0]

	dico_cube[cube].X = -1
	dico_cube[cube].Y = -1
	dico_cube[cube].Z = -1

	MAJ_L_voisins(dico_cube, cube, figure)

	#metre a jour les liste de voisins des voisins
	for i in dico_cube[cube].L_voisins :
		if i != 0 :
			MAJ_L_voisins(dico_cube, i, figure) #pas tres optimal...


def retirer_cube_P(position, figure, dico_cube):
	"""
	retire un cube de la matrice de la forme a partire d'une position et met a jour la liste des voisins de ce cube et de ceux autour
	position :	coordonnees ou l'on veut placer le cube dans la figure, triplet
	figure :	figure a obtenir, matrice 3D
	dico_cube :	dicionnaire d'objets cubes
	"""
	if position[0] < len(figure) and position[1] < len(figure[0]) and position[2] < len(figure[0][0]) and position[0] >= 0 and position[1] >= 0 and position[2] >= 0 :

		cube = figure[position[0]][position[1]][position[2]].num			
		figure[position[0]][position[1]][position[2]] = dico_cube[0]

		dico_cube[cube].X = -1
		dico_cube[cube].Y = -1
		dico_cube[cube].Z = -1

		MAJ_L_voisins(dico_cube, cube, figure)

	
		#metre a jour les liste de voisins des voisins
		for i in dico_cube[cube].L_voisins :
			if i != 0 :
				MAJ_L_voisins(dico_cube, i, figure) #pas tres optimal...
	return cube
	


































