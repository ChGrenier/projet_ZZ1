import maths
#----combien de cube dans une figure ?-------------------------------------------------------------------------------------------------------------------------------------------

def nb_cube(figure):
	"""
	donne le nombre de place occupee dans une figure
	figure :	figure a obtenir, matrice 3D
	"""
	nb = 0
	for i in range len(figure):
		for j in range len(figure[0]):
			for k in range len(figure[0][0]):
				if figure[i][j][k].num != 0 :
					nb += 1
	return nb

#----qui est la meilleur entre deux figure ?-------------------------------------------------------------------------------------------------------------------------------------

def meilleur(figure1, figure2):
	"""
	determine qui est la meilleur entre deux figures (nombre de cube), retourn True si la premiere figure donnee est la meilleur et Flase sinon
	figure1 :	premiere figure comparee, matrice 3D
	figure2 :	deuxieme figure comparee, matrice 3D
	"""
	return (nb_cube(figure1) > nb_cube(figure2))#si egalite ca retourne que la figure 1 n'est pas la meilleur  
