#import maths
#----combien de cube dans une figure ?-------------------------------------------------------------------------------------------------------------------------------------------

def nb_cube(figure):
	#print("nb_cube")
	"""
	donne le nombre de place occupee dans une figure
	figure :	figure a obtenir, matrice 3D
	"""
	nb = 0
	for i in range (len(figure)):
		for j in range (len(figure[0])):
			for k in range (len(figure[0][0])):
				if figure[i][j][k].num != 0 :
					nb += 1
	return nb

