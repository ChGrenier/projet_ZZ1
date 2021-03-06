import gestion_cubes as g

#----initialisation de la figure-------------------------------------------------------------------------------------------------------------------------------------------------

"""
creation de la figure que l'on souhaite obtenir, initialise a 0 la matrice 3D de la forme a realiser
forme de type parallellepipede rectangle : longeur, largeur, hauteur
longueur : 	longeur de la forme a obtenir, dimension selon X
largeur : 	largeur de la forme a obtenir, dimension selon Y
hauteur : 	hauteur de la forme a obtenir, dimension selon Z

"""
def init_fig(hauteur, largeur, longueur):
	return [[[g.objets_cubes[0] for k in range(hauteur)] for j in range(largeur)]for i in range(longueur)]



#----cube deja dans la figure ?--------------------------------------------------------------------------------------------------------------------------------------------------

def present(cube, figure):
	"""
	verifi si un cube est present ou on dans la figure
	cube :		numero du cube a placer, int
	figure :	figure a obtenir, matrice 3D
	present :	test si le sube est present, booleen
	"""
	present = False
	i = 0
	while not present and i<len(figure):
		present=cube in figure[i]
		i+=1
	return present

#----affichage de la figure------------------------------------------------------------------------------------------------------------------------------------------------------

def afficher_fig(figure):
	"""
	affiche les numeros (ou autre si modifie) des cubes present dans la figure passee en parametre
	figure :	figure a obtenir, matrice 3D
	"""
	R = [[[figure[i][j][k].num for k in range (len(figure[0][0]))] for j in range (len(figure[0]))] for i in range (len(figure))]
	print(R)

#---liste des cubes dans la figure-----------------------------------------------------------------------------------------------------------------------------------------------

def liste_cube_fig(figure):
	cube=[]
	for i in range (len(figure)):
		for j in range (len(figure[0])):
			for k in range (len(figure[0][0])):
				if figure[i][j][k].num!=0 :
					cube.append(figure[i][j][k].num)
	return cube


#----liste des cubes pas encore utilises-----------------------------------------------------------------------------------------------------------------------------------------

def Cubes_libre_fig(figure):
	"""
	constitution de la liste des cubes encore disponible en vu de les placer
	figure :	figure a obtenir, matrice 3D
	cubes_libre :	liste des cube encore disponibles par rapport a la figure donnee
	"""
	cubes_libres=[]
	for i in range (1,28) :
		if present(i, figure):
			cubes_libres.append(i)
	return cubes_libres


#---suppresion des figure en double dans la liste des sous solution--------------------------------------------------------------------------------------------------------------

def en_double(liste_fig) :
	for i in liste_fig :
		if liste_fig.count(i)>1 :
			liste_fig.remove(i)
	return(liste_fig)


#----supression des figure contenant des cubes en double-------------------------------------------------------------------------------------------------------------------------

def doublon(liste_fig):
	for i in liste_fig :
		lst=liste_cube_fig(i)
		dbl=False
		j=0
		while not dbl and j<len(lst) :
			dbl=not(lst.count(lst[j])==1 or lst[j]==0)
			j+=1
		if dbl :
			liste_fig.remove(i)
	return(liste_fig)





